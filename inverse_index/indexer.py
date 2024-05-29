from pathlib import Path
from bs4 import BeautifulSoup
import json
from inverse_index.utils.compute_attributes import compute_word_frequency, compute_position, compute_doc_length
from porter2stemmer import Porter2Stemmer
from inverse_index.posting import Posting
from inverse_index.utils.conversion import postings_to_str
from math import log10
import nltk
import re


def build_index(documents: list[Path]) -> dict:
    inverted_index = {}
    n = 0
    batch_of_documents = []
    batch_size = (len(documents) // 3) + 1
    batch_names = ['./inverse_index/indexes/index_a.txt', './inverse_index/indexes/index_b.txt', './inverse_index/indexes/index_c.txt']
    batch_number = 0
    nltk.download('punkt')

    #URL mapping
    with open('./inverse_index/mappings/URL_mapping.txt', 'w', encoding='utf-8') as f:
        pass

    while len(documents) != 0:
        batch_of_documents = get_batch(documents, batch_size)

        # create partial index file
        with open(batch_names[batch_number], 'w+', encoding='utf-8') as f:
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
            text = re.sub(r'[^A-Za-z0-9 ]+', ' ', soup.text.lower())
            tokens = nltk.word_tokenize(text)
            stemmer = Porter2Stemmer()
            stemmed_tokens = []
            for token in tokens:
                current_token = stemmer.stem(token)
                stemmed_tokens.append(current_token)

            stemmed_token_positions = compute_position(stemmed_tokens)
            stemmed_token_frequency =  compute_word_frequency(stemmed_tokens)
            doc_length = compute_doc_length(stemmed_token_frequency)

            # loop through tokens
            for token in stemmed_token_frequency.keys():
                if token not in inverted_index:
                    inverted_index[token] = []
                tf_idf = 1 + log10(stemmed_token_frequency[token])
                inverted_index[token].append(Posting(n, stemmed_token_frequency[token], stemmed_token_positions[token], tf_idf, doc_length))

        sort_and_write_to_disk(inverted_index, batch_names[batch_number])
        batch_number += 1
        inverted_index = {}


def get_batch(documents: list[Path], size: int):
    document_chunk = []

    for i in range(size):
        if len(documents) == 0:
            return document_chunk
        else:
            document_chunk.append(documents.pop())
    return document_chunk


def sort_and_write_to_disk(index: dict, name_of_file: str):
    # first sort the index values for faster retrieval later
    for value in index.values():
        value.sort(key = lambda x: x.docid)

    # now sort the terms for merging partial indexes later
    index = dict(sorted(index.items()))
    # writing to disk
    with open(name_of_file, 'a', encoding='utf-8') as f:
        for key, value in index.items():
            f.write(f'{key} --> ')
            f.write(postings_to_str(value))
            f.write('\n')