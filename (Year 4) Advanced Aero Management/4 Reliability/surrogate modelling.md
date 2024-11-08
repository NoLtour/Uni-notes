---
aliases:
  - meta model
  - response surface
tags:
---

## Surrogate modelling

As suggested in [[optimisation under uncertainty#Randomised Sampling]] we can use [[Monte Carlo simulation]] to find solutions, the problem is this type of optimisation can be extremely computationally demanding. A suitable solution is using surrogate models.

Here we attempt to emulate the true function with a more computationally efficient function, permitting much faster computation in our [[Monte Carlo simulation]]. This often involves curve fitting or some sort of interpolation.

