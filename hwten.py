import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize
#Define my function
def Funct(x,y):
    Valz = (1/2*x)*1/2*y
    return Valz
#Prelimiary work to find the minimum
upper = -2
lower = 2
x0 = np.arange(upper, lower, 0.1)
y0 = np.arange(upper, lower, 0.1)
X, Y = np.meshgrid(x0, y0)
Z = Funct(X, Y)

min_val = np.where(Z == Z.min()) # where [0] and [1] rows and coloumbs respectively 
listOfCoordinates = list(zip(min_val[0], min_val[1])) # (x,y) of the coordinates
xmin_1 = x0[listOfCoordinates[0][0]]
ymin_1 = y0[listOfCoordinates[0][1]]

xmin_2 = x0[listOfCoordinates[1][0]]
ymin_2 = y0[listOfCoordinates[1][1]]

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='plasma')
ax.scatter3D(xmin_1, ymin_1, [Funct(xmin_1, ymin_1)], s=[100], c="g");
ax.scatter3D(xmin_2, ymin_2, [Funct(xmin_2, ymin_2)], s=[100], c="g");
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
ax.set_title('z = (1/2x)*1/2y')
plt.show()

for angle in range(0, 360):
    ax.view_init(30, 40)

