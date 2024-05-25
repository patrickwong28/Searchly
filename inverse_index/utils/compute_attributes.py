from inverse_index.utils.conversion import str_to_postings, postings_to_str
from math import log10
import os

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

def compute_tf_idf(index_file, output):
    with open(index_file, 'r') as f, open(output, 'w+') as output:
        while True:
            line = f.readline()
            
            if not line:
                break
            key, values = line.split(' --> ')
            postings = str_to_postings(values)
        
            df = len(postings)
            for posting in postings:
                # update tf_idf to actual score instead of placeholder 0
                # df does not need to be logged due to the weighing scheme: lnc.ltc
                posting.tf_idf =  (1 + log10(posting.frequency)) * df

            output.write(f'{key} --> ')
            output.write(f'{postings_to_str(postings)}')
            output.write(f'\n')

    # remove used index
    os.remove(index_file)
    print('tf-idf scores calculations completed.')