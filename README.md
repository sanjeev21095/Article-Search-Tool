# Article-Search-Tool
This project deals with searching for a relevant article based on keywords used to look up
for the article. Over the last few decades, scientific papers often come up with an section
called "key-words" to help look up for those articles online. But the vast multitude of such
documents makes it difficult to get to the right document. In order to go beyond search
keywords, it's important to build more meaningful keyword lists or databases that are rich
in context and take the searchers intent into account. This project aims to build such a
tool that will point to a right set of documents for the user on an offline interface.
### Step - 1 : Downlaod the dataset
The dataset is a set of accepted papers from the Neural Information Processing System
Conference, 2015 (NIPS 2015) Download from [here](https://www.kaggle.com/benhamner/nips-2015-papers/version/2/home) and also the code to get the papers are shown [here](https://github.com/benhamner/nips-2015-papers).
### Step - 2 : Dataset Cleaning
Good luck dealing with raw data!
This dataset is slightly corrupted and needs some cleaning. Use [Pdfminer](https://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python) tool to extract data from the downloaded pdf files to text files.
### Step - 3 : Clean up the dataset