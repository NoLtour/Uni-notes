```jupyter
import numpy as np
import matplotlib.pyplot as plot

dx = 0.1

xPoints = np.arange( -5, 5, dx )

yPoints = xPoints ** 2

plot.figure( 69 );

plot.plot( xPoints, yPoints, "kx" );

plot.ylabel("outputs (trol units)")
plot.xlabel("inputs (trol units)")  

plot.show();
```