---
aliases: [""]
tags: []
---

## Simplified model of the car dynamics

As an introduction to much of the content, it's best to work through a example and introduce concepts along the way to contextualise them all first.


### [[control system loop types|Open-loop system]] implementation

#### Creating the car model

![[Pasted image 20231014123644.png]]

Here we can quite intuitively assume 2 forces:
- $F_{p}(t)$, the propulsive force of the engine
- $F_{d}(t)$, environmental disturbance force (random stuff, eg wind gusts)

Creating a more practical representation we can model the car as a lumped mass $m$, it becomes clear there will be some frictional force:

![[Pasted image 20231014123810.png]]

A simple model of friction could just be some frictional constant times velocity ($F_{B} = -Bv$), then [[Newtons second law]]:
$$\begin{align*}
m a   &= \sum\limits F\\
  &= F_{p}(t) + F_{d}(t) - Bv\\
m \frac{dv}{dt} + Bv &= F_{p}(t) + F_{d}(t)   
\end{align*}$$

#### Creating the [[systems control defs|input]]s

For a car we control engine force using a pedal, so let's do just that. Model propulsive force as a linear function of pedal angle ($\theta$) times some constant ($K_{e}$):
$$ F_{p}(t) = K_{e}\: \theta(t) $$

Subbing back:
$$\begin{align*}
m \frac{dv}{dt} + Bv &= F_{p}(t) + F_{d}(t)    && &\to && m \frac{dv}{dt} + Bv &= K_{e}\: \theta(t) + F_{d}(t)    
\end{align*}$$

#### [[block diagram|Block diagram]] representation

![[Pasted image 20231014124800.png]]

This is a [[control system loop types|open-loop system]], it'd be the equivalent of closing your eyes ignoring any feedback and just holding the pedal at some speed... which unless you are a [[yoooo that is what they call me|impressively terrible]] driver is not how these things work. 

#### Expanding the force balance equation

##### Assuming no disturbance

Since $F_{d}(t)$ is some undefined function, let's just assume no strange inputs and the car is on level ground:

$$\begin{align*}
& &  F_{d}&= 0 \\
m \frac{dv}{dt} + Bv &= K_{e}\: \theta(t) + F_{d}(t) & &\to & m \frac{dv}{dt} + Bv &= K_{e}\: \theta(t)\\
&& && \frac{m}{B} \frac{dv}{dt} + v &= \frac{K_{e}}{B}  \theta(t)
\end{align*}$$

Now if we compare this with the [[standard form first-order ODE]] and take $\theta$ as a constant:
$$\begin{align*} && \tau \frac{dy}{dt} + y  &= f(t) \\\\ 
\frac{m}{B} \frac{dv}{dt} + v &= \frac{K_{e}}{B}  \theta  &&  \to& \tau &= \frac{m}{B} \\ && && f(t) &= \frac{K_{e}}{B} \theta  \\ && && y&=v  \end{align*}$$

It becomes clear we can just [[solution of first order linear differential equations|solve it as a first order inhomogeneous ODEs]]:
$$\begin{align*}
\tau \frac{dv}{dt} + v &= f(t) & &\to & v(t) &= e^{-\frac{ t}{\tau}} \left[ \int e^{\frac{t}{\tau}} \times f(t)\cdot dt + C \right] \\
&& &&  &= e^{-\frac{ t}{\tau}} \left[ \frac{1}{\tau} e^{\frac{t}{\tau}} \times f  + C \right] \\
&& &&  &=   \frac{1}{\tau} f  + C e^{-\frac{ t}{\tau}}\\
&& && v  &=   \frac{B}{m} \frac{K_{e}}{B} \theta  + C e^{-\frac{ t B}{m}}\\
&& && v  &=   \frac{K_{e}}{m} \theta   + C e^{-\frac{ t B}{m}}
\end{align*}$$

Then we can take the case where at $t=0,$ $v=0$:

$$\begin{align*}
0  &=   \frac{K_{e}}{m} \theta  + C e^{-\frac{ 0\times B}{m}}\\
0  &=   \frac{K_{e}}{m} \theta  + C  & &\to &  C  &= -  \frac{K_{e}}{m} \theta    
\end{align*}$$
Subbing this back:
$$\begin{align*}
v  &=   \frac{K_{e}}{m} \theta   + C e^{-\frac{ t B}{m}} & & \to & v  &=   \frac{K_{e}}{m} \theta   -  \frac{K_{e}}{m} \theta    e^{-\frac{ t B}{m}}& \to &
 &v  &=   \frac{K_{e}\theta}{m}   \left(1 -   e^{-\frac{ t B}{m}} \right)
\end{align*}$$

This can be plotted:
![[Pasted image 20231014152325.png]]

It's clear that after holding theta at a set value it will slowly tend to some value $v_{ss}$ and taking a look at the final equation we made the value of $v_{ss}$ is obvious:

$$\begin{align*}
&& v_{ss}&=  \frac{K_{e}\theta}{m} \\
v  &=   \frac{K_{e}\theta}{m}   \left(1 -   e^{-\frac{ t B}{m}} \right) & &\to & v  &=  v_{ss}  \left(1 -   e^{-\frac{ t B}{m}} \right)
\end{align*}$$

It's pretty easy to find the particular solution for a case where at $t=0, v=v_{0}$ then see the corresponding graph, since $\theta$ is constant it'll basically always look like some $e$ graph converging to some $v_{ss}$ depending on $\theta$. Of course if $\theta=0$ then $v_{ss}=0$ and speed will converge to zero.

