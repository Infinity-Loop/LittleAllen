import gensim
if __name__=="__main__":
    model= gensim.models.Doc2Vec.load("./sci.md")
    print model.most_similar(positive=['woman', 'king'], negative=['man'])
    #for word in model.vocab:
    #    print word
