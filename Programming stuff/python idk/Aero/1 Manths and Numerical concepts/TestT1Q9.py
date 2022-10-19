import numpy as np
import matplotlib.pyplot as plot

dx = 0.01
dy = 0.01

axisSize = 4

xPoints = np.arange( -axisSize, axisSize, dx )

yPoints = np.arange( -axisSize, axisSize, dy );

X, Y = np.meshgrid( xPoints, yPoints );

xVels = 5*X*(Y**2)
yVels = X*(Y**3)


xDelMod =( np.subtract(  (Y**3), 10*X*Y  ) )

plot.figure( 69 );

#plot.quiver( X, Y, xVels, yVels )

plot.colorbar( plot.contourf( X, Y, xDelMod, 20 ) )
#plot.plot( xPoints, intPoints, "bx" );

plot.show();