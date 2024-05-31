def map_posting_lengths(index_file: str) -> None:
    with open(index_file, 'r') as f, open('./inverse_index/mappings/index_lengths.txt', 'w+', encoding='utf-8') as output:
        while True:
            line = f.readline()
            if not line:
                break

            term, values = line.split(' --> ')
            # get length without actually creating the postings for less overhead
            length =  len(values.split(', '))
            output.write(f'{term} - {length}\n')

    print(f'Length mapping of {index_file} finished.')