import numpy as np
import matplotlib.pyplot as plot 

theta  = np.arange(0, np.pi, 0.001)

alpha = 5 * np.pi/180

eta = 0.2

Cps = 4 * ( alpha * (1 + np.cos(theta))/np.sin(theta) + eta * np.sin(theta) )

c = 10

plot.plot( (c/2) * (1 - np.cos(theta) ), Cps )
plot.xlabel( "distance from leading edge (x)" )
plot.ylabel( "Pressure coeff between top and bottom" )
plot.ylim([0, 4])
plot.grid()
plot.show()