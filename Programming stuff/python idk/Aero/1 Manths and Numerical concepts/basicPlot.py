import numpy as np
import matplotlib.pyplot as plot

dx = 0.1

xPoints = np.arange( -5, 5, dx )

test = xPoints ** 0.5

figure = plot.figure( 69 );

plot.plot( xPoints, test, "kx" );

y_axis = figure.add_subplot(211)

y_axis.set_ylabel("test")

plot.show();