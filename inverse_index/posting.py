class Posting:
    def __init__(self, docid: int, frequency: int) -> None:
        self.docid = docid
        self.frequency = frequency

    def docid(self):
        return self.docid

    def frequency(self):
        return self.frequency