from search.utils.intersect import merge
from porter2stemmer import Porter2Stemmer
from inverse_index.posting import Posting
from search.utils.parse_mapping import parse_mapping
from inverse_index.utils.conversion import str_to_postings
from search.utils.vector_creation import create_query_vector
from search.retrieval.boolean_retrieval import boolean_retrieval
from search.retrieval.document_retrieval import document_at_a_time_retrieval
import time

def run_interface():
    # load URL mapping and byte offset mapping and store them in dictionaries
    url_map = parse_mapping('./inverse_index/mappings/URL_mapping.txt')
    offset_map = parse_mapping('./inverse_index/mappings/index_offsets.txt')
    length_map = parse_mapping('./inverse_index/mappings/index_lengths.txt')

    while True:
        query = input('Query: ').lower()

        # measure execution time
        start_time = time.time()
        query_dict = create_query_dict(query)
        remove_common_query_terms(query_dict, length_map)
  
        if len(query_dict) != 0:
            merged_documents_dict, term_ordering = boolean_retrieval(offset_map, query_dict)
            print(len(merged_documents_dict))
            
            if len(merged_documents_dict) != 0:
                query_vector = create_query_vector(offset_map, query_dict, term_ordering, len(url_map))
                top_documents =  document_at_a_time_retrieval(query_vector, merged_documents_dict, 10)
                top_docids = [score_document_pair[1] for score_document_pair in top_documents]
                print_results(top_docids, url_map)
            
        print(f'Total query execution time: {int((time.time() - start_time) * 1000)} ms')

def create_query_dict(query: str):
    result = {}
    query_split = query.split()
    stemmer = Porter2Stemmer()
    for word in query_split:
        stemmed_word = stemmer.stem(word)
        if stemmed_word not in result:
            result[stemmed_word] = 0
        result[stemmed_word] += 1

    return result

def remove_common_query_terms(query_dict: dict, length_map: dict):
    for term in list(query_dict.keys()):
        if term in length_map:
            if int(length_map[term]) > 8000000:
                del query_dict[term]

def print_results(results: list[int], url_mapping: dict):
    for result in results:
        print(url_mapping[str(result)], end='')
