import matplotlib.pyplot as plt
import scipy
import numpy


# because the image we loaded is RGB image, 
# http://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale

bug = scipy.misc.imread('stinkbug1.png')

# if you want to inspect the shape of the loaded image
# uncomment following line
#print bug.shape

# convert to gray
bug = bug[:,:,0]

# show original image
plt.figure()
plt.gray()

plt.subplot(121)
plt.imshow(bug)

# show 'zoomed' region
zbug = bug[100:350,140:350]

plt.subplot(122)
plt.imshow(zbug)

plt.show()
