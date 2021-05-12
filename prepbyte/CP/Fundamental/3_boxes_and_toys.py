#def boxtoy(t ,c):
  
  
  

N = int(input())
boxes = 0 
while(N>0):
  toys,cap = [int(x) for x in input().split()]
  #boxtoy(toys,cap)
  
  if (cap - toys)>= 2:
    boxes += 1
  
  N -=1
print(boxes)
  
  
