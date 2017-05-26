# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 10:56:30 2017

@author: U56648
"""

from nltk import bigrams
from nltk import trigrams
import nltk

with open('C:\Users\U56648\Desktop\second_doc.txt', 'r') as f:
    sample = f.read()

text="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ornare
tempor lacus, quis pellentesque diam tempus vitae. Morbi justo mauris,
congue sit amet imperdiet ipsum dolor sit amet, consectetur adipiscing elit. Nullam ornare
tempor lacus, quis pellentesque diam"""

# split the texts into tokens
tokens = nltk.word_tokenize(text)
tokens = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
bi_tokens = bigrams(tokens)
tri_tokens = trigrams(tokens)

# print trigrams count
print [(item, tri_tokens.count(item)) for item in sorted(set(tri_tokens))]