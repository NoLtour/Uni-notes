import numpy as np
import matplotlib.pyplot as plot

dx = 0.1

xPoints = [160, 180, 200, 220, 240, 260, 280, 300, 320, 340]

yPoints = [6.23, 5.97, 6.07, 6.97, 8.04, 7.72, 7.54, 6.79, 7.9, 8.43]


plot.figure( 69 );

plot.plot( xPoints, yPoints, "kx" );
#plot.plot( xPoints, intPoints, "bx" );

plot.show();