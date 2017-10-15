# not enough time. use simple greedy to try luck

import numpy as np
t = int(input())

for tt in range(t):
  out = 0
  c, n = map(int, input().split())
  weights = np.zeros(n, dtype=int)
  power = np.zeros(n, dtype=int)
  for i in range(n):
    weights[i], power[i] = map(int, input().split())
  # print(power)
  while(power.sum() != 0):   
    p = np.argmax(power)
    # print(power)
    # print("p")
    # print(p)
    # print(weights[p])
    if(weights[p] <= c):
      # print("c")
      # print(c)
      c = c - weights[p]
      out += power[p]
    power[p] = 0
  print(out)


