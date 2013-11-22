import scipy.misc
import matplotlib.pyplot as plt
lena = scipy.misc.lena()
plt.gray()
plt.imshow(lena)
plt.colorbar()
plt.show()
