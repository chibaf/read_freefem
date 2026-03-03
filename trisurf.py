# import packages
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# read data
coord=np.genfromtxt("Th.csv", delimiter=",")
print(coord)

x = coord[:,0]
y = coord[:,1]
z = coord[:,2]
tridata=np.genfromtxt("Th.csv", delimiter=",")
tri = mtri.Triangulation(x,y,triangles=tridata)

# plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(tri,z,cmap=plt.cm.jet)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u')
plt.show()
