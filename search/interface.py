from search.utils.intersect import merge
from porter2stemmer import Porter2Stemmer
from inverse_index.posting import Posting
from search.utils.parse_mapping import parse_mapping
from search.utils.vector_creation import create_query_vector
from search.retrieval.boolean_retrieval import boolean_retrieval
from search.retrieval.document_retrieval import document_at_a_time_retrieval
import time

def run_interface() -> None:
    # load URL mapping and byte offset mapping and store them in dictionaries
    url_map = parse_mapping('./inverse_index/mappings/URL_mapping.txt')
    offset_map = parse_mapping('./inverse_index/mappings/index_offsets.txt')
    length_map = parse_mapping('./inverse_index/mappings/index_lengths.txt')

    while True:
        print('Enter q to quit searching.')
        query = input('>>> ').lower()
        
        if query == 'q':
            break

        # measure execution time
        start_time = time.time()
        if query:
            unmodified_query_dict = create_query_dict(query)
            query_dict = remove_common_query_terms(unmodified_query_dict, length_map)
    
            if len(query_dict) != 0:
                merged_documents_dict, term_ordering = boolean_retrieval(offset_map, query_dict)
                print(f'Total documents found: {len(merged_documents_dict)}')
                
                if len(merged_documents_dict) != 0:
                    query_vector, query_lengths = create_query_vector(offset_map, query_dict, term_ordering, len(url_map))
                    top_documents =  document_at_a_time_retrieval(query_vector, query_lengths, merged_documents_dict, len(url_map), 10)
                    top_docids = [score_document_pair[1] for score_document_pair in top_documents]
                    print_results(top_docids, url_map)
            
        print(f'Total query execution time: {int((time.time() - start_time) * 1000)} ms')
        print()

def run_interface_web(user_query: str):
    # load URL mapping and byte offset mapping and store them in dictionaries
    url_map = parse_mapping('./inverse_index/mappings/URL_mapping.txt')
    offset_map = parse_mapping('./inverse_index/mappings/index_offsets.txt')
    length_map = parse_mapping('./inverse_index/mappings/index_lengths.txt')

    query = user_query.lower()

    # measure execution time
    start_time = time.time()
    unmodified_query_dict = create_query_dict(query)
    query_dict = remove_common_query_terms(unmodified_query_dict, length_map)

    if len(query_dict) != 0:
        merged_documents_dict, term_ordering = boolean_retrieval(offset_map, query_dict)
        
        if len(merged_documents_dict) != 0:
            query_vector, query_lengths = create_query_vector(offset_map, query_dict, term_ordering, len(url_map))
            top_documents =  document_at_a_time_retrieval(query_vector, query_lengths, merged_documents_dict, len(url_map), 10)
            top_docids = [score_document_pair[1] for score_document_pair in top_documents]
            result = []
            for docs in top_docids:
                result.append(url_map[str(docs)])
            
            execution_time = (time.time() - start_time) * 1000

            if result is None:
                return []
                
            return (result, execution_time)
        

def create_query_dict(query: str) -> dict:
    result = {}
    query_split = query.split()
    stemmer = Porter2Stemmer()
    for word in query_split:
        stemmed_word = stemmer.stem(word)
        if stemmed_word not in result:
            result[stemmed_word] = 0
        result[stemmed_word] += 1

    return result

def remove_common_query_terms(query_dict: dict, length_map: dict) -> dict:
    new_query_dict = {}
    for term in query_dict.keys():
        if term in length_map:
            # if term exists in index, check to see if a lot of documents have that term
            if int(length_map[term]) < 15000:
                new_query_dict[term] = query_dict[term]
        else:
            new_query_dict[term] = query_dict[term]
    
    # check to see if common words make up 75% of the query and if it does, we don't remove them
    if (1 - (len(new_query_dict) / len(query_dict))) > 0.75:
        return query_dict
    else:
        return new_query_dict
        
            

def print_results(results: list[int], url_mapping: dict) -> None:
    count = 1
    for result in results:
        print(f'#{count}: {url_mapping[str(result)]}', end='')
        count += 1
