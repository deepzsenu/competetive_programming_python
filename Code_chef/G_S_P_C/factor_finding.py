# cook your dish here
num =  int(input())
count = 0 
l = []
for i in range(1,num+1):
    if num%i == 0:
        count +=1
        l.append(i)
print(count)
for e in l:
    print(e,end=" ")
print()
