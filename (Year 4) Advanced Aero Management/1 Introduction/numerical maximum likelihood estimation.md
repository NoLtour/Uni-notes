---
aliases: [""]
tags: []
---

## Numerical maximum likelihood estimation

The previously outlined [[maximum likelihood estimation]] won't work for all functions, since for some of them a analytical solution just doesn't exist. For these we can still employ it, but instead of solving for the turning point which then determines where "maximum likelihood" is, we find the maximum by treating it as an optimization problem. Fundamentally the equations used are the same, we just replace the solving step:

![[maximum likelihood estimation#^6e1413]]

Python can do lot's of the heavy lifting for you if you use the scipy.stats library with the .fit operator.
