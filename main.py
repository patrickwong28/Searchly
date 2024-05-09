from documents.retrieve_documents import retrieve_documents
from indexer import build_index
from pathlib import Path
import os

def get_required_info(docs: list[Path], index: dict):
    number_of_documents = len(docs)
    unique_tokens = len(index)
    # TODO: uncomment the comments here when dictionary file dump is added
    
    # total_size_bytes = os.path.getsize('index.json')
    # total_size_kb = total_size_bytes / 1024

    print(f'Number of documents  -->  {number_of_documents}')
    print(f'Number of unique tokens  -->  {unique_tokens}')
    # print(total_size_kb)


if __name__ == '__main__':
    file_path = input('Please provide the file path:')
    docs = retrieve_documents(file_path)
    index = build_index(docs)
    get_required_info(docs, index)

