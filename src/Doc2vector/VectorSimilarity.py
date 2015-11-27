from gensim.models import doc2vec
import re
import paramiko
import string
from nltk.corpus import stopwords
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
        def __iter__(self):
            for fname in os.listdir(self.dirname):
                if 'txt' in fname:
                    for line in open(os.path.join(self.dirname, fname)):
                        yield line.split()
if __name__=="__main__":
    '''#client = paramiko.SSHClient()
    #client.load_system_host_keys()
    #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #client.connect('diadem.cs.brandeis.edu',username='ljf1992',password='!Aa6813896')
    #ftp=client.open_sftp()
    #sentence=[]
    for file in ftp.listdir('/common/public/AI_DATA/'):
        if 'science_text_books.txt' in file:
            stdin,stdout,stderr = client.exec_command("cat /common/public/AI_DATA/"+file)
            text=stdout.readlines()
            for line in text:
                tmp=[]
                #for word in re.findall(r"[\w']+", line):
                for word in re.findall(r"[a-zA-Z]+",line):
                    word= word.lower()
                    if word not in stopwords.words('english') and len(word)>=2:
                        tmp.append(word)

                sentence.append(tmp)
            #f=ftp.file('/common/public/AI_DATA/'+file)
            #for line in f.read():
            #sentence.append(line)
    print sentence'''
    '''#remote_file = ftp.open('/common/public/AI_DATA/GoogleNews-vectors-negative300.bin')
    #documents = doc2vec.TaggedLineDocument(remote_file)
    #model=doc2vec.Doc2Vec(documents)
    #model=doc2vec.Doc2Vec.load_word2vec_format(remote_file,binary=True)

    #model = gensim.models.Word2Vec(sentence)
    model.save('./sci.md')
    ftp.close()'''
    data_dir="/Users/jinfenglin/Documents/workspace/AI/LittleAllen/data/"
    result_dir="/Users/jinfenglin/Documents/workspace/AI/LittleAllen/result/"
    #model=doc2vec.Doc2Vec.load_word2vec_format(data_dir+"GoogleNews-vectors-negative300.bin",binary=True)
    documents=doc2vec.TaggedLineDocument(data_dir+'science_text_books.txt')
    model=doc2vec.Doc2Vec(documents)
    with open(data_dir+"validation_set.tsv") as test, open(result_dir+"vec_submit.csv",'w') as res:
        for count,line in enumerate(test):
            if count==0:
                res.write("id,correctAnswer\n")
            else:
                items=line.split('\t')
                id=items[0]
                print id
                question=[token.strip(' .\t\n\r') for token in items[1].split(' ') if token.strip(' .\t\n\r') in model.vocab]
                a= [token.strip(' .\t\n\r') for token in items[2].split(' ') if token.strip(' .\t\n\r') in model.vocab]
                b= [token.strip(' .\t\n\r') for token in items[3].split(' ') if token.strip(' .\t\n\r') in model.vocab]
                c= [token.strip(' .\t\n\r') for token in items[4].split(' ') if token.strip(' .\t\n\r') in model.vocab]
                d= [token.strip(' .\t\n\r') for token in items[5].split(' ') if token.strip(' .\t\n\r') in model.vocab]
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

    print "DONE!" 
    


