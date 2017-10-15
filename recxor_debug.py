from math import ceil as ceil


q= int(input())

def xor_1_to_n(n):
  res = n % 4
  if res == 0:
    return n
  if res==1:
    return 1
  if res==2:
    return n+1
  if res==3:
    return 0

for i in range(q):
  l, h, n, d1, d2 = map(int,input().split())
  out_xor = xor_1_to_n(l*h+n-1) ^ xor_1_to_n(n-1)

  print("out_xor:")
  print(l*h+1-n)
  print(out_xor)

  d1_row = ceil((d1 -n +1) / l)
  d1_col = d1 -n +1 - (d1_row - 1) * l
  d2_row = ceil((d2 -n +1) / l)
  d2_col =  d2 -n +1 - (d2_row - 1) * l

  print("d1_row, d1_col, d2_row, d2_col")
  print(d1_row, d1_col, d2_row, d2_col)

  l_in = abs(d2_col - d1_col) + 1
  h_in = abs(d2_row - d1_row) + 1
  if(d1_col < d2_col):
    upper_left = d1
  else:
    upper_left = d1 - l_in + 1
    
  print("upper_left")
  print(upper_left)
  print("l_in, h_in")
  print(l_in, h_in)

  in_xor = xor_1_to_n(upper_left + l_in -1) ^ xor_1_to_n(upper_left -1) 
  left = upper_left
  for j in range(1, h_in):    # find the left edge, and the right edge. key
    left = left + l
    in_xor ^= xor_1_to_n(left + l_in -1) ^ xor_1_to_n(left -1) 

    print("left")
    print(left)
    print("right")
    print(left + l_in -1)
  print("in_xor")
  print(in_xor)

  print(out_xor ^ in_xor)
