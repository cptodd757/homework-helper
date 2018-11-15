import re
import string
import pandas as pd
import numpy as np
import pprint as pp
import io

def clean_sent(sentence,stopWords=[]):
    punctuation = string.punctuation
    sent = re.sub(r'http\S+', '', sentence) #Remove links starting with http
    sent = re.sub(r'www\S+', '', sent) #Remove links starting with www
    sent = re.sub("\d+", "", sent) #Remove numbers
    sent = [x if x not in punctuation else " " for x in sent] # Remove all punctuation
    sent = ''.join(sent)
    sent = ' '.join([x for x in sent.split() if x not in stopWords])
    return sent

sent="The quick! 1234 1 2 brown! fox ? jumps over the www.google.com/abc123 9lazy sleeping dog.       How quickly the daft Mr. Zebra  jumps. A long time ago in a galaxy far far away. "

clean_sent(sent)

import nltk

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
sentences=sent_tokenize(sent)

stopWords=stopwords.words('english')
pp.pprint(stopWords[0:10])

clean_sentences = [clean_sent(x, stopWords) for x in sentences]

# ## Vector Creation
# 
# <center>We want to now take our split sentences and turn them into vectors</center>
# 
# ### Bag of Words
# 
# Ignoring any notion of order, create a vector of the counts of words
# 
# Let's take the sentence:
# 
# ####  <center> "John likes to watch movies, Mary likes to watch movies too." <center>
# 
# Our bag of word construction is then:
# 
# | john | likes | mary | movies | too | to | watch |
# |------|-------|------|------- |-----|----| ----- |
# | 1    | 2     | 1    | 2      | 1   | 2  | 2     |
# 
# 
# We can do the same thing, but instead consider bigrams (all consecutive pairs of words)
# 
# <br>
# So, 
# 
# ####  <center> "John likes to watch movies, Mary likes to watch movies too." <center>
#     
# becomes,
# 
# 
# | john likes | likes to | to watch | watch movies | movies mary | mary likes | movies too |
# |------------|----------|----------|--------------|-------------|------------|------------|
# | 1          | 2        | 2        | 2            | 1           | 1          | 1          |
# 
# 
# 
# ### TF-IDF (Term Frequency  Inverse Document Frequency)
# 
# I'll glance over the math here, but essentially this downweights words that occur really frequently across many documents, and upweights words that occur frequently, but only in a few documents.

# In[ ]:


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(clean_sentences)

df=pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names())

from nltk.cluster.util import cosine_distance
def sentence_similarity(dfRow1,dfRow2):
    v1=dfRow1.as_matrix()[0]
    v2=dfRow2.as_matrix()[0]
    return 1-cosine_distance(v1,v2)

sentence_similarity(df.iloc[[3]],df.iloc[[3]])

def makeAdjMatrix(df):
    S = np.zeros((len(df.index), len(df.index)))
    for x in range(len(df.index)):
        for y in range(x+1,len(df.index)):
            sim = sentence_similarity(df.iloc[[x]],df.iloc[[y]])
            S[x][y]=sim
            S[y][x]=sim
    
    for idx in range(len(S)):
        rowSum = S[idx].sum()
        if rowSum>0: S[idx] /= S[idx].sum() 
    return S

A=makeAdjMatrix(df)

def pageRank(A, eps=0.0001, d=0.85):
    P = np.ones(len(A)) / len(A)
    while True:
        new_P = np.ones(len(A)) * (1 - d) / len(A) + d * A.T.dot(P)
        delta = abs(new_P - P).sum()
        if delta <= eps:
            return new_P
        P = new_P

def textRank(text,topN=5,stopWords=[],ngramRange=(1,1)):
    sentences=sent_tokenize(text)
    clean_sentences=[clean_sent(x) for x in sentences]
    
    vectorizer = TfidfVectorizer(ngram_range=ngramRange)
    X = vectorizer.fit_transform(clean_sentences)
    
    df=pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names())
    
    A=makeAdjMatrix(df)
    
    sentence_rankings = pageRank(A)
    
    ranked_sentence_indexes = [item[0] for item in sorted(enumerate(sentence_rankings), key=lambda item: -item[1])]
    selectedSentences = sorted(ranked_sentence_indexes[:topN])
    summary = [clean_sentences[x] for x in selectedSentences]
    return summary

with io.open('blockchain.txt', 'r', encoding="utf-8") as myfile:
    text=myfile.read().replace('\n', ' ')

summary=textRank(text,stopWords=stopwords.words('english'))
for x in summary:
    print (x+".")

summary=textRank(text,stopWords=stopwords.words('english'),ngramRange=(2,3))
for x in summary:
    print (x+".")

