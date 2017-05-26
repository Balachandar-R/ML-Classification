# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:02:10 2017

@author: U56648
"""


#nltk.download()
import nltk
from nltk.corpus import brown
from nltk import sent_tokenize,word_tokenize,pos_tag

#Test to print 
print "Hello"

###
#Construct for Corpus Test
#print brown.words()[0:10]
#print brown.tagged_words()[0:10]
#print len(brown.words())
#print dir(brown)
###

#nltk.help.upenn_tagset()

#Sentence Tokenizer
sampleText="Whenever Machine learning is the "" + ( ) % 6 7 8 science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning and AI"
sampleText2='The woman bought over $150,000 worth of clothes'

def sentence_tokenize(text):    
    sentences = sent_tokenize(sampleText2)
    print "Sentence Tokenizer are"
    print sentences

def words_tokenize(text):
    tokens = word_tokenize(sampleText2)
    print "Length of the Tokens" ,len(tokens)
    print pos_tag(tokens)

def POS_tag(text):
    pos_tagging = pos_tag(sampleText2)
    print "POS Tagging with First String",pos_tagging
    #print "POS Tagging with Second String",pos_tagging

if __name__ == '__main__':
    sentence_tokenize(sampleText2)
    words_tokenize(sampleText2)
    POS_tag(sampleText2)

