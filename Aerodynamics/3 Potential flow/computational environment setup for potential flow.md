---
aliases: [""]
tags: []
---

## Computational environment setup for potential flow

First we need to setup the grid that will form the space in which the flow occurs, hence we define the domain size as well as the step interval (resolution of our grid):

```jupyter
import numpy as np
import matplotlib.pyplot as plot

domainWidth = 4;

xMin = -domainWidth
xMax = domainWidth
zMin = -domainWidth
zMax = domainWidth

dx = dz = 0

xAxis = np.arrange( xMin, xMax )

```

