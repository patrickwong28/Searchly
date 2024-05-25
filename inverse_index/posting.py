class Posting:
    def __init__(self, docid: int, frequency: int, positions, tf_idf: float = 0) -> None:
        self.docid = docid
        self.frequency = frequency
        self.positions = positions
        self.tf_idf = tf_idf

    def docid(self):
        return self.docid

    def frequency(self):
        return self.frequency
    
    def positions(self):
        return self.positions
    
    def tf_idf(self):
        return self.tf_idf