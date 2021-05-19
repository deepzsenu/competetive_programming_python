# cook your dish here
n = input().split()
s , e = int(n[0]), int(n[1])
l = []
for i in range(s, e+1):
    if i%2!=0:
        l.append(i)
        
for e in l:
    print(e,end=" ")
print()

