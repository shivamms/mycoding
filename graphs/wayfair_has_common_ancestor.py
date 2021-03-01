# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

# For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

#              15
#              |
#          14  13
#          |   |
# 1   2    4   12
#  \ /   / | \ /
#   3   5  8  9
#    \ / \     \
#     6   7     11

# parent_child_pairs_1 = [
#     (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
#     (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
#    (12, 9), (15, 13)
# ]

# Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

# Sample input and output:

# has_common_ancestor(parent_child_pairs_1, 3, 8) => false
# has_common_ancestor(parent_child_pairs_1, 5, 8) => true
# has_common_ancestor(parent_child_pairs_1, 6, 8) => true
# has_common_ancestor(parent_child_pairs_1, 6, 9) => true
# has_common_ancestor(parent_child_pairs_1, 1, 3) => false
# has_common_ancestor(parent_child_pairs_1, 3, 1) => false
# has_common_ancestor(parent_child_pairs_1, 7, 11) => true
# has_common_ancestor(parent_child_pairs_1, 6, 5) => true
# has_common_ancestor(parent_child_pairs_1, 5, 6) => true

# Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

#         11
#        /  \
#       10   12
#      /  \
# 1   2    5
#  \ /    / \
#   3    6   7
#    \        \
#     4        8

# parent_child_pairs_2 = [
#     (1, 3), (11, 10), (11, 12), (2, 3), (10, 2),
#     (10, 5), (3, 4), (5, 6), (5, 7), (7, 8),
# ]

# has_common_ancestor(parent_child_pairs_2, 4, 12) => true
# has_common_ancestor(parent_child_pairs_2, 1, 6) => false
# has_common_ancestor(parent_child_pairs_2, 1, 12) => false

# n: number of pairs in the input


# '''

parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
    (15, 13)
]

parent_child_pairs_2 = [
    (1, 3), (11, 10), (11, 12), (2, 3), (10, 2), 
    (10, 5), (3, 4), (5, 6), (5, 7), (7, 8)
]

from collections import defaultdict

def has_common_ancestor(pc,ind1, ind2):
    adjacenyList = defaultdict(list)
    for p in pc:
        adjacenyList[p[1]].append(p[0])
    
    # has_common = False
    
    # def dfs(adjacenyList, ind1, ind2):
    #   if ind1 in adjacenyList.keys():
    #     for i in adjacenyList[ind1]:
    #       dfs(adjacenyList, )
    print(adjacenyList)

