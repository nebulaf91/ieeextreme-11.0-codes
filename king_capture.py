import numpy as np;

v, e= map(int,input().split())
# connection = np.zeros([v, v], dtype = bool)
connection = np.zeros([v, v], dtype = int)
distance = np.zeros([v], dtype = int)
for i in range(v):
  distance[i] = -1;

for j in range(e):
  v1, v2 = map(int,input().split())
  # connection[v1 -1, v2 -1] = True
  # connection[v2 -1, v1 -1] = True
  connection[v1 -1, v2 -1] = 1
  connection[v2 -1, v1 -1] = 1

count = 1;
distance[0] = 0
# print(distance)
#distance based on vertex 0
for i in range(0, v):
  indices = np.argwhere(distance == i)
  for index in indices:
    # print(index)
    for j in range(0, v):
      if connection[j, index] and distance[j] == -1:
        distance[j] = count
  count = count + 1
  # print(distance)



  
    


