# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 12:33:28 2017

@author: U56648
"""

from nltk.corpus import treebank #import Tree banmodel from the corpus 
from nltk.tag import tnt #importing a tnt pos taggging
import pickle #For Pickle creation

#Split the Train and TEst data set as follows 
len(treebank.tagged_sents()) # length of the Treebank tagbag is 3914

#Make them to split according to the trian and Test Data

train_data = treebank.tagged_sents()[:3000]
test_data = treebank.tagged_sents()[3000:]

#to display the Sample train and Test data
print train_data[0]
print test_data[0]

#Building the model for TnT POS tagger as follows
tnt_pos_tagger = tnt.TnT()
tnt_pos_tagger.train(train_data)
accuracy = tnt_pos_tagger.evaluate(test_data)
print accuracy #Accuracy of this Model

#Creating a our own pickle 
f = open('tnt_treebank_pos_tagger.pickle', 'w')
pickle.dump(tnt_pos_tagger, f)
f.close()

#We can use this model for other POS tagging functions
tnt_pos_tagger.tag(nltk.word_tokenize("Whenever Machine learning is the "" + ( ) % 6 7 8 science of getting computers to act without being explicitly programmed. In the past decade, machine learning has given us self-driving cars, practical speech recognition, effective web search, and a vastly improved understanding of the human genome. Machine learning is so pervasive today that you probably use it dozens of times a day without knowing it. Many researchers also think it is the best way to make progress towards human-level AI. In this class, you will learn about the most effective machine learning techniques, and gain practice implementing them and getting them to work for yourself. More importantly, you'll learn about not only the theoretical underpinnings of learning, but also gain the practical know-how needed to quickly and powerfully apply these techniques to new problems. Finally, you'll learn about some of Silicon Valley's best practices in innovation as it pertains to machine learning and AI"))

