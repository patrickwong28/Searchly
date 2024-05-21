class Posting:
    def __init__(self, docid: int, frequency: int, positions) -> None:
        self.docid = docid
        self.frequency = frequency
        self.positions = positions

    def docid(self):
        return self.docid

    def frequency(self):
        return self.frequency
    
    def positions(self):
        return self.positions