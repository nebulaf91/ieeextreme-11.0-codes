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
  indices = []
  for j in range(dim):
    indices.append(slice(start[j]-1, end[j]))
  # print(indices)
  # sub_array = array.take(indices)
  # print(sub_array)
  print(array[indices].sum())
