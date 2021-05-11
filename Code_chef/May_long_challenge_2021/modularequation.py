# cook your dish here
def modequ(N,M):
    sets = []
    total = 0
    m = (10**9)+7
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            if ((M%i)%j) == ((M%j)%i):
                total 
            
    print(total)
            
        
def main():
    Testcase = int(input(""))
    while(Testcase>0):
        Entry = input().split()
        N,M = int(Entry[0]), int(Entry[1])
        
        modequ(N,M)
        
        Testcase -= 1
        
if __name__ == "__main__":
    main()
