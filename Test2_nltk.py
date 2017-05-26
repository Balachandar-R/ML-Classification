# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 12:21:38 2017

@author: U56648
"""

from nltk import word_tokenize,pos_tag

text="The woman bought over $150,000 worth of clothes"

tokens = word_tokenize(text)

pos_values = pos_tag(tokens)

print pos_values
