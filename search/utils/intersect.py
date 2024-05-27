from inverse_index.posting import Posting
def merge(query1_postings: list[Posting], query2_postings: list[Posting], prev_merge_dict: dict) -> list[Posting]:
    result = []
    new_merge_dict = {}
    query1_index = 0
    query2_index = 0
    
    while query1_index < len(query1_postings) and query2_index < len(query2_postings):
        query1_posting = query1_postings[query1_index]
        query2_posting = query2_postings[query2_index]
        if query1_posting.docid == query2_posting.docid:
            result.append(query1_postings[query1_index])

            if query1_posting.docid not in new_merge_dict:
                new_merge_dict[query1_posting.docid] = []       
            new_merge_dict[query1_posting.docid].append(query2_posting)

            query1_index += 1
            query2_index += 1
        elif query1_posting.docid < query2_posting.docid:
            query1_index += 1
        else:
            query2_index += 1

    if len(prev_merge_dict) != 0:
        for docid in new_merge_dict.keys():
            if docid in prev_merge_dict:
                new_merge_dict[docid] = prev_merge_dict[docid] + new_merge_dict[docid]
    
    return result, new_merge_dict
