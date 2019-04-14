import tkinter as tk
from tkinter import *
from tkinter import ttk
from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
import os,re
import string
from scipy.spatial.distance import cosine

#Edit this path to the "d2v.model" file
path1 = "C:/Users/Sanjeev Narayanan/Desktop/Sem 3/Neural Networks/Project/Updated GUI files/"
model = Doc2Vec.load(path1+"d2v.model")

#Edit this path to the "outs" folder
path = "C:/Users/Sanjeev Narayanan/Desktop/Sem 3/Neural Networks/Project/Updated GUI files/outs/"
path3 = "C:/Users/Sanjeev Narayanan/Desktop/Sem 3/Neural Networks/Project/Updated GUI files/pdfs/"

#Edit this path to the "glove.model" file

path2 = "C:/Users/Sanjeev Narayanan/Desktop/Sem 3/Neural Networks/Project/Updated GUI files/"

from glove import Glove
glove = Glove.load(path2+'glove.model')
#############################

filenames = []
all_files = []
title = []
for i in os.listdir(path):
    filenames.append(path + '%s' %i)
    with open(path+'%s' %i,'r',encoding='utf-8') as myfile:
        data = myfile.read()
    data = re.sub(r'([^\s\w]|_)+', '', data)
    data = "".join(filter(lambda char: char in string.printable, data))
    all_files.append(data)
    title.append(i.replace('-',' ')[5:].title().split('.')[0])

file2 = []
for i in os.listdir(path3):
    file2.append(path3 + '%s' %i)


class LoginPage():
   def __init__(self):
      self.root=tk.Tk()
      self.root.geometry("700x500+200+250")
      label = tk.Label(self.root, text="Paper Search Tool",fg="blue", font=("Arial Bold", 30))
      label.place(x=200,y=10)

      label_1 = tk.Label(self.root, text="Enter Search key 1")
      self.entry_1 = tk.Entry(self.root)
      label_1.place(x=200,y=170)
      self.entry_1.place(x=325,y=170)
      logbtn = tk.Button(self.root, text="Search", command = self._login_btn_clickked)
      logbtn.place(x=350,y=280)
      myButton = tk.Button(self.root, text="Exit",command = self.buttonPushed)
      myButton.grid(row=10)

      self.root.mainloop()

   def buttonPushed(self):
      self.root.destroy()

   def _login_btn_clickked(self):
      #print("Clicked")
      self.search1 = self.entry_1.get()
      
      list1 = word_tokenize(self.search1.lower())
      if len(self.search1)==0:          
          label4 = tk.Label(self.root, text="Cannot leave any field blank!",fg="red", font=("Arial Bold", 15))
          label4.place(x=200,y=320)
          
      elif len(self.search1)!=0:
          for item in range(len(list1)):
              try:
                  glove.most_similar(list1[item])
                  label4 = tk.Label(self.root, text="                                                                                                        ", font=("Arial Bold", 15))
                  label4.place(x=200,y=340+(40*item))
                           
              except Exception:
                  print("works, Word %s is invalid! Please edit" %(list1[item]))
                  label4s = tk.Label(self.root, text="Word %s is invalid! Please edit" %(list1[item]) ,fg="red", font=("Arial Bold", 15))
                  label4s.place(x=200,y=340+(40*item))
                  
          temp = []            
          if len(self.search1)!=0:
              for item in range(len(list1)):
                  if glove.most_similar(list1[item]):
                      temp.append(list1[item])
              
              if temp == list1:
                  label4 = tk.Label(self.root, text="                                                                                                        ", font=("Arial Bold", 15))
                  label4.place(x=200,y=320)
                  RP = resultspage(self.search1)
              
          else:
              pass

      else:
          label4 = tk.Label(self.root, text="                                                         ", font=("Arial Bold", 15))
          label4.place(x=200,y=320)
          RP = resultspage(self.search1)


class resultspage():
    
    def __init__(self,list1):
        self.root=tk.Tk()
        self.root.geometry("700x500+200+250")
        self.choice1 = 11
        self.var1 = StringVar()
        label = tk.Label(self.root, text="Paper Search Tool",fg="blue", font=("Arial Bold", 30))
        label.place(x=200,y=10)
        myButton = tk.Button(self.root, text="Exit",command = self.buttonPushed)
        myButton.grid(row=10)
        scrollbar = ttk.Scrollbar(self.root)
        listbox = tk.Listbox(self.root,width = 100)
        listbox.place(x=40,y=100)
        list2= word_tokenize(list1.lower())
        v1 = model.infer_vector(list2, steps=20, alpha=0.025)
        similar_doc = model.docvecs.most_similar(positive=[v1])
        
        
#        myButton2 = tk.Button(self.root, text="View Papers",command = self.viewpapers)
#        myButton2.place(x=200,y=300)
        
        myButton3 = tk.Button(self.root, text="Verify Papers",command = self.verify)
        myButton3.place(x=300,y=70)
        
        
        out_docs = []
        for i in similar_doc:
            out_docs.append(title[int(i[0])])
        
        for i in range(len(out_docs)):
            listbox.insert(END, "%s" %(out_docs[i]))
            
        self.outer = out_docs
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        
        variable = StringVar(self.root)
        variable.set("View Papers") # default value
        w = OptionMenu(self.root, variable, "%s"%(out_docs[0]), "%s"%(out_docs[1]), "%s"%(out_docs[2]),"%s"%(out_docs[3]), "%s"%(out_docs[4]), "%s"%(out_docs[5]),"%s"%(out_docs[6]), "%s"%(out_docs[7]), "%s"%(out_docs[8]),"%s"%(out_docs[9]))
        w.place(x=100,y=300)
        
        def ok():
            tle = variable.get()
            for i in range(len(title)):
                if title[i]==tle:
                    val = i
            from os import startfile
            startfile(file2[val])
        
        button = Button(self.root, text="OK", command=ok)
        button.place(x=70,y=303)
        
        
        
        self.root.mainloop()
    
    def buttonPushed(self):
        self.root.destroy()
    
    def verify(self):
        VP=verify_paps(self.outer)
     


