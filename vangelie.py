import numpy as np

t = int(input())
for i in range(t):
  v, e = map(int,input().split())
  # connection = np.zeros([v * v], dtype=bool)
  connection = np.zeros([v, v], dtype=int)
  # print(connection)
  edges = list(map(int,input().split()))
  # print(edges)
  for j in range(0, e):
    # print(j)
    if(edges[2 * j] == edges[2 * j+1]):
        connection[edges[2 * j]][edges[2 * j+1]] = 2
    else:
      connection[edges[2 * j]][edges[2 * j+1]] = connection[edges[2 * j+1]][edges[2 * j]] = 1
  # print(connection)
  degrees = connection.sum(dtype = int, axis = 0)
  while 1 in degrees:
    end = np.argwhere(degrees==1)
    connection[end] = False
    connection[:, end] = False
    degrees = connection.sum(dtype = int, axis = 0)

  if degrees.sum():
    print('1')
  else:
    print('0')
