import numpy

#input a1 ~ c2 into a list 
inp =[int(float(x)*10e14) for x in input("""A linear equation looks like\n
a1*x + b1*y = c1\n
a2*x + b2*y = c2\n
please input(a1 b1 c1 a2 b2 c2) : """).split()]

#put a1 ~ c2 into a numpy array
delta = numpy.array([[inp[0],inp[1]],[inp[3],inp[4]]])
delta_x = numpy.array([[inp[2],inp[1]],[inp[5],inp[4]]])
delta_y = numpy.array([[inp[0],inp[2]],[inp[3],inp[5]]])

#calculate the determination of the array
delta_sum = numpy.linalg.det(delta)
deltax_sum = numpy.linalg.det(delta_x)
deltay_sum = numpy.linalg.det(delta_y)

if delta_sum: #if delta == 0 will go to else
    x = deltax_sum / delta_sum
    y = deltay_sum / delta_sum
    print(f'the answer of the linear equations is:\nx = {x}\ny = {y}')
else: 
    if (deltax_sum**2+deltay_sum**2) == 0:
        #if true, meaning both of above equals to 0
        print("infinitely solution to this equation")
    else:
        print("no solution to this equation")

