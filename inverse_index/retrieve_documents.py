from pathlib import Path

def retrieve_documents(start_path: str) -> list[Path]:
    documents = []
    for path in Path(start_path).rglob('*.json'):
        documents.append(Path(path))

    return documents