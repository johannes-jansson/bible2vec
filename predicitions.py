import word2vec
model = word2vec.load('kjv.bin')

# Similar words
# indexes, metrics = model.cosine('face')
# print(model.generate_response(indexes, metrics).tolist())

# Similar Phrases
# indexes, metrics = model.cosine('sherlock_holmes')
# print(model.generate_response(indexes, metrics).tolist())

# Analogies
indexes, metrics = model.analogy(pos=['Jesus', 'man'], neg=['woman'], n=10)
print(model.generate_response(indexes, metrics).tolist())

# Clusters
# clusters = word2vec.load_clusters('cano-clusters.txt')
# print(clusters.get_words_on_cluster(clusters['good'])[:10])

# Analogy including clusters
# clusters = word2vec.load_clusters('cano-clusters.txt')
# model.clusters = clusters
# indexes, metrics = model.analogy(pos=['father', 'woman'], neg=['man'], n=10)
# print(model.generate_response(indexes, metrics).tolist())

