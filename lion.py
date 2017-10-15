import numpy as np;

n, m, k = map(int, input().split())

number = np.zeros(k, dtype = int)
dict = {}
for i in range(k):
  dict[i] = list(map(int, input().split()))

# print(dict[0])
# print(dict[3])
# print(dict[0][0])



# print(dict)
for i in range(k):
  for j in range(k):
    # print(i)
    # print(j)
    if(i==j):
      continue;
    if((abs(dict[i][0] - dict[j][0]) + abs(dict[i][1] - dict[j][1])) <= dict[j][2]):
      number[i] = number[i] + 1

lion = np.argmax(number)
print(str(lion+1) + ' ' + str(number[lion]) )