class verify_paps():
    def __init__(self,out_docs):
        self.root=tk.Tk()
        self.root.geometry("1000x650+100+150")
        label = tk.Label(self.root, text="Paper Search Tool - Verify Papers",fg="blue", font=("Arial Bold", 15))
        label.place(x=350,y=10)
        myButton = tk.Button(self.root, text="Exit",command = self.buttonPushed)
        myButton.grid(row=10)
        variable1 = StringVar(self.root)
        variable1.set("Choose Article 1")
        variable2 = StringVar(self.root)
        variable2.set("Choose Article 2")# default value
        label_1 = tk.Label(self.root, text="Paper 1 :")
        label_1.place(x=100,y=105)
        label_2 = tk.Label(self.root, text="Paper 2:")
        label_2.place(x=100,y=145)
        w1 = OptionMenu(self.root, variable1, "%s"%(out_docs[0]), "%s"%(out_docs[1]), "%s"%(out_docs[2]),"%s"%(out_docs[3]), "%s"%(out_docs[4]), "%s"%(out_docs[5]),"%s"%(out_docs[6]), "%s"%(out_docs[7]), "%s"%(out_docs[8]),"%s"%(out_docs[9]))
        w1.place(x=150,y=100)
        w2 = OptionMenu(self.root, variable2, "%s"%(out_docs[0]), "%s"%(out_docs[1]), "%s"%(out_docs[2]),"%s"%(out_docs[3]), "%s"%(out_docs[4]), "%s"%(out_docs[5]),"%s"%(out_docs[6]), "%s"%(out_docs[7]), "%s"%(out_docs[8]),"%s"%(out_docs[9]))
        w2.place(x=150,y=140)
        def ok():
            tle1 = variable1.get()
            tle2 = variable2.get()
            for i in range(len(title)):
                if title[i]==tle1:
                    val1 = i
            for i in range(len(title)):
                if title[i]==tle2:
                    val2 = i
            print(val1,val2)
            if val1==val2:
                label = tk.Label(self.root, text="Pick the second Article different from the first topic!",fg="red", font=("Arial Bold", 10))
                label.place(x=175,y=170)
            else:
                label = tk.Label(self.root, text="                                                                                                 ",fg="red", font=("Arial Bold", 10))
                label.place(x=170,y=170)
                
                label100 = tk.Label(self.root, text="Paper 1", font=("Verdana", 12))
                label100.place(x=200,y=200)
                label200 = tk.Label(self.root, text="Paper 2", font=("Verdana", 12))
                label200.place(x=660,y=200)
                T1 = tk.Text(self.root,height = 15, width = 40, font=("Helvetica", 12))
                T1.place(x=50,y=250)
                self.quote1 = all_files[val1]
#                self.stringfiles1 = [" ".join([l for l in self.quote1])]
                T1.insert(END, self.quote1)
                T1.config(state=DISABLED)
                
                T2 = tk.Text(self.root,height = 15, width = 40, font=("Helvetica", 12))
                T2.place(x=500,y=250)
                self.quote2 = all_files[val2]
#                self.stringfiles2 = [" ".join([l for l in self.quote2])]
                T2.insert(END, self.quote2)
                T2.config(state=DISABLED)
                
                
                label_1 = tk.Label(self.root, text="Enter text here", font=("Helvetica", 12))
                self.entry_1 = tk.Entry(self.root, font=("Verdana", 10))
                label_1.place(x=80,y=550)
                self.entry_1.place(x=200,y=540,width=500,height = 55)
                
                logbtn = tk.Button(self.root, text="Predict", command = self._login_btn_clickked,height = 3,width = 10)
                logbtn.place(x=700,y=540)
                logbtn2 = tk.Button(self.root, text="Clear", command = self.buttonPushed,height = 3,width = 10)
                logbtn2.place(x=770,y=540)
        
        button = Button(self.root, text="OK", command=ok)
        button.place(x=70,y=125)
        self.root.mainloop()   
    def buttonPushed(self):
        self.root.destroy()
    def _login_btn_clickked(self):
        self.search1 = self.entry_1.get()
        if len(self.search1)>0:
            
            self.model1 = model
            self.model2 = model
            
            self.test_data = word_tokenize(self.search1.lower())
            v1 = self.model1.infer_vector(self.test_data, steps=20, alpha=0.025)
            v2 = self.model2.infer_vector(self.test_data, steps=20, alpha=0.025)
            v01 = self.model1.infer_vector(self.quote1, steps=20, alpha=0.025)
            v02 = self.model2.infer_vector(self.quote2, steps=20, alpha=0.025)
            distance1 = cosine(v1,v01)
            distance2 = cosine(v2,v02)
            print(distance1,distance2)
            print(self.search1,"@#$@#$")
                  
            if distance1>distance2:
                label300 = tk.Label(self.root, text="                                                       ", font=("Helvetica", 14))
                label300.place(x=300,y=600)
                label300 = tk.Label(self.root, text="Closest article is from Paper 1",fg="green", font=("Helvetica", 14))
                label300.place(x=300,y=600)
            else:
                label300 = tk.Label(self.root, text="                                                       ", font=("Helvetica", 14))
                label300.place(x=300,y=600)
                label300 = tk.Label(self.root, text="Closest article is from Paper 2",fg="green", font=("Helvetica", 14))
                label300.place(x=300,y=600)
                
        else:
            pass

        
LP=LoginPage()

