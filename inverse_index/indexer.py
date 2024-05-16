from pathlib import Path
from bs4 import BeautifulSoup
import json
from inverse_index.parse import tokenize, compute_word_frequency
from porter2stemmer import Porter2Stemmer
from inverse_index.posting import Posting


def build_index(documents: list[Path]) -> dict:
    inverted_index = {}
    n = 0
    batch_of_documents = []
    batch_size = (len(documents) // 3) + 1
    batch_names = ['./inverse_index/indexes/index_a', './inverse_index/indexes/index_b', './inverse_index/indexes/index_c']
    batch_number = 0

    #URL mapping
    with open('./inverse_index/mappings/URL_mapping.txt', 'w', encoding='utf-8') as f:
        pass

    while len(documents) != 0:
        batch_of_documents = get_batch(documents, batch_size)

        # create partial index file
        with open(batch_names[batch_number], 'w+') as f:
            pass

        for document in batch_of_documents:
            n = n + 1

            # decode json file
            with open(document) as f:
                data = json.load(f)

            # print log information and mapping to file
            print(f'Doc #: {n} --> {document}')
            with open('./inverse_index/mappings/URL_mapping.txt', 'a', encoding='utf-8') as f:
                f.write(f"{n} - {data['url']}\n")

            # parse document
            content = data['content']
            soup = BeautifulSoup(content, 'lxml')
            with open('./inverse_index/current_page.txt', 'w+', encoding='utf-8') as f:
                f.write(soup.text)
            
            tokens = tokenize('./inverse_index/current_page.txt')
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

        sort_and_write_to_disk(inverted_index, batch_names[batch_number])
        batch_number += 1
        inverted_index = {}

    return inverted_index


def get_batch(documents: list[Path], size: int):
    document_chunk = []

    for i in range(size):
        if len(documents) == 0:
            return document_chunk
        else:
            document_chunk.append(documents.pop())
    return document_chunk
    

def postings_str(postings: list[Posting]) -> str:

    posting_string = ''
    for posting in postings:
        posting_string += f'({posting.docid}; {posting.frequency}), '
    
    # remove lsat comma and space if exists
    if len(posting_string) != 0:
        posting_string = posting_string[:-2]
    
    return posting_string
    

def sort_and_write_to_disk(index: dict, name_of_file):
    # first sort the index values for faster retrieval later
    for value in index.values():
        value.sort(key = lambda x: x.docid)

    # now sort the terms for merging partial indexes later
    index = dict(sorted(index.items()))
    # writing to disk
    with open(name_of_file, 'a') as f:
        for key, value in index.items():
            f.write(f'{key} --> ')
            f.write(postings_str(value))
            f.write('\n')

        
