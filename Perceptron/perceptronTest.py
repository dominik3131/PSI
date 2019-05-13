import random
from perceptron import *
number_of_ages = 10
a_of_line = 3.2
b_of_line = 4


def initData(number_of_points):  
	data = [[random.randrange(-50,50 )for i in range(number_of_points)],[random.randrange(-50,50 ) for i in range(number_of_points)]]
	t=[up(i,data[0][i],data[1][i]) for i in range(number_of_points)]
	return data,t
def up(i,x,y):
    if y > x*a_of_line+b_of_line:
        return 1
    else:
        return 0

for i in range(100):
    perc= Perceptron(number_of_ages)
    data,t=initData(1000)
    perc.setData(data,t)
    perc.learn()
    data,t=initData(200)
    perc.setData(data,t)
    perc.test()
