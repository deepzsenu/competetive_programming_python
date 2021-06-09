def coco(xa, xb, Xa, Xb):
    mm = Xa//xa
    m = Xb//xb
    total = mm+m
    return total
    
def main():
    t = int(input())
    while t>0 :
        n = input().split()
        xa,xb,Xa, Xb = int(n[0]),int(n[1]),int(n[2]),int(n[3])
        
        print(coco(xa, xb, Xa, Xb))
        
        t -=1
        
if __name__ == "__main__":
    main()
