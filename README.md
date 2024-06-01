# COMPSCI 121 Assignment 3
### Created by Justin Jue, Patrick Wong, Senghoung Lim, Justin Woo

## **Program Summary**
The following program allows you to construct an inverted index off of a given folder from your computer that contains json files of websites. After the creation of this index, you will be able to query the results and get the top 10 highest ranking documents for that said query search. 

Example Output of Querying Portion of Search Engine:

```
Enter q to quit searching.
>>> master of software engineering
Total documents found: 845
#1: https://www.ics.uci.edu/~lopes/
#2: https://mswe.ics.uci.edu/
#3: https://www.informatics.uci.edu/grad/student-profiles/#content
#4: https://www.informatics.uci.edu/undergrad/student-profiles/#content
#5: https://www.informatics.uci.edu/explore/blogs-we-author/
#6: https://www.informatics.uci.edu/impact/undergraduate-alumni-spotlights/
#7: https://mswe.ics.uci.edu/career/
#8: https://mswe.ics.uci.edu/program/
#9: https://mswe.ics.uci.edu/admissions/
#10: https://www.informatics.uci.edu/impact/graduate-alumni-spotlights/#content
Total query execution time: 33 ms
```

---
## **Setting Up Your Virtual Environment**
For the installation found later in this document, it might make sense to create a virtual envrionment to install all the needed add ons.  
To setup your virtual environment, open your terminal and enter the following command:  
**NOTE:** On macOS, use python3 instead of python
```
python -m venv <path>
```

Enter the following command to run your virtual environment:  
Windows:
```
.\venv\Scripts\activate
```

MacOS:
```
source \venv\bin\activate
```

---
## **How to Setup**
Open your terminal and install the following libraries:  
**BeautifulSoup**, **Porter2Stemmer**, **lxml**, **nltk** and **Flask**

To do this, use the following commands in terminal:  
(**NOTE:** If on macOS, use pip3 instead of pip)

BeautifulSoup:

```
pip install bs4
```

Porter2Stemmer:

```
pip install porter2stemmer
```

lxml:

```
pip install lxml
```

nltk:

```
pip install nltk
```

Flask:
```
pip install Flask
```

---

## **How to Use**
###  **Creation of Index Portion**
  
Open up terminal and enter the command in the following layout:  
**NOTE:** On macOS, use python3 instead of python  

```
python create_index.py [directory_path]
```
- directory_path would be the directory you want to use in order for the program to sift through all the json files.  
### **Query Search**
Open up terminal if you don't already have that open and enter the command in the following layout:  
**NOTE**: Again, if you are on macOS, use python3 instead of python

```
python query.py
```

Afterwards, you are then greeted with this output:  

```
Enter q to quit searching.
>>> 
```
Simply type any query you want in this, and it will output the top 10 highest ranking documents of that query.  
Once you are done, you can type 'q' within the search input and it will end the program.

### **Query Search for Web UI**
Enter the follow command in terminal:  
**NOTE**: Again, if you are on macOS, use python3 instead of python
```
python query_web.py
```

Afterwards, you are the greeted with this output:
```
 * Serving Flask app 'query_web'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 114-176-628
```
To open the Web UI, ctrl + click on the locally hosted server http://127.0.0.1:5000. A new tab should be opened on your web browser displaying the following website:

