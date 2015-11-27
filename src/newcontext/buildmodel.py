from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec
from random import shuffle
import os
import nltk
import numpy

class PackSource:
    '''collect file in dir into source format'''
    def __init__(self,dir_path):
        file_names=os.listdir(dir_path)
        self.dic={}
        for fname in file_names:
            prefix=fname.replace('.','_')
            path=dir_path+fname
            self.dic[path]=prefix
    def getSource(self):
        return self.dic

class LabeledLineSentence(object):
    def __init__(self, sources):
        self.sources = sources
        flipped = {}
        # make sure that keys are unique
        for key, value in sources.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                raise Exception('Non-unique prefix encountered')
    
    def __iter__(self):
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    yield LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no])
    
    def to_array(self):
        self.sentences = []
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    self.sentences.append(LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no]))
        return self.sentences
    
    def sentences_perm(self):
        print self.sentences
        return numpy.random.permutation(self.sentences)

if __name__=="__main__":
    #sources = {'test-neg.txt':'TEST_NEG', 'test-pos.txt':'TEST_POS', 'train-neg.txt':'TRAIN_NEG', 'train-pos.txt':'TRAIN_POS', 'train-unsup.txt':'TRAIN_UNS'}
    pk=PackSource("/Users/jinfenglin/Documents/workspace/AI/LittleAllen/data/clean_txt/")
    sources=pk.getSource()
    print sources
    sentences = LabeledLineSentence(sources)
    model = Doc2Vec(min_count=1, window=10, size=300, sample=1e-4, negative=5)
    sentences_list=sentences.to_array()
    model.build_vocab(sentences_list)
    Idx=range(len(sentences_list))
    for epoch in range(20):
        print epoch
        shuffle(Idx)
        perm_sentences = [sentences_list[i] for i in Idx]
        model.train(perm_sentences)
        #model.train(sentences.sentences_perm())
    model.save("./model.d2v")
