from minorminer import find_embedding  # There's no reason to reinvent the wheel if there's already a library

# A triangle is a minor of a square.
triangle = [(0, 1), (1, 2), (2, 0)]
#square = [(0, 1), (1, 2), (2, 3), (3, 0)]
square = [(0, 1), (0, 2), (1, 3), (2, 3)]

# Find an assignment of sets of square variables to the triangle variables
embedding = find_embedding(triangle, square)
print(len(embedding))  # 3, one set for each variable in the triangle
print(embedding)
# We don't know which variables will be assigned where, here are a
# couple possible outputs:
# [[0, 1], [2], [3]]
# [[3], [1, 0], [2]]

print(type(triangle))

print(triangle[0])