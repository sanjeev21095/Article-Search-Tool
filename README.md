# [Article-Search-Tool](https://youtu.be/jgrfciDYHd4)
This project deals with searching for a relevant article based on keywords used to look up
for the article. Over the last few decades, scientific papers often come up with an section
called "key-words" to help look up for those articles online. But the vast multitude of such
documents makes it difficult to get to the right document. In order to go beyond search
keywords, it's important to build more meaningful keyword lists or databases that are rich
in context and take the searchers intent into account. This project aims to build such a
tool that will point to a right set of documents for the user on an offline interface.
### Step - 1 : Download the dataset
The dataset is a set of accepted papers from the Neural Information Processing System
Conference, 2015 (NIPS 2015) Download from [here](https://www.kaggle.com/benhamner/nips-2015-papers/version/2/home) and also the code to get the papers are shown [here](https://github.com/benhamner/nips-2015-papers). Parallely, download the pre-trained [GloVe Vectors](https://nlp.stanford.edu/projects/glove/). The first 100 files have been uploaded.
### Step - 2 : Dataset Cleaning
Good luck dealing with raw data!
This dataset is slightly corrupted and needs some cleaning. Use [Pdfminer](https://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python) tool to extract data from the downloaded pdf files to text files.
### Step - 3 : Clean up the dataset
This step is straightforward
1. Split each document into its title and body
2. Strip the document of links, citations, stop words and other special characters
3. Tokenize the words in the document
### Step - 4 : Training
Run the file [LSTM](https://github.com/sanjeev21095/Article-Search-Tool/blob/master/LSTM.py).py
### Step - 5 : Create the GUI
The GUI is made using tkinter. The link to the video on how to use the GUI is shown [here](https://youtu.be/jgrfciDYHd4). Detailed description of this project is compiled in the [Article Search Tool](https://github.com/sanjeev21095/Article-Search-Tool/blob/master/Article%20Search%20Tool.pdf) pdf file. Verify the model by making a [paragraph vector model](https://github.com/sanjeev21095/Article-Search-Tool/blob/master/verify_with_d2v.py) and checking if the input query are actua;y present in the article. 
