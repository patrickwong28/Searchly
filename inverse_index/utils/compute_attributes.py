from math import sqrt, log10

def compute_word_frequency(token_list: list[str]) -> dict:
    word_frequency = {}
    for token in token_list:
        if token not in word_frequency:
            word_frequency[token] = 1
        else:
            word_frequency[token] += 1
    
    return word_frequency

def compute_position(token_list: list[str]) -> dict:
    positions = {}
    current_position = 1
    for token in token_list:
        if token not in positions:
            positions[token] = []
        positions[token].append(current_position)
        current_position += 1

    return positions

def compute_doc_length(frequency_dict: dict) -> float:
    doc_length = 0
    for value in frequency_dict.values():
        tf_weighted = 1 + log10(value)
        doc_length += (tf_weighted ** 2)

    doc_length = sqrt(doc_length)

    return doc_length