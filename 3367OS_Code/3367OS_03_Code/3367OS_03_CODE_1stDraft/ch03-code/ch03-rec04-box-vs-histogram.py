from pylab import *

dataset = [113, 115, 119, 121, 124, 
           124, 125, 126, 126, 126,
           127, 127, 128, 129, 130,
           130, 131, 132, 133, 136]


subplot(121)
boxplot(dataset, vert=False)

subplot(122)
hist(dataset)

show()
