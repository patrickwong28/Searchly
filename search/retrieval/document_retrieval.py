from search.utils.intersect import merge
from inverse_index.utils.conversion import str_to_postings
from queue import PriorityQueue
from search.utils.score import calculate_relevance_score

def document_at_a_time_retrieval(query_vector: list[float], query_lengths: list[int], document_dict: dict, number_of_documents: int, result_count: int) -> list[tuple[float, int]]:
    result = PriorityQueue()
    
    # go through all documents and calculate the score for them
    for docid in document_dict.keys():
        score = calculate_relevance_score(query_vector, query_lengths, document_dict[docid], number_of_documents)
        result.put(((-1) * score, docid))
    
    # return the top documents depending on the result_count parameter
    result_list = []
    for i in range(result_count):
        # if the priority queue is empty, cut it off short and return all results
        if result.qsize() == 0:
            break
        result_list.append(result.get())
    return result_list
    