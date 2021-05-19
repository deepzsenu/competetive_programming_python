# cook your dish here

def rev_num(num):
    st = ''
    for i in range(len(num),0,-1):
        st = st+num[i-1]
        
    print(int(st))
        
    
    
def main():
    T = int(input())
    while(T>0):
        num = int(input())
        
        num = str(num)
        
        rev_num(num)
        T-= 1


if __name__ == "__main__":
    main()
