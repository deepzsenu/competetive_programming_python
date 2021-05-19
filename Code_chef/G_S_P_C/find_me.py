# cook your dish here
entry = input().split()
ran, num = int(entry[0]), int(entry[1])

l = input().split()
for i in l:
    if int(i) == num:
        print(1)
        break
else:
    print(-1)
        
