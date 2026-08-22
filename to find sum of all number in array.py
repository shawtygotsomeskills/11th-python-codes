import numpy
import numpy as np
ar = np.array([250,300,350,400,450,500])
sum = 0
for i in ar:
    sum=sum+i
    print("total sales is" ,sum)
    av = sum/7
    print("average is" , av)
