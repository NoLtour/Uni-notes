---
aliases: [""]
tags: []
---

## Navier stokes equations
Our [[euler equations for inviscid and incompressible flow]] are [[crenge|cring]], since they exclude so much... so to get more [[BaSeD|based]] equations we need to include viscosity, hence the navier stokes equations.

> ### $$ \frac{\delta V_{x}}{ \delta x } + \frac{\delta V_{y}}{ \delta y } = 0$$
> ### $$ \rho \left(V_{x} \frac{\delta V_{x}}{\delta x} + V_{y} \frac{\delta V_{x}}{\delta y} \right) = -\frac{\delta p}{\delta x} + \frac{\delta \tau_{xx}}{\delta x} + \frac{\delta \tau_{xy}}{\delta y} $$ 
> ### $$ \rho \left(V_{x} \frac{\delta V_{y}}{\delta x} + V_{y} \frac{\delta V_{y}}{\delta y} \right) = -\frac{\delta p}{\delta y} + \frac{\delta \tau_{yy}}{\delta x} + \frac{\delta \tau_{yx}}{\delta y} $$ 
>> where:
>> $V_{x},V_{y}=$ velocity in y and x axis
>> $\rho=$ density
>> $\tou=$ [[normal stress]]
