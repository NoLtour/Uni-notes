---
aliases: [""]
tags: []
---

## Computational environment setup for potential flow

First we need to setup the grid that will form the space in which the flow occurs, hence we define the domain size as well as the step interval (resolution of our grid):

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

