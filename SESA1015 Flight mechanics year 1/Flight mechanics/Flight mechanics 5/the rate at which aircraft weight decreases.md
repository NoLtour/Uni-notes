---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you get
## The rate at which aircraft weight decreases
### Introduction
Unless you are drone striking an orphanage the only reason your plane should really be loosing weight is through fuel consumption, and here's a real shocker fuel consumption is determined by... engines. (at least I hope so)

So we need a nice way of expressing fuel consumption in terms of thrust, to do this we use [[specific fuel consumption (aircraft)]].

![[specific fuel consumption (aircraft)]]

### When in equilibrium
Well we know that:
- Thrust = Drag
- Lift = Weight

So lets sub that into out [[specific fuel consumption (aircraft)|s.f.c]] equation, we will also be using: [[lift to drag ratio]]

$$\begin{align*}
  \frac{dW(t)}{dt}  &= -sT\\
&= -sD\\
&= -s \frac{D}{L}L\\
&= -s \frac{D}{L}W & \frac{L}{D} &= \frac{C_L}{C_D} \\
&= -s \frac{C_D}{C_L}W
\end{align*}$$

^5fbc62

#### Derived equation

> ### $$ \frac{dW(t)}{dt} = -sW \frac{C_D}{C_L} $$ 
>> where:
>> $s=$ [[specific fuel consumption (aircraft)|specific fuel consumption]] 
>> $W(t)=$ weight at a given time
>> $W=$ Current total aircraft weight
>> $\frac{C_D}{C_L}^{-1}=$ [[lift to drag ratio]]

^5a7c77

#### Elaboration on conditions
It is a assumed that the [[lift to drag ratio]] is constant, but this requires lift to decrease as weight decreases (fuel use).

So to decrease lift, we need to change atleast one of the values which determine it:
![[lift equation#^1f2714]]

Here we have the choice of changing:
- density
-  true airspeed
-  angle of attack ([[effect of angle on lift coefficient|see why]])
-  
How these things are changed throughout the flight is called the [[cruise pattern]].