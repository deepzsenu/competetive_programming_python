import math

t = int(input())

for i in range(1, t+1):
  entry = input().split()
  n,m = int(entry[0]), int(entry[1])
  
  print(math.gcd(n,m))
