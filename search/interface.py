from search.intersect import merge
import pickle
from porter2stemmer import Porter2Stemmer

def run_interface():
    with open('index.pkl', 'rb') as f:
        inverted_index = pickle.load(f)


    while True:
        query = input('Query: ').lower()
        query_list = filter_words(query)
        split_query = []

        stemmer = Porter2Stemmer()
        for word in query_list:
            split_query.append(stemmer.stem(word))

    
        if len(split_query) == 1:
            try:
                merge_result = inverted_index[split_query[0]]
            except KeyError:
                merge_result = []
            merge_ids = list(map(lambda x: str(x.docid), merge_result))
            print(merge_ids)

            with open('URL_mapping.txt', 'r') as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    if line.startswith(tuple(merge_ids)):
                        print(line)
        print()

def filter_words(query: str):
    query_list = query.split()
    return query_list

def print_results():
    pass