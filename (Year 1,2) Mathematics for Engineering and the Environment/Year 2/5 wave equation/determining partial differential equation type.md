---
aliases: ["determining PDE type"]
tags: []
---

## Determining partial differential equation type

It's quite easy to find the [[classification of partial differential equations|classification of PDEs]]. This is the most general case of second order linear PDEs:
$$ a \frac{\delta^{2} u}{ \delta x^{2} } + 2b \frac{\delta^{2}u}{\delta x \delta y} + c \frac{\delta^{2} u}{\delta y^{2}} + d \frac{\delta u}{\delta x} + e \frac{\delta u}{\delta y} + fu = 0 $$
The value of $b^{2}-ac$ determines what type it is.

> ### $$ a \frac{\delta^{2} u}{ \delta x^{2} } + 2b \frac{\delta^{2}u}{\delta x \delta y} + c \frac{\delta^{2} u}{\delta y^{2}} + d \frac{\delta u}{\delta x} + e \frac{\delta u}{\delta y} + fu = 0 $$
>> conditions:
>> $b^{2}-ac<0$ then it's a [[elliptic partial differential equations|elliptic PDE]] 
>> $b^{2}-ac=0$ then it's a [[hyperbolic partial differential equations|hyperbolic PDE]]
>> $b^{2}-ac>0$ then it's a [[parabolic partial differential equations|parabolic PDE]]

Since variables $a\to f$ are functions of $x,y$ it is possible that the classification of the PDE can change as the coordinates $y,x$ vary, so it is necessary to check the classification of the PDE across the entire range. If it does change classification across the range then you may need to find multiple solutions.
