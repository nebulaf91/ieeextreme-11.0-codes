# time limit exceeded

import numpy as np

dim = int(input())
shape = list(map(int,input().split()))
elements = list(map(int,input().split()))
# print(elements)
array = np.array(elements).reshape(shape)
# print(array)
query = int(input())
for i in range(query):
  start = list(map(int,input().split()))
  # print(start)
  end = list(map(int,input().split()))
  # print(end)
  sub_array = array
  for j in range(dim):
    # indices.append(range(start[j]-1, end[j]))
    sub_array = sub_array.take(range(start[j]-1, end[j]), axis = j)
    # print(array)
  print(sub_array.sum())
