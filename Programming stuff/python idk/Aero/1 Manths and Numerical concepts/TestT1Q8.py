import numpy as np
import matplotlib.pyplot as plot

dx = 0.1

xPoints = np.arange( 0, 1, dx )

yPoints = 32 * np.cos( xPoints )**5 + 5 * xPoints**3;

intPoints = []

for i in range( 0, len(xPoints) ):
    intPoints.append( np.trapz( yPoints[0:i], xPoints[0:i] ) )

plot.figure( 69 );

plot.plot( xPoints, yPoints, "kx" );
plot.plot( xPoints, intPoints, "bx" );

plot.show();