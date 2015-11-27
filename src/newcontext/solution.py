import enchant  
import nltk
import os
from gensim.models.doc2vec import Doc2Vec
from nltk.stem.lancaster import LancasterStemmer

class Solution:
    def __init__(self):
        self.model=Doc2Vec.load('./model.d2v')
        self.st = LancasterStemmer()

        
    def getTerms(self,sentences):
        self.word_checker=enchant.Dict("en_US")
        tokens = nltk.word_tokenize(sentences.decode('utf8'))
        words = [self.st.stem(w.lower()).encode('utf8') for w in tokens if w.isalnum() and self.word_checker.check(w) and self.st.stem(w.lower()) in self.model.vocab]
        return words

    def generate(self):
        data_dir="/Users/jinfenglin/Documents/workspace/AI/LittleAllen/data/"
        result_dir="/Users/jinfenglin/Documents/workspace/AI/LittleAllen/result/"
        model=self.model
        with open(data_dir+"validation_set.tsv") as test, open(result_dir+"vec_submit.csv",'w') as res:
            for count,line in enumerate(test):
                if count==0:
                    res.write('id,correctAnswer\n')
                    continue

                items=line.split('\t')
                id=items[0]
                print id
                question=self.getTerms(items[1])
                a=self.getTerms(items[2])
                b=self.getTerms(items[3])
                c=self.getTerms(items[4])
                d=self.getTerms(items[5])
                print a,b,c,d
                if a==[]:
                    q_a=0
                else:
                    q_a=model.n_similarity(question,a)
                if b==[]:
                    q_b=0
                else:
                    q_b=model.n_similarity(question,b)
                if c==[]:
                    q_c=0
                else:
                    q_c=model.n_similarity(question,c)
                if d==[]:
                    q_d=0
                else:
                    q_d=model.n_similarity(question,d)
                print q_a,q_b,q_c,q_d
                max_val=q_a
                answer='A'
                if q_b> max_val:
                    max_val=q_b
                    answer='B'
                if q_c > max_val:
                    max_val=q_c
                    answer='C'
                if q_d > max_val:
                    answer='D'
                res.write(id+','+answer+'\n')

if __name__=="__main__":
    sol=Solution()
    sol.generate()
    print "DONE"
