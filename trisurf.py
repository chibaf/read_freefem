# import packages
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# read data
a=np.genfromtxt("u.csv", delimiter=",", usemask=True)
print(a[0][0:3])

# plot
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot_trisurf(tri,z,cmap=plt.cm.jet)
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('u')
#plt.show()
