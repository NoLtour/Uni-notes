import numpy as np
import matplotlib.pyplot as plot

dx = 0.25
dy = 0.25

axisSize = 4

xPoints = np.arange( -axisSize, axisSize, dx )

yPoints = np.arange( -axisSize, axisSize, dy );

X, Y = np.meshgrid( xPoints, yPoints );

xVels = 5*X*(Y**2)
yVels = X*(Y**3)

xDelMod = np.add( np.gradient( xVels ) , np.gradient( yVels ) )

plot.figure( 69 );

plot.quiver( X, Y, xVels, yVels )

#plot.colorbar( plot.contourf( X, Y, np.gradient( xVels ), 8 ) )
#plot.plot( xPoints, intPoints, "bx" );

plot.show();