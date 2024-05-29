def map_posting_lengths(index_file: str):
    with open(index_file, 'r') as f, open('./inverse_index/mappings/index_lengths.txt', 'w+', encoding='utf-8') as output:
        while True:
            line = f.readline()
            if not line:
                break
        
            term, values = line.split(' --> ')
            length =  len(values.split(', '))
            output.write(f'{term} - {length}\n')
