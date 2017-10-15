q = int(input())

def layer(n):
  count = 0
  while(n!=0):
    n = n >> 1
    count = count +1
  return count



for i in range(q):
  count = 0
  a, b = map(int,input().split())
  root = a ^ b
  la = layer(a)
  lb = layer(b)
  lr = layer(root)
  print(la, lb, lr)
  print(abs(la-lb) + lr - 1)