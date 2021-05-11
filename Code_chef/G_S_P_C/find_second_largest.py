# cook your dish here
l = []
for i in range(3):
    num = int(input())
    l.append(num)
    
def seclargest(l):
    if len(l)<= 1:
        return None
    lar = l[0]
    slar = None
    
    for x in l[1:]:
        if x >lar:
            slar = lar
            lar = x
        elif x!= lar:
            if slar == None or slar < x:
                slar = x
                
    return slar
    
print(seclargest(l))
    
