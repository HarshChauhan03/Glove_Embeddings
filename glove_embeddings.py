# Day 09 - Word Embeddings using Pretrained GloVe

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load GloVe embeddings file
# Download from: https://nlp.stanford.edu/projects/glove/
# Use file: glove.6B.50d.txt

embeddings_index = {}

with open("glove.6B.50d.txt", encoding="utf8") as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], dtype="float32")
        embeddings_index[word] = vector

print("Total words loaded:", len(embeddings_index))

# Get vector for a word
word = "king"
print(f"\nVector for '{word}':\n", embeddings_index[word])

# Function to compute similarity
def word_similarity(w1, w2):
    vec1 = embeddings_index[w1].reshape(1, -1)
    vec2 = embeddings_index[w2].reshape(1, -1)
    return cosine_similarity(vec1, vec2)[0][0]

# Similarity examples
print("\nSimilarity between 'king' and 'queen':", word_similarity("king", "queen"))
print("Similarity between 'king' and 'apple':", word_similarity("king", "apple"))

# Word analogy example: king - man + woman ≈ queen
result_vector = embeddings_index["king"] - embeddings_index["man"] + embeddings_index["woman"]

best_word = ""
max_sim = -1

for w, vec in embeddings_index.items():
    sim = cosine_similarity(result_vector.reshape(1, -1), vec.reshape(1, -1))[0][0]
    if sim > max_sim and w not in ["king", "man", "woman"]:
        max_sim = sim
        best_word = w

print("\nAnalogy Result (king - man + woman):", best_word)
