# -*- coding: utf-8 -*-
import enchant  
import nltk
import os
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords

class CleanDoc:
    def __init__(self,in_dir,out_dir):
        self.in_dir=in_dir;
        self.out_dir=out_dir
        self.st = LancasterStemmer()
        self.word_checker=enchant.Dict("en_US")
        self.stops = set(stopwords.words('english'))
        
    def clean(self,path,target):
        with open(path) as fin,open(target,'wb') as fout:
            for line in fin:
                tokens=self.getTerms(line)
                if tokens!=[]:
                    fout.write(" ".join(tokens)+'\n')
    def processDir(self):
        files=os.listdir(self.in_dir)
        for fname in files:
            self.clean(self.in_dir+fname,self.out_dir+fname)
            
    def getTerms(self,sentences):
        tokens = nltk.word_tokenize(sentences.decode('utf8'))
        words = [self.st.stem(w.lower()).encode('utf8') for w in tokens if w.isalnum() and self.word_checker.check(w) and w.lower() not in self.stops ]
        return words

if __name__=='__main__':
    cleaner=CleanDoc('/Users/jinfenglin/Documents/workspace/AI/LittleAllen/data/raw_txt/','/Users/jinfenglin/Documents/workspace/AI/LittleAllen/data/clean_txt/')
    cleaner.processDir()
    print "DONE!"

