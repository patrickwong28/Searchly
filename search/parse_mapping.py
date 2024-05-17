def parse_mapping(mapping_file):
    result = {}
    with open(mapping_file, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break

            key_and_value = line.split(' - ')
            key = key_and_value[0]
            value = key_and_value[1]

            result[key] = value

    return result

