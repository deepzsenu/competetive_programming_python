# cook your dish here
def xor(p ,n, m):
    res = 1 
    
    """
    for i in range(0,2**n):
        i = i%m
        if i^(i+1)==(i+2)^(i+3):
            res = res+1
    
    return res"""
            
    p = p%m
    
    if p==0:
        print(0)
    while(n>0):
        if (n&1):
            res = (res * p ) % m
        n = n>>1
        p = (p*p)%m
    print(res)
    
m = (10**9)+7
m = 1000000007

testcases =  int(input())
for i in range(testcases):
    entry = int(input())
    xor(2,(entry-1),m)
