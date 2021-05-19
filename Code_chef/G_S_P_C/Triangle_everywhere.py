# cook your dish here


entry = input().split()

a,b,c = [int(i) for i in entry]
if a== 0 or b== 0 or c== 0 :
    print(-1)
elif (a == b) and (b==c):
    print(1)
    
elif ((a == b) and (a+b)>c) or ((b == c) and (c+b)>a) or ((a == c) and (a+c)>b):
    print(2)
    
elif ((c+b > a) and (abs(c-b)< a)) or ((a+b > c) and (abs(a-b)< c))or ((c+a > b) and (abs(c-a)< b)) :
    print(3)
else:
    print(-1)
