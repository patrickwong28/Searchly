from pathlib import Path
from bs4 import BeautifulSoup
import json

def build_index(documents: list[Path]) -> dict:
    inverted_index = {}
    n = 0
    for document in documents:
        n = n + 1

        # decode json file
        json_file = open(document)
        data = json.load(json_file)

        # parse document
        
        