from inverse_index.posting import Posting

def str_to_postings(string: str) -> list[Posting]:
    postings = []
    value_list = string.split(', ')
    for value in value_list:
        # remove parentheses
        value = value[1:-1]
        attributes = value.split('; ')

        # convert positions to an actual list
        position_list = [int(i) for i in attributes[2].split(',')]

        posting = Posting(int(attributes[0]), int(attributes[1]), position_list)
        postings.append(posting)

    return postings


def postings_to_str(postings: list[Posting]) -> str:

    posting_string = ''
    for posting in postings:
        position_str = ''
        for position in posting.positions:
            position_str += f'{position},'
        if len(position_str) != 0:
            position_str = position_str[:-1]
            
        posting_string += f'({posting.docid}; {posting.frequency}; {position_str}), '

    # remove last comma and space if exists
    if len(posting_string) != 0:
        posting_string = posting_string[:-2]

    
    return posting_string