class cleanText:
    def clean(self,file_path):
        new_file=file_path+'_new'
        with open(file_path):
            for word in re.findall(r"[a-zA-Z]+",line):
            word= word.lower()
            if word not in stopwords.words('english') and len(word)>=2:


        

if __name__=="__main__":

