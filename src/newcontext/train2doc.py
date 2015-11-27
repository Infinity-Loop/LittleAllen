if __name__=="__main__":
    with open("/Users/jinfenglin/Documents/workspace/AI/LittleAllen/data/training_set.tsv") as fin,open("/Users/jinfenglin/Documents/workspace/AI/LittleAllen/data/raw_txt/training_set.tsv",'wb') as fout:
        for line in fin:
            items=line.split('\t')
            question=items[1]
            correct=items[2]
            a=items[3]
            b=items[4]
            c=items[5]
            d=items[6]
            if correct=='A':
                extra=a
            elif correct=='B':
                extra=b
            elif correct=='C':
                extra=c
            else:
                extra=d
            fout.write(question+" "+extra.strip()+"\n")

