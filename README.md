# COMPSCI 121 Assignment 3 Milestone 1

## **Program Summary**
The following program takes a folder from your computer and constructs and inverted index where the keys are the word tokens and the values are the documents that contain said token.  

The resulting response after processing will be in the following format:

```
Number of documents  -->  (Number of Documents)
Number of unique tokens  -->  (Unique Tokens)
Total Size (KB)  -->  (Total Size in KB)
```
Example Output:

```
Number of documents  -->  55393
Number of unique tokens  -->  1092500
Total Size (KB)  -->  252066.3720703125
```

## **How to Setup**
Open your terminal and install the following libraries:  
**BeautifulSoup** and **Porter2Stemmer**

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

After installing both libraries, run the program from main.py and enter in a file path after being asked for an input.

