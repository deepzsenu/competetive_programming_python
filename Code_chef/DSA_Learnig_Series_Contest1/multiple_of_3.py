t = int(input())
for _ in range(t):
    k,d0,d1 = map(int,input().split())
    count=2
    s=d0+d1
    lastdigit =(d0+d1)%10
    k-=2
    while k>0:
        if lastdigit==2:
            sets = (k//4)
            k-=sets*4
            s+=sets*20
            if k==1:
                s+=2
            elif k==2:
                s+=6
            elif k==3:
                s+=14
            break
        elif lastdigit==0:
            break
        else:
            s+=lastdigit
            lastdigit = (lastdigit*2)%10
            k-=1
    if s%3:
        print("NO")
    else:
        print("YES")

'''# cook your dish here
def div_three(k, d , e):
    s = str(d)+str(e)
    
    sum = d+e
    for i in range(2,k):
        s = s+(str(sum%10))
        sum = sum + int(s[i])
    #print(s)   
    if int(s) %3 == 0:
        
        print("YES")
    else:
        print("NO")

# int the above solution the time limit exceed for large numbers

def main():
    T = int(input())
    while(T>0):
        entry = input().split()
        k, d1, d2 = int(entry[0]), int(entry[1]), int(entry[2])
        
        div_three(k, d1, d2)
        
        T -= 1
        
if __name__ == '__main__':
    main()
    
    
    '''
