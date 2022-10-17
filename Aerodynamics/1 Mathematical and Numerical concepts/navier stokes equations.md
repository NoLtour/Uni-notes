---
aliases: [""]
tags: []
---

## Navier stokes equations
Our [[euler equations for inviscid and incompressible flow]] are [[crenge|cring]], since they exclude so much... so to get more [[BaSeD|based]] equations we need to include viscosity, hence the navier stokes equations.

> ### $$ \frac{\delta V_{x}}{ \delta x } + \frac{\delta V_{y}}{ \delta y } = 0$$
> ### $$ V_{x} \frac{\delta V_{x}}{\delta x} + V_{y} \frac{\delta V_{x}}{\delta y}  = - \frac{1}{\rho} \frac{\delta p}{\delta x} + \nu \left( \frac{\delta^{2} V_{x} }{ \delta x^{2} } + \frac{\delta^{2} V_{x} }{ \delta y^{2} } \right)  $$  
> ### $$ V_{x} \frac{\delta V_{y}}{\delta x} + V_{y} \frac{\delta V_{y}}{\delta y}  = - \frac{1}{\rho} \frac{\delta p}{\delta y} + \nu \left( \frac{\delta^{2} V_{y} }{ \delta x^{2} } + \frac{\delta^{2} V_{y} }{ \delta y^{2} } \right)  $$  
>> where:
>> $V_{x},V_{y}=$ velocity in y and x axis
>> $\rho=$ density 
>> $p=$ pressure
>> $\nu=$ [[kinematic viscosity]]
