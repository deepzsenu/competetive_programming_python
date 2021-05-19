# cook your dish here
n = int(input())
odd = 0
even = 0 


for i in range(1,((n+1)*2)-1):
    if i%2 != 0:
        odd += i
    elif i%2 == 0:
        even += i
        
print(odd,"", even)
