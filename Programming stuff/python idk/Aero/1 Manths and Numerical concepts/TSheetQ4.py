import numpy as np
import matplotlib.pyplot as plot

dx = 0.1

dr = 0.1

rMax = 15

R = 2

# r = 0 -> rMax
rP1 = np.arange( 0, R, dr )
rP2 = np.arange( R, rMax, dr )

T = 5

# u_theta = func(r)
uThP1 = T*rP1/(R**2)
uThP2 = T/rP2
uThP = uThP1 + uThP2

# u_r = 0
uRP = np.repeat( 0, uThP )


test = xPoints ** 0.5

plot.figure( 69 );

plot.plot( xPoints, test, "kx" );

plot.show();