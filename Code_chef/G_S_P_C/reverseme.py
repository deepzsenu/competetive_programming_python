# cook your dish here

def reverse(list):
    s =0 
    e =len(list) -1
    while s<e:
        list[s],list[e] = list[e], list[s]
        
        s = s+1
        e = e-1
    return list
num = int(input())       
l = [int(x) for x in input().split()]
rev_l = reverse(l)
for e in rev_l:
    print(e,end =" ")
print()



