from inverse_index.posting import Posting
def merge(query1_postings: list[Posting], query2_postings: list[Posting]) -> list[Posting]:
    result = []
    query1_index = 0
    query2_index = 0
    
    while query1_index < len(query1_postings) and query2_index < len(query2_postings):
        if query1_postings[query1_index].docid == query2_postings[query2_index].docid:
            result.append(query1_postings[query1_index])
            query1_index += 1
            query2_index += 1
        elif query1_postings[query1_index].docid < query2_postings[query2_index].docid:
            query1_index += 1
        else:
            query2_index += 1
    
    return result
