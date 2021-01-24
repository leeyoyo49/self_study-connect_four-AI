import numpy as np
n = int(input("enter how many unknown numbers to solve : "))
input_list = []
all_param = []
for x in range(n):
    temp = [float(y) for y in input(f"input the {x+1} equation's parameters (eg. a1 b1 c1) : ").split()]
    if x:
        delta = np.append(delta, [temp[:n]], axis = 0)
    else:
        delta = np.array([temp[:n]])
    input_list.append(temp)
delta_sum = np.linalg.det(delta) 
for x in range(n):
    for y in range(n):
        if x:
            delta[y][x-1] = input_list[y][x-1]
        delta[y][x] = input_list[y][n]  
    deltax_sum = np.linalg.det(delta)
    all_param.append(deltax_sum / delta_sum)
temp = 0
if delta_sum: #if delta == 0 will go to else
    for y in range(n):
        print(f'the {y+1} parameter of the linear equations is : {all_param[y]}')
else:
    for y in range(n):
        temp += all_param[y]**2
    if temp == 0:
        #if true, meaning both of above equals to 0
        print("infinitely solution to this equation")
    else:
        print("no solution to this equation")
