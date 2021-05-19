# cook your dish here

entry = input().split()

a,b,c = [int(i) for i in entry]

if (a+b >c) and (abs(a-b)<c):
    print("YES")
    
elif (a+c > b) and (abs(a-c)<b):
    print("YES")
    
elif (c+b > a) and (abs(c-b)< a):
    print("YES")
else:
    print("NO")

