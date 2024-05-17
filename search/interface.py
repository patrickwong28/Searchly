from search.intersect import merge
from porter2stemmer import Porter2Stemmer
from inverse_index.posting import Posting
from search.parse_mapping import parse_mapping
import time

def run_interface():
    # load URL mapping and byte offset mapping and store them in dictionaries
    url_map = parse_mapping('./inverse_index/mappings/URL_mapping.txt')
    offset_map = parse_mapping('./inverse_index/mappings/index_offsets.txt')

    while True:
        query = input('Query: ').lower()

        # measure execution time
        start_time = time.time()

        query_list = filter_words(query)

        try:
            fetched_results = []
            with open('./inverse_index/indexes/index_abc', 'r', encoding='utf-8') as f:
                for word in query_list:
                    f.seek(int(offset_map[word]))
                    line = f.readline()
                    values = line.split(' --> ')[1]
                    fetched_results.append(build_postings(values))
                fetched_results.sort(key=lambda x: len(x))
                merged_results = fetched_results[0]
                for i in range(1, len(fetched_results)):
                    merged_results = merge(merged_results, fetched_results[i])
        except KeyError:
            merged_results = []
        
        print_results(merged_results, url_map)
        print(f'Total query execution time: {int((time.time() - start_time) * 1000)} ms')
        
        
        

def build_postings(index_string) -> list[Posting]:
    posting_list = []
    string_list = index_string.strip().split(', ')
    for value in string_list:
        #[1:-1] to remove parentheses
        attributes = value[1:-1].split('; ')
        posting_list.append(Posting(int(attributes[0]), int(attributes[1])))

    return posting_list

def filter_words(query: str):
    result = []
    query_split = query.split()
    stemmer = Porter2Stemmer()
    for word in query_split:
        result.append(stemmer.stem(word))
    return result

def print_results(results: list[Posting], url_mapping: dict):
    if len(results) < 5:
        for result in results:
            print(url_mapping[str(result.docid)], end='')
    else:
        for i in range(5):
            print(url_mapping[str(results[i].docid)], end='')