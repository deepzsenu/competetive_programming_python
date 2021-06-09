def bell(D,d,P,Q):
    x = D//d
    if x%2==0:
        c = d*((x//2)*(2*P+(x-1)*Q))
        c += (D%d)*(P+x*Q)
    else:
        c = d*(x*(P+((x-1)//2)*Q))
        c+= (D%d)*(P+x*Q)
        
    return c
def main():
    t = int(input())
    
    while t>0:
        n = input().split()
        D,d,P,Q = int(n[0]), int(n[1]),int(n[2]),int(n[3])
        
        print(bell(D,d,P,Q))
        
        t -=1
        
if __name__ == "__main__":
    main()
