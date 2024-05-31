from search.utils.vector_creation import create_document_vector
from inverse_index.posting import Posting
from math import log10

def calculate_relevance_score(query_vector: list[float], query_lengths: list[int], documents:list[Posting], number_of_documents: int) -> float:
    cosine_score = calculate_cosine_score(query_vector, documents)
    
    relevance_score = cosine_score
    return relevance_score


def calculate_cosine_score(query_vector: list[float], documents: list[Posting]) -> float:
    document_vector = create_document_vector(documents)
    score = 0
    for i in range(len(query_vector)):
        score += query_vector[i] * document_vector[i]

    return score


def calculate_tfidf_score(documents: list[Posting], query_lengths: list[int], number_of_documents: int) -> float:
    # need to calculate actual tfidf score as this is only the tf raw score
    score = 0
    for i in range(len(documents)):
        score += documents[i].tf_idf * (log10(number_of_documents / query_lengths[i]))
    
    return score


