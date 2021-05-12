T = int(input())
while(T>0):
  num = int(input())
  sum = 0
  for i in range(1,num):
    
    if num%i == 0:
      #print(i)
      sum +=i
  if sum == num:
    print("true")
  else:
    print("false")
   
  T -= 1 
