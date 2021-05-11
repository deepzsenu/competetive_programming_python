# cook your dish here
import math
def iss(n):
    res = 0
    m = (10**9)+7
    
    for i in range(1, ((2*n)+1)):
        res += math.gcd(n+(i**2), n+((i+1)**2) )
        #res += res
        
    print(res%m)

t = int(input(""))
for i in range(t):
    entry = int(input(""))
            
    iss(entry)
            
