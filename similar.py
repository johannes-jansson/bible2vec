import word2vec
import sys
model = word2vec.load('kjv.bin')
indexes, metrics = model.cosine(sys.argv[1])
print('')
for i in range(model.generate_response(indexes, metrics).size):
    print(
        model.generate_response(indexes, metrics)[:][i][0] +
        ' (' +
        str(model.generate_response(indexes, metrics)[:][i][1]) +
        ')'
    )
print('\n\n')
