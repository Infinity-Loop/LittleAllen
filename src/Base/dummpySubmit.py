from dataloader import DataLoader
import random
class dummy(DataLoader):
    def __init__(self):
        DataLoader.__init__(self)
        self.read_train()
        self.read_test()
    def generate(self):
        with open(self.result+'/dummy.csv',"w") as outfile:
            outfile.write('id,correctAnswer\n')
            for (key,value) in self.test_data.items():
                count=random.randint(1,4)

                if count==1:
                    choice='A'
                elif count==2:
                    choice='B'
                elif count==3:
                    choice='C'
                else:
                    choice='D'
                        
                outfile.write(key+','+choice+'\n')
        
if __name__=="__main__":
    dm=dummy()
    dm.generate()
