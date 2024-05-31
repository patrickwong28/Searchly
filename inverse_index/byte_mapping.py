def map_byte_offsets(index_file: str) -> None:
    with open(index_file, 'rb') as f, open('./inverse_index/mappings/index_offsets.txt', 'w+', encoding='utf-8') as output:
        current_byte_offset = 0
        while True:
            line = f.readline()
            if not line:
                break
        
            token = line.decode(encoding='utf-8').split(' --> ')[0]

            # write to output file
            output.write(f'{token} - {current_byte_offset}\n')
            
            # since in a txt file, every character is a single byte, we can get length of line
            current_byte_offset += len(line)
            
    print(f'Byte mapping of {index_file} finished.')