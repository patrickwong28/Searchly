from pathlib import Path
from bs4 import BeautifulSoup
import json
from parse import tokenize
from porter2stemmer import Porter2Stemmer


def build_index(documents: list[Path]) -> dict:
    inverted_index = {}
    n = 0
    for document in documents:
        n = n + 1

        # decode json file
        with open(document) as f:
            data = json.load(f)

        # parse document
        content =  data['content']
        soup = BeautifulSoup(content, 'html.parser')
        with open('current_page.txt', 'w+') as f:
            f.write(soup.text)
        
        tokens = tokenize('current_page.txt')
        stemmer = Porter2Stemmer()
        stemmed_tokens = set()
        for token in tokens:
            stemmed_tokens.add(stemmer.stem(token))
        
        # TODO: wondering how we should create index to map
        # index and urls for faster access - Justin Jue

        # loop through tokens
        for token in tokens:
            pass
            # if all token t is element of T do
            #   i <-- List<Posting>()
            # end if
            # I.append(Posting(n))
        # end for
    # end for
    # return I
    # end procedure
            