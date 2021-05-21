

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
'''
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
