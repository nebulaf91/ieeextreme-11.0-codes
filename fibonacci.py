f = [1,1,2]
for i in range(3, 60):
  f.append((f[i-1] + f[i-2]) % 10)

print(f[0:60])

t = int(input())
for i in range(t):
  s = int(input()) % 60
  print(f[s])