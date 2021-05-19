# cook your dish here

n = int(input())

for i in range(1, ((n)*5), 5):
    if (i-1)%10==0:
        print(i , i+1, i+2, i+3, i+4)
        
    else:
        print(i+4, i+3, i+2, i+1, i)
        
