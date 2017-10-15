import numpy as np;

kinds = []
s = int(input())

def p(l, r):
  if(r == 1 or l == r):
    return 1
  return p(l-1, r-1) + p(l-1, r)

# to the 16th layer, sum is beyond 10000 (more than s)
array = np.ones([15,15], dtype=int);
# print(array)

for i in range(0, 15):
  for j in range(0, i):
    if(j != 0):
      array[i][j] = array[i-1][j-1] + array[i-1][j]

# print(array.sum(axis = 1))
# print(array)

for layer in range(15):
  
