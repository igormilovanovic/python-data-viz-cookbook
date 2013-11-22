# coding: utf-8
from pylab import *

# generate uniform data points
x = 1e6*rand(1000)
y = rand(1000)

figure()

# crate first subplot
subplot(211)
# make scatter plot
scatter(x, y)
xscale('linear')
# limit x axis 
xlim([1e-6, 1e6])

# crate second subplot
subplot(212)
# make scatter plot
scatter(x,y)
# but make x axis logarithmic
xscale('log')
# set same x axis limit 
xlim([1e-6, 1e6])

show()
