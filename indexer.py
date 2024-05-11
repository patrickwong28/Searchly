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

    #URL mapping
    with open('URL_mapping.txt', 'w', encoding='utf-8') as f:
        pass

    for document in documents:
        n = n + 1

        # decode json file
        with open(document) as f:
            data = json.load(f)

        # print log information and mapping to file
        print(f'Doc #: {n} --> {document}')
        with open('URL_mapping.txt', 'a', encoding='utf-8') as f:
            f.write(f"{n} - {data['url']}\n")

        # parse document
        content = data['content']
        soup = BeautifulSoup(content, 'lxml')
        with open('current_page.txt', 'w+', encoding='utf-8') as f:
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
    
    # dump contents of index into a file to store on disk instead of memory
    with open('index.pkl', 'wb') as f:
        pickle.dump(inverted_index, f)

    return inverted_index