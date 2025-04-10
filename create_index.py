from inverse_index.retrieve_documents import retrieve_documents
from inverse_index.indexer import build_index
from inverse_index.merge import merge
from inverse_index.byte_mapping import map_byte_offsets
from inverse_index.length_mapping import map_posting_lengths
import sys
import os

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise IndexError
        file_path = sys.argv[1]

        # create directories to store indexes and mappings
        if not os.path.exists('./inverse_index/indexes'):
            os.mkdir('./inverse_index/indexes')
        if not os.path.exists('./inverse_index/mappings'):
            os.mkdir('./inverse_index/mappings')

        docs = retrieve_documents(file_path)
        build_index(docs)
        
        merge('./inverse_index/indexes/index_a.txt', './inverse_index/indexes/index_b.txt', 10)
        merge('./inverse_index/indexes/index_ab.txt', './inverse_index/indexes/index_c.txt', 10)
        map_byte_offsets('./inverse_index/indexes/index_abc.txt')
        map_posting_lengths('./inverse_index/indexes/index_abc.txt')
        
    except FileNotFoundError:
        print('File not found!')
    except IndexError:
        print('Invalid amount of arguments!')

