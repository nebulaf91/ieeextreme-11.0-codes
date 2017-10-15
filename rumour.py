q = int(input())





for i in range(q):
  count = 0
  a, b = map(int,input().split())
  while(a != b):
    if(a > b):
      a = a>>2
      count = count + 1
    if(a < b):
      b = b>>2
      count = count + 1

  print(count)