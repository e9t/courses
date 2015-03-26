#! /usr/bin/python3
# -*- coding: utf-8 -*-

from glob import glob
import json

def get_content(filename):
    with open(filename, 'r') as f:
        return json.load(f)['content']

'''
datadir = '/Users/e9t/data/dada/tmp/data/naver-news/texts'  # News from 2015-02-12

filenames = glob('%s/*/*/*/*/*.json' % datadir)
print(len(filenames))   # nfiles = 19885

print(1)
docs = [get_content(f) for f in filenames]

print(2)
from konlpy.tag import Twitter; t = Twitter()
pos = lambda d: ['/'.join(p) for p in t.pos(d, stem=True, norm=True)]
texts = [pos(doc) for doc in docs]

print(3)
from gensim import corpora
dictionary = corpora.Dictionary(texts)
dictionary.save('ko.dict')  # save dictionary to file for future use

print(4)
from gensim import models
tf = [dictionary.doc2bow(text) for text in texts]
tfidf_model = models.TfidfModel(tf)
tfidf = tfidf_model[tf]
corpora.MmCorpus.serialize('ko.mm', tfidf) # save corpus to file for future use
# 4'42"
'''

from gensim import corpora, models
dictionary = corpora.Dictionary.load('ko.dict')
tfidf = corpora.MmCorpus.load('ko.mm')
ntopics, nwords = 5, 5
lsi = models.lsimodel.LsiModel(tfidf, id2word=dictionary, num_topics=ntopics)
print(lsi.print_topics(num_topics=ntopics, num_words=nwords))
