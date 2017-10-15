import numpy as np

n, m = map(int,input().split())
connection = np.zeros([n,n], dtype = bool)
# output = []
for j in range(m):
  city1, city2 = map(int,input().split())
  connection[city1 -1, city2 -1] = True
  connection[city2 -1, city1 -1] = True



degrees = connection.sum(dtype = int, axis = 0)
# print("degrees:")
# print(degrees)
while 1 in degrees:
  end = np.argwhere(degrees==1)    #end is short for endian
  connection[end] = False
  connection[:, end] = False
  degrees = connection.sum(dtype = int, axis = 0)

# for i in range(len(degrees)):
#   if(degrees[i]==0):
#     print(i+1)

# print(connection)
# print(degrees)
# print(connection)
# print(connection.dtype)

for i in range(degrees.size):
  if degrees[i]==0:
    print(i+1)




  
  
