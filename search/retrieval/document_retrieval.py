from search.utils.intersect import merge
from inverse_index.utils.conversion import str_to_postings
from queue import PriorityQueue
from search.utils.score import calculate_cosine_score

def document_at_a_time_retrieval(query_vector, document_dict, result_count):
    result = PriorityQueue()
    for docid in document_dict.keys():
        score = calculate_cosine_score(query_vector, document_dict[docid])
        result.put(((-1) * score, docid))
    
    # return only top 10 results
    result_list = []
    for i in range(result_count):

        if result.qsize() == 0:
            break
        result_list.append(result.get())
    return result_list
    