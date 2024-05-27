from inverse_index.utils.conversion import str_to_postings
from search.utils.intersect import merge

def boolean_retrieval(index_mapping, query_dict) -> dict:
    try:
        fetched_results = []
    
        with open('./inverse_index/indexes/index_abc.txt', 'r', encoding='utf-8') as f:
            for word in query_dict.keys():
                f.seek(int(index_mapping[word]))
                line = f.readline()
                term, values = line.split(' --> ')
                fetched_results.append((term, str_to_postings(values)))
                
            fetched_results.sort(key=lambda x: len(x[1]))
            term_ordering = [result[0] for result in fetched_results]
            postings_list = [result[1] for result in fetched_results]
            merged_results = postings_list[0]
            merge_dict = {}
            
            for i in range(len(fetched_results)):
                merged_results, merge_dict = merge(merged_results, postings_list[i], merge_dict)
    except KeyError:
        merged_results = []
        term_ordering = []
        merge_dict = {}

    return merged_results, merge_dict, term_ordering
