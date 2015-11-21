import os
class DataLoader:
    def __init__(self):
        self.src=os.path.dirname(os.path.abspath("__file__"))
        self.root=os.path.abspath(os.path.join(self.src,os.path.pardir))# root path
        self.data=os.path.join(self.root,"data")#data path
        print "data path:",self.data
        self.result=os.path.join(self.root,"result")# /result
        self.train_data={} 
        self.test_data={}

    def read_train(self):
        '''Read from training data'''
        train_file=self.data+"/training_set.tsv"
        with open(train_file) as infile:
            for count,line in enumerate(infile):
                if count>0:
                    id,question,correctAnswer,AnswerA,AnswerB,AnswerC,AnswerD= line.split("\t")
                    self.train_data[id]=[question,correctAnswer,AnswerA,AnswerB,AnswerC,AnswerD]
    
    def read_test(self):
        '''Read from test data'''
        test_file=self.data+"/validation_set.tsv"
        with open(test_file) as infile:
            for count,line in enumerate(infile):
                if count>0:
                    id,question,AnswerA,AnswerB,AnswerC,AnswerD= line.split("\t")
                    self.test_data[id]=[question,AnswerA,AnswerB,AnswerC,AnswerD]

if __name__=="__main__":
    dl=DataLoader()

