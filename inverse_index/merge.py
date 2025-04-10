from inverse_index.utils.conversion import str_to_postings, postings_to_str
from inverse_index.posting import Posting
import os

def merge(index_one: str, index_two: str, chunk_size_mb: int) -> None:
    # get the alphabetical number at the end of each index name
    # [30:-4] to only retrieve the letters of index file name
    output_name = './inverse_index/indexes/index_' + index_one[30:-4] + index_two[30:-4] +'.txt'
    
    # converts bytes to megabytes
    chunk_size_mb = chunk_size_mb * 1024 * 1024
    f1_remaining_chunk = ''
    f2_remaining_chunk = ''

    with open(index_one, 'r', encoding='utf-8') as f1, open(index_two, 'r', encoding='utf-8') as f2, open(output_name, 'w+', encoding='utf-8') as output:
        f1_index = 0
        f2_index = 0
        # build first chunks
        f1_chunk_list, f1_remaining_chunk = build_chunk(f1.read(chunk_size_mb),f1_remaining_chunk)
        f2_chunk_list, f2_remaining_chunk = build_chunk(f2.read(chunk_size_mb),f2_remaining_chunk)


        while True:
            # if after merging, both chunks are empty
            if not f1_chunk_list and not f2_chunk_list:
                break
            
            # if after merging, there is remaining information in the second chunk
            if f1_chunk_list and not f2_chunk_list:
                while f1_index < len(f1_chunk_list):
                    f1_piece_key, f1_piece_values = f1_chunk_list[f1_index]
                    write_to_disk(f1_piece_key ,f1_piece_values, output)
                    f1_index += 1
                    break

            # if after merging, there is remaining information in the first chunk
            if not f1_chunk_list and f2_chunk_list:
                while f2_index < len(f2_chunk_list):
                    f2_piece_key, f2_piece_values = f2_chunk_list[f2_index]
                    write_to_disk(f2_piece_key, f2_piece_values, output)
                    f2_index += 1
                    break
            
            # while both chunks still have information on them, continue the merging
            while f1_index < len(f1_chunk_list) and f2_index < len(f2_chunk_list):
                f1_piece_key, f1_piece_values = f1_chunk_list[f1_index]
                f2_piece_key, f2_piece_values =  f2_chunk_list[f2_index]

                if f1_piece_key == f2_piece_key:
                    merged_values = f1_piece_values + f2_piece_values
                    merged_values.sort(key=lambda x: x.docid)
                    write_to_disk(f1_piece_key, merged_values, output)
                    f1_index += 1
                    f2_index += 1
                elif f1_piece_key < f2_piece_key:
                    write_to_disk(f1_piece_key, f1_piece_values, output)
                    f1_index += 1
                elif f1_piece_key > f2_piece_key:
                    write_to_disk(f2_piece_key, f2_piece_values, output)
                    f2_index += 1

            # check which chunk finished first and then retrieve a new chunk for the empty chunk
            if f1_index >= len(f1_chunk_list):
                f1_chunk_list, f1_remaining_chunk = build_chunk(f1.read(chunk_size_mb),f1_remaining_chunk)
                f1_index = 0

            if f2_index >= len(f2_chunk_list):
                f2_chunk_list, f2_remaining_chunk = build_chunk(f2.read(chunk_size_mb),f2_remaining_chunk)
                f2_index = 0

    # remove partial indexes after merge
    os.remove(index_one)
    os.remove(index_two)
    
    print(f'Merge of {output_name} completed.')


def build_chunk(current_chunk: tuple[str, list[Posting]], previous_incomplete_chunk: str) -> tuple[list[Posting], str]:
    chunk_list = []
    # add previous trailing chnk to beginning of new chunk
    chunk = previous_incomplete_chunk + current_chunk
    index_list = chunk.split('\n')
    
    # create chunk_list (the list of postings)
    for i in range(len(index_list) - 1):
        term_and_values = index_list[i].split(' --> ')
        term = term_and_values[0]
        values = str_to_postings(term_and_values[1])
        chunk_list.append((term, values))
    
    # return chunk and trailing chunk (the trailing chunk is an unfinished term index)
    return chunk_list, index_list[-1]

def write_to_disk(key: str, postings: list[Posting], output_file: str) -> None:
    output_file.write(f'{key} --> ')
    output_file.write(f'{postings_to_str(postings)}')
    output_file.write(f'\n')