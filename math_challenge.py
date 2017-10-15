from scipy.special import comb
n = int(input())
for i in range(n):
  base, comb1, comb2 = map(int,input().split())
  print(pow(base, comb(comb1, comb2))%1000000007)
