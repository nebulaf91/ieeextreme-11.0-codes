# simple recursion
f = [0,1,2]
for i in range(3, 22001):
  f.append(f[i-1] + f[i-2])




t = int(input())
for i in range(t):
  s = int(input())
  print(f[s])

