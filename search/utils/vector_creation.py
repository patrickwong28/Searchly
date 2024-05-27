from inverse_index.utils.conversion import str_to_postings
from math import sqrt, exp2, log10
from inverse_index.posting import Posting

def create_query_vector(index_mapping, query_dict, query_ordering, number_of_documents):
    weight_vector = []
    doc_length = 0

    # create weight vector
    with open('./inverse_index/indexes/index_abc.txt', 'r') as f:
        for query in query_ordering:
            if query in index_mapping:
                f.seek(int(index_mapping[query]))
                line = f.readline()
                postings = str_to_postings(line.split(' --> ')[1])

                weight = (1 + log10(query_dict[query])) * (log10(number_of_documents / len(postings)))
                weight_vector.append(weight)

                doc_length += exp2(weight)
            else:
                weight_vector.append(0)
    
    # normalize weight vector
    doc_length = sqrt(doc_length)
    if doc_length != 0:
        result_vector = [weight / doc_length for weight in weight_vector]

    return result_vector


def create_document_vector(document: list[Posting]):
    weight_vector = []
    doc_length = 0
    for posting in document:
        weight = posting.tf_idf
        weight_vector.append(weight)
        doc_length += exp2(weight)
    
    # normalize weight vector
    doc_length = sqrt(doc_length)
    if doc_length != 0:
        result_vector = [weight / doc_length for weight in weight_vector]
    
    return result_vector
    

    