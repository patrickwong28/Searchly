def compute_word_frequency(token_list: list[str]) -> dict:
    """
    Returns the frequency of each token in the token list
    """
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
