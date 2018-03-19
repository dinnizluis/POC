#%pylab inline 
from pylab import *
import matplotlib.pyplot as plt 

x = linspace(0, 5, 10)
y =x ** 2

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()