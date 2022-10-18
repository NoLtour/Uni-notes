import numpy as np
import matplotlib.pyplot as plot

dx = 0.1
dy = 0.1

axisSize = 20

xPoints = np.arange( -axisSize, axisSize, dx )

yPoints = np.arange( -axisSize, axisSize, dy );

X, Y = np.meshgrid( xPoints, yPoints );

intPoints = X**2 * Y**2

plot.figure( 69 );

plot.colorbar( plot.contourf( xPoints, yPoints, intPoints, 150 ) )
#plot.plot( xPoints, intPoints, "bx" );

plot.show();