---
aliases: ["LES"]
tags: []
---

## Large eddy simulations
This is where instead of [[direct numerical simulation|DNS]] you ignore [[eddy (fluids)|eddies]] below a certain scale, of course this leads to your simulation missing information which will lead to potentially major inaccuracy in the simulation, to compensate for this we add a function $\tilde{F}_{x}$ to the [[navier stokes equations]] to model this missing data:
 
 $$ \frac{\delta u}{ \delta x } + \frac{\delta v}{ \delta y } = 0$$
 $$ u \frac{\delta u}{\delta x} + v \frac{\delta u}{\delta y}  = - \frac{1}{\rho} \frac{\delta p}{\delta x} + \nu \left( \frac{\delta^{2} u }{ \delta x^{2} } + \frac{\delta^{2} u }{ \delta y^{2} } \right)  $$  
 $$ u \frac{\delta v}{\delta x} + v \frac{\delta v}{\delta y}  = - \frac{1}{\rho} \frac{\delta p}{\delta y} + \nu \left( \frac{\delta^{2} v }{ \delta x^{2} } + \frac{\delta^{2} v }{ \delta y^{2} } \right)  $$   

