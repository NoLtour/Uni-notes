---
aliases: ["LES"]
tags: []
---

## Large eddy simulations
This is where instead of [[direct numerical simulation|DNS]] you ignore [[eddy (fluids)|eddies]] below a certain scale, of course this leads to your simulation missing information which will lead to potentially major inaccuracy in the simulation, to compensate for this we add a function $\tilde{F}_{x}$ to the [[navier stokes equations]] to model this missing data from the ignored smaller scale eddies:
 
 $$ \frac{\delta \tilde{u}}{ \delta x } + \frac{\delta \tilde{v}}{ \delta y } = 0$$
 $$ \tilde{u} \frac{\delta \tilde{u}}{\delta x} + \tilde{v} \frac{\delta \tilde{u}}{\delta y}  = - \frac{1}{\rho} \frac{\delta p}{\delta x} + \nu \left( \frac{\delta^{2} \tilde{u} }{ \delta x^{2} } + \frac{\delta^{2} \tilde{u} }{ \delta y^{2} } \right) + \tilde{F}_{x} $$  
 $$ \tilde{u} \frac{\delta \tilde{v}}{\delta x} + \tilde{v} \frac{\delta \tilde{v}}{\delta y}  = - \frac{1}{\rho} \frac{\delta p}{\delta y} + \nu \left( \frac{\delta^{2} \tilde{v} }{ \delta x^{2} } + \frac{\delta^{2} \tilde{v} }{ \delta y^{2} } \right) + \tilde{F}_{y} $$   
Although still very computationally expensive, it is much less demanding than [[direct numerical simulation]] so is doable for moderate reynolds numbers on a supercomputer in a reasonable timeframe. The exact model used for $\tilde{F}_{x},\tilde{F}_{y}$ may change depending on the situation you want to model for to maximise accuracy in that use case.