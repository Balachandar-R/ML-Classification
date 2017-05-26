# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:29:21 2017

@author: U56648
"""

import nltk 
with open('C:\Users\U56648\Desktop\sample.txt', 'r') as f:
    sample = f.read()

print sample

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
print tagged_sentences
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
print chunked_sentences

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NN':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)

    entity_names.extend(extract_entity_names(tree))

# Print all entity names
#print entity_names

# Print unique entity names
print set(entity_names)