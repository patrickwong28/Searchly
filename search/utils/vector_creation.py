from inverse_index.utils.conversion import str_to_postings
from math import sqrt, log10
from inverse_index.posting import Posting

def create_query_vector(index_mapping, query_dict, query_ordering, number_of_documents):
    weight_vector = []
    doc_length = 0

    # create weight vector
    with open('./inverse_index/indexes/index_abc.txt', 'r') as f:
        query_lengths = []
        for query in query_ordering:
            if query in index_mapping:
                f.seek(int(index_mapping[query]))
                line = f.readline()
                postings_length = len(str_to_postings(line.split(' --> ')[1]))
                query_lengths.append(postings_length)

                weight = (1 + log10(query_dict[query])) * (log10(number_of_documents / postings_length))
                weight_vector.append(weight)

                doc_length += (weight ** 2)
    
    # normalize weight vector
    doc_length = sqrt(doc_length)
    result_vector = [weight / doc_length for weight in weight_vector]

    return result_vector, query_lengths


def create_document_vector(documents: list[Posting]):
    weight_vector = []
    doc_length = 0
    for posting in documents:
        weight = posting.tf_idf
        weight_vector.append(weight)
        doc_length = posting.doc_length
    
    # normalize weight vector
    result_vector = [weight / doc_length for weight in weight_vector]
        
    return result_vector
    

    