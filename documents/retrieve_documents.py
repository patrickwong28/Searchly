
from pathlib import Path
from document import Document

def retrieve_documents(start_path: str) -> list[Document]:
    documents = []
    for path in Path(start_path).rglob('*.json'):
        documents.append(path)

    return documents


