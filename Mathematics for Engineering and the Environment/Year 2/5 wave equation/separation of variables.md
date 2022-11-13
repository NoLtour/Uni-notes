---
aliases: [""]
tags: []
---

## Separation of variables
### Intro

Ok so we have the abomination from [[classification of partial differential equations|classification of PDEs]], so how the fuck are we supposed to solve it? 
$$ a \frac{\delta^{2} u}{ \delta x^{2} } + 2b \frac{\delta^{2}u}{\delta x \delta y} + c \frac{\delta^{2} u}{\delta y^{2}} + d \frac{\delta u}{\delta x} + e \frac{\delta u}{\delta y} + fu = 0 $$
Turns out it's not so bad, we start by assuming the solution is:
$$ y(x,t) = X(x) \times T(t) $$
Now you see we've [[see what I did there so funny|__separated__ the variables]] into two simpler functions, theoretically these functions are just [[ordinary differential equation|ODE]]s so they can be solved as such!
