import word2vec

# Create phrase file
word2vec.word2phrase('material/kjv.txt', 'kjv-phrases', verbose=True)

# Do training
word2vec.word2vec('kjv-phrases', 'kjv.bin', size=100, verbose=True)

# Do clustering
word2vec.word2clusters('material/kjv.txt',
                       'kjv-clusters.txt',
                       100,
                       verbose=True)
