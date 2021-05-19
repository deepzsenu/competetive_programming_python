entry = input().split()

a, b, c = int(entry[0]), int(entry[1]), int(entry[2])
# cook your dish here
if a+b+c == 180 and a!=0 and b!=0 and c!=0:
    print("YES")
else:
    print("NO")
