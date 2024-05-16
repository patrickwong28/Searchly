def merge(index_one: str, index_two: str, chunk_size_mb: int):
    # get the alphabetical number at the end of each index name
    output_name = './inverse_index/indexes/index_' + index_one[30:] + index_two[30:]
    chunk_size_mb = chunk_size_mb * 1024 * 1024
    f1_remaining_chunk = ''
    f2_remaining_chunk = ''

    with open(index_one, 'r') as f1, open(index_two, 'r') as f2, open(output_name, 'w+') as output:
        # convert bytes to megabytes
        while True:
            f1_chunk_list, f1_remaining_chunk = build_chunk(f1.read(chunk_size_mb),f1_remaining_chunk)
            f2_chunk_list, f2_remaining_chunk = build_chunk(f2.read(chunk_size_mb),f2_remaining_chunk)

            if not f1_chunk_list and not f2_chunk_list:
                break

            f1_index = 0
            f2_index = 0

            while f1_index < len(f1_chunk_list) and f2_index < len(f2_chunk_list):
                f1_piece_key = f1_chunk_list[f1_index][0]
                f2_piece_key =  f2_chunk_list[f2_index][0]
                f1_piece_values = f1_chunk_list[f1_index][1]
                f2_piece_values = f2_chunk_list[f2_index][1]

                if f1_piece_key == f2_piece_key:
                    merged_values = f1_piece_values + f2_piece_values
                    merged_values.sort()
                    output.write(f'{f1_piece_key} --> ')
                    output.write(f'{convert_string(merged_values)}')
                    output.write(f'\n')
                    f1_index += 1
                    f2_index += 1
                elif f1_piece_key < f2_piece_key:
                    output.write(f'{f1_piece_key} --> ')
                    output.write(f'{convert_string(f1_piece_values)}')
                    output.write(f'\n')
                    f1_index += 1
                elif f1_piece_key > f2_piece_key:
                    output.write(f'{f2_piece_key} --> ')
                    output.write(f'{convert_string(f2_piece_values)}')
                    output.write(f'\n')
                    f2_index += 1
                    
            # now check for which chunk ended first, then append the rest of the other one
            if f1_index >= len(f1_chunk_list):
                while f2_index < len(f2_chunk_list):
                    output.write(f'{f2_piece_key} --> ')
                    output.write(f'{convert_string(f2_piece_values)}')
                    output.write(f'\n')
                    f2_index += 1
            elif f2_index >= len(f2_chunk_list):
                while f1_index < len(f1_chunk_list):
                    output.write(f'{f1_piece_key} --> ')
                    output.write(f'{convert_string(f1_piece_values)}')
                    output.write(f'\n')
                    f1_index += 1


def build_chunk(current_chunk, previous_incomplete_chunk: str) -> tuple[list[tuple], str]:
    chunk_list = []
    chunk = previous_incomplete_chunk + current_chunk
    index_list = chunk.split('\n')
    
    for i in range(len(index_list) - 1):
        term_and_values = index_list[i].split(' --> ')
        term = term_and_values[0]
        values = term_and_values[1].split(', ')
        chunk_list.append((term, values))
    
    return chunk_list, index_list[-1]
    
def convert_string(values: list):
    result = ''
    for value in values:
        result += value + ', '

    return result[:-2]