from inverse_index.posting import Posting

def str_to_postings(string: str) -> list[Posting]:
    postings = []
    value_list = string.split(', ')
    for value in value_list:
        # remove parentheses and trailing \n operator
        value = value.strip().strip('()')
        attributes = value.split('; ')
        
        posting = Posting(int(attributes[0]), int(attributes[1]), float(attributes[2]), float(attributes[3]))
        postings.append(posting)

    return postings


def postings_to_str(postings: list[Posting]) -> str:
    posting_string = ''
    for posting in postings:  
        posting_string += f'({posting.docid}; {posting.frequency}; {posting.tf_idf}; {posting.doc_length}), '

    # remove last comma and space if exists
    if len(posting_string) != 0:
        posting_string = posting_string[:-2]

    
    return posting_string