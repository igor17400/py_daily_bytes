###############
# Day 11: Bipartite Graph
###############

"""
Goal: Understand an application of Bipartite Graphs - Recommender Systems
"""

import numpy as np

# Define the number of users and items
num_users = 2
num_items = 5

# The dimension of the feature embeddings
# Embeddings are a way to represent objects as lists of numbers
feature_dim = 8

# 1. Construct the bipartite graph as an adjacency matrix A
# -- A is a matrix of shape (num_users, num_items)
# -- An entry A[i, j] = 1 if user i has clicked on item j, 0 otherwise
# -- We'll create a random, sparse matrix to simulate clicks
# -- This matrix A corresponds to the a A ∈ R^|U|x|N|
adjacency_matrix_A = np.random.randint(0, 2, size=(num_users, num_items))

print("--- Recommender System Bipartite Graph ---")
print(f"Adjacency Matrix A (Users x Items):\n{adjacency_matrix_A}\n")
print(f"Shape of A: {adjacency_matrix_A.shape}\n")

# 2. Initialize the node feature matrix for nodes, R_u
# -- R_u is of shape (num_users, feature_dim)
# -- Let's random initialize it as well
user_feature_matrix_R_u = np.random.randn(num_users, feature_dim)

print(f"User Feature Matrix R_u (randomly initialized):\n{user_feature_matrix_R_u}\n")
print(f"Shape of R_u: {user_feature_matrix_R_u.shape}\n")

# 3. Initialize the node feature matrix for new nodes, R_n
# -- R_n is of shape (num_items, feature_dim)
# -- It's initialized with items embeddings.
# -- Let's also use random representation for those items embeddings
# -- This matrix R_n corresponds to the R_n ∈ R^|N|xd.
items_feature_matrix_R_n = np.random.randn(num_items, feature_dim)

print(f"Items Feature Matrix R_n (conceptual items embeddings):\n{items_feature_matrix_R_n}\n")
print(f"Shape of R_n: {items_feature_matrix_R_n.shape}\n")
