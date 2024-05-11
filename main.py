from documents.retrieve_documents import retrieve_documents
from indexer import build_index
from pathlib import Path
import os
import sys

def get_required_info(docs: list[Path], index: dict):
    number_of_documents = len(docs)
    unique_tokens = len(index)
    
    total_size_bytes = os.path.getsize('index.pkl')
    total_size_kb = total_size_bytes / 1024

    print(f'Number of documents  -->  {number_of_documents}')
    print(f'Number of unique tokens  -->  {unique_tokens}')
    print(f'Total Size (KB)  -->  {total_size_kb}')


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise IndexError
        file_path = sys.argv[1]
        docs = retrieve_documents(file_path)
        index = build_index(docs)
        print(index)
        get_required_info(docs, index)
    except FileNotFoundError:
        print('File not found!')
    except IndexError:
        print('Invalid amount of arguments!')
    


