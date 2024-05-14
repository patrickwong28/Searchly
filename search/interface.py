from search.merge import merge
import pickle

def run_interface():
    with open('index.pkl', 'rb') as f:
        inverted_index = pickle.load(f)

    while True:
        query = input('Query: ')
        split_query = filter_words(query)
    
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