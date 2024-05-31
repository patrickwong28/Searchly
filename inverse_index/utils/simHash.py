import hashlib
from collections import defaultdict
import nltk
import re

def simhash(text, hash_bits=64):
    # Step 1: Tokenize the text and count word occurrences
    cleaned_text = re.sub(r'[^A-Za-z0-9 ]+', ' ', text.lower())
    words = nltk.word_tokenize(cleaned_text)
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1 # format [word, freq]

    # Step 2: Create a vector of size hash_bits initialized to zero
    v = [0] * hash_bits # initailize with the bit we have

    # Step 3: For each word, generate a hash and update vector
    for word, count in word_count.items():
        # Generate a hash value
        hash_value = int(hashlib.md5(word.encode('utf-8')).hexdigest(), 16)
            # To hash, we need binary so we encode the word string into bytes using UTF-8 encoding
                # cause MD5 require byte data (can present universal char)
            # hashlib.md5 generate a new hash obj for md5 (128bits: 16-byte hash value) creating unique fixed-size hash from bytes
            # .hexdigest() is converting the binary to hex and then ".., 16" is convert to int for debugging and readability
        
        # Update vector components based on hash bits
        for i in range(hash_bits): 
            bit = (hash_value >> i) & 1
            # We need to loop thru each bit using bit shifting (>>)
                # then & by 1 to check if it's 0 or 1
            if bit == 1:
                v[i] += count # sum it up depend on the freq of the words 
            else: 
                v[i] -= count # subtract via word

    # Step 4: Derive the fingerprint
    fingerprint = 0
    for i in range(hash_bits):  
        if v[i] >= 0:
            fingerprint |= (1 << i) # |= set individual bit without alter them
                                    #   bit mask so that it only changes to where we want
                                    # << shift the bit to where we want  
    return fingerprint


def hash_similarity(hash1, hash2, hash_bits=64):
    # >> i & 1 for shifting bit to the least significant bit so we can isolate it 
    # to ensure each bit is checked 
    matching_bits = sum((hash1 >> i) & 1 == (hash2 >> i) & 1 for i in range(hash_bits)) 
    return matching_bits / hash_bits
