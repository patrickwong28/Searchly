from search.utils.vector_creation import create_document_vector

def calculate_cosine_score(query_vector, document):
    document_vector = create_document_vector(document)
    score = 0
    for i in range(len(query_vector)):
        score += query_vector[i] * document_vector[i]

    return score

