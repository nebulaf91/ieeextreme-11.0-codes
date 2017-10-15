import numpy as np

n, m = map(int,input().split())
dict = {}
dict_inverse = {}
dist_mat = np.full([n, n], 10000000, dtype=int)
#dist_count < 10000000, means visited
dist_count = np.full([n], 10000000, dtype=int)   
 
route = []


for i in range(n):
  id = int(input())
  dict[id] = i
  dict_inverse[i] = id

# print(dict)

for j in range(m):
  id1, id2, d = map(int,input().split())
  dist_mat[dict[id1]][dict[id2]] = dist_mat[dict[id2]][dict[id1]] = d
# print(dist_mat)

start = dict[min(dict.keys())]
end = dict[max(dict.keys())]

now = start
dist_count[start] = 0
print(dist_count)

# while dist_count[end] == 10000000:
temp = np.full([n, n], 10000000, dtype=int)    
indices = np.argwhere(dist_count < 10000000)
print(dist_count)
print(indices)
for index in indices:
  connected_points = np.argwhere(dist_mat[index] < 10000000)
  # print(index)
  # print(dist_mat[index])
  print(connected_points)
  # print(temp.shape)
  # print(dist_count.shape)
  # print(dist_mat.shape)
  for connected_point in connected_points:
    temp[index][connected_point] = dist_count[index] + dist_mat[connected_point][index]
# print(dist_count)
# print(temp.argmin() % n)
dist_count[temp.argmin() % n] = np.min(temp)
# print(dist_count)
# print(temp)

    

# route.append(dict_inverse[now])

# print(route)



  # print("now")
  # print(now)
  # route.append(dict_inverse[now])
  # indices = np.argwhere(dist_mat[now] < 10000000)
  # print("indices")
  # print(indices)
  # for index in indices:
  #   if dist_mat[now][index] + dist_count[now] < dist_count[index]:
  #     dist_count[index] = dist_mat[now][index] + dist_count[now]
  # print("dist_count")
  # print(dist_count)
  # temp = dist_count
  # temp[now] += 10000000
  # now = temp.argmin()