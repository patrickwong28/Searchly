from inverse_index.posting import Posting

def str_to_postings(string: str) -> list[Posting]:
    postings = []
    value_list = string.split(', ')
    for value in value_list:
        # remove parentheses
        value = value[1:-1]
        attributes = value.split('; ')
        posting = Posting(int(attributes[0]), int(attributes[1]))
        postings.append(posting)

    return postings


def postings_to_str(postings: list[Posting]) -> str:

    posting_string = ''
    for posting in postings:
        posting_string += f'({posting.docid}; {posting.frequency}), '
    
    # remove lsat comma and space if exists
    if len(posting_string) != 0:
        posting_string = posting_string[:-2]
    
    return posting_string