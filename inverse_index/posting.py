class Posting:
    def __init__(self, docid: int, frequency: int, tf_idf: float, doc_length: float) -> None:
        self.docid = docid
        self.frequency = frequency
        self.tf_idf = tf_idf
        self.doc_length = doc_length

    def docid(self):
        return self.docid

    def frequency(self):
        return self.frequency
    
    def tf_idf(self):
        return self.tf_idf
    
    def doc_length(self):
        return self.doc_length