# cook your dish here

item = input().split()

pen, pencil , p_cost, pencil_cost = int(item[0]), int(item[1]), int(item[2]), int(item[3])
cost  = (pen*p_cost)+(pencil*pencil_cost)
print(cost)
