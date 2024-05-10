from pathlib import Path
from bs4 import BeautifulSoup
import json
from parse import tokenize, compute_word_frequency
from porter2stemmer import Porter2Stemmer
from posting import Posting
import pickle


def build_index(documents: list[Path]) -> dict:
    inverted_index = {}
    n = 0
    for document in documents:
        n = n + 1

        # print log information
        print(f'Doc #: {n} --> {document}')

        # decode json file
        with open(document) as f:
            data = json.load(f)

        # parse document
        content = data['content']
        soup = BeautifulSoup(content, 'lxml')
        with open('current_page.txt', 'w+') as f:
            f.write(soup.text)
        
        tokens = tokenize('current_page.txt')
        stemmer = Porter2Stemmer()
        stemmed_tokens = []
        for token in tokens:
            stemmed_tokens.append(stemmer.stem(token))
        
        stemmed_token_frequency =  compute_word_frequency(stemmed_tokens)

        # loop through tokens
        for token in stemmed_token_frequency.keys():
            if token not in inverted_index:
                inverted_index[token] = []
            inverted_index[token].append(Posting(n, stemmed_token_frequency[token]))
    
    #TODO: Add file dump here in order to dump dictioary contents onto disk storage
    with open('index.pkl', 'wb') as f:
        pickle.dump(inverted_index, f)

    return inverted_index