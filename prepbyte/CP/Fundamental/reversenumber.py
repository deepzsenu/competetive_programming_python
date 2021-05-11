num = int(input(""))
r_num = 0

while(num>0):
  rem = num%10
  r_num = (r_num*10)+rem
  num = num//10
  
print(r_num)
