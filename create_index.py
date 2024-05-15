from inverse_index.retrieve_documents import retrieve_documents
from inverse_index.indexer import build_index
from pathlib import Path
import sys

if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise IndexError
        file_path = sys.argv[1]
        docs = retrieve_documents(file_path)
        index = build_index(docs)
    except FileNotFoundError:
        print('File not found!')
    


