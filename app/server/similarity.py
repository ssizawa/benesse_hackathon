# import gensim
# import numpy as np

# word2vec = gensim.models.KeyedVectors.load_word2vec_format('./static/word2vec/GoogleNews-vectors-negative300.bin', binary=True)
# model = gensim.models.KeyedVectors.load_word2vec_format('./static/word2vec/ja/ja.bin', binary=False, encoding="utf8",unicode_errors='ignore')

# def get_vec(word):
#     return word2vec[word]

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

# Define a function to calculate the magnitude (norm or length) of a vector.
def magnitude(vector):
    return sum(x**2 for x in vector) ** 0.5

# Define a function to calculate the cosine similarity between two vectors
# using the dot product and magnitudes.
def cosine_similarity(a, b):
    dot_prod = dot_product(a, b)
    mag_a = magnitude(a)+1e-6
    mag_b = magnitude(b)+1e-6
    similarity = dot_prod / (mag_a * mag_b)
    return similarity

import numpy as np

def euclidian(a, b):
    # 2つの点p, qの座標位置の配列を定義
    p = np.array(a)
    q = np.array(b)
    # 2点間のユークリッド距離を計算する
    dist = np.linalg.norm(p - q)
    return dist