### [[control system loop types|Closed-loop system]] implementation

#### Modelling the feedback

Now to get somewhere useful. 

To reach a target speed, it's clear that by definition the "error" will be difference between desired speed $v_{d}$ and current speed $v$. To keep thing's convenient let's order the subtraction such that the error represents the desired "direction of correction" so it is negative if the speed is too high and positive when below:
$$\begin{align*}
e(t) &= v_{d}(t) - v(t)
\end{align*}$$

Note that if you are wondering why everything is a function of time, it's because literally everything can be described as *some* function of time at their root, so if some function doesn't have a clear definition you can always default to "time".

Ok now, lets say that some response to this error creates the correcting action to theta. Hence theta can be defined as $e$ times this correcting response $K_{p}$:

$$\begin{align*}
\theta(t) &= K_{p} e(t) & &\to & \theta(t) &= K_{p}( v_{d}(t) - v(t) )
\end{align*}$$

Subbing back into $F_{p}$:
$$\begin{align*}
F_{p}(t) &= K_{e}\: \theta(t) & &\to & F_{p}(t) &= K_{e}  K_{p}( v_{d}(t) - v(t) )
\end{align*}$$

#### Creating a block diagram

![[Pasted image 20231014125300.png]]

Here we are using a purely linear response to error, this is known as [[control response types|proportional control]].

#### Expanding the force balance equation

##### Assuming no disturbance

Since $F_{d}(t)$ is some undefined function, let's just assume no strange inputs and the car is on level ground:

$$\begin{align*}
& &  F_{d}&= 0 \\
& &  F_{p}&= K_{e}  K_{p}( v_{d}(t) - v(t) ) \\
m \frac{dv}{dt} + Bv &= F_{p}(t)  + F_{d}(t) & &\to &  m \frac{dv}{dt} + Bv &= K_{e}  K_{p}( v_{d}  - v  ) \\
 
\end{align*}$$

Now if we turn this into a [[standard form first-order ODE]]:
$$\begin{align*}
m \frac{dv}{dt} + Bv &= K_{e}  K_{p}( v_{d}  - v  ) & &\to & \frac{m}{ B + K_{e}  K_{p}} \frac{dv}{dt} + v  &=  \frac{ K_{e}  K_{p} v_{d}}{ B + K_{e}  K_{p}}   & \to& &  \tau \frac{dv}{dt} + v  &= f(t) \\\\
&& && && \tau =& \frac{m}{ B + K_{e}  K_{p}} \\
&& && && f =&  \frac{ K_{e}  K_{p} v_{d} (t) }{ B + K_{e}  K_{p}} \\
 \end{align*}$$
Now if we take the case that $v_{d}$ is a constant, solving is trivial ([[solution of first order linear differential equations|solving first order inhomogeneous ODEs]]) once we take $v_{d}$ as constant:

$$\begin{align*}
&& \text{from}&\text{ previous}\\
v(t) &= e^{-\frac{ t}{\tau}} \left[ \int e^{\frac{t}{\tau}} \times f(t)\cdot dt + C \right] & &\to & v  &=   \frac{1}{\tau} f  + C e^{-\frac{ t}{\tau}} \\
&& &&  &=   \frac{1}{\frac{m}{ B + K_{e}  K_{p}}} \frac{ K_{e}  K_{p} v_{d}   }{ B + K_{e}  K_{p}}  + C e^{-\frac{ t}{\frac{m}{ B + K_{e}  K_{p}}}} \\
&& && v(t) &=   \frac{ K_{e}  K_{p} v_{d}   }{  m}  + C e^{-\frac{ t(B + K_{e}  K_{p})}{ m }} \\
\end{align*}$$

Then if we take $t=0, v=v_{0}$:

$$\begin{align*}
v_{0} &=   \frac{ K_{e}  K_{p} v_{d}   }{  m}  + C e^{-\frac{ 0\times(B + K_{e}  K_{p})}{ m }} \\
v_{0} &=   \frac{ K_{e}  K_{p} v_{d}   }{  m}  + C  & &\to & C &= v_{0} -   \frac{ K_{e}  K_{p} v_{d}   }{  m} 
\end{align*}$$

Subbing back again:

$$\begin{align*}
v(t) &=   \frac{ K_{e}  K_{p} v_{d}   }{  m}  + C e^{-\frac{ t(B + K_{e}  K_{p})}{ m }} && \to & 
v(t) &=   \frac{ K_{e}  K_{p} v_{d}   }{  m}  + \left( v_{0} -   \frac{ K_{e}  K_{p} v_{d}   }{  m} \right) e^{-\frac{ t(B + K_{e}  K_{p})}{ m }} 
\end{align*}$$

If we once again assume acceleration from rest ($v_{0} = 0$):
$$\begin{align*}
v(t) &=   \frac{ K_{e}  K_{p} v_{d}   }{  m}  + \left( 0 -   \frac{ K_{e}  K_{p} v_{d}   }{  m} \right) e^{-\frac{ t(B + K_{e}  K_{p})}{ m }}  & &\to &
v(t) &=   \frac{ K_{e}  K_{p} v_{d}   }{  m}  \left(  1 - e^{-\frac{ t(B + K_{e}  K_{p})}{ m }}     \right) 
\end{align*}$$

Which is this thing again:
![[Pasted image 20231014155515.png]]

