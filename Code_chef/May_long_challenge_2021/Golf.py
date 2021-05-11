# cook your dish here
def golf(n,x,k):
    if x%k == 0 or (n+1-x)%k == 0:
        print("Yes")
        
    else:
        print("NO")
    
    """if n < k:
        print("NO")
    else:
        l = [i for i in range(0,n+2,k)]
        j = l[::-1]
        for w in j:
            l.append(w)
            
        for i in range(n):
            if len(l) < n :
                l = l+l
        if l[n] == x:
            print("YES")
        else:
            print("NO")"""
    
    


def main():
    testcases = int(input())
    while(testcases>0):
        entry = input().split()
        n,x,k = int(entry[0]),int(entry[1]), int(entry[2])
        
        golf(n,x,k)
        
        testcases -= 1
if __name__ =="__main__":
    main()
    
