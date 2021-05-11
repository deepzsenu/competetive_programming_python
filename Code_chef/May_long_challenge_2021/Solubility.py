# cook your dish here
def solutbility(x,a,b):
    solutbility =(a +(100 - x )*b)*10
    print(solutbility)
    
def main():
    testcase =  int(input(""))
    while (testcase>0):
        
        entry = input().split()
        x,a,b = int(entry[0]),int(entry[1]),int(entry[2])
        
        solutbility(x,a,b)
        
        testcase -=1
        
if __name__ == "__main__":
    main()
    #(x,a,b)

        
        
