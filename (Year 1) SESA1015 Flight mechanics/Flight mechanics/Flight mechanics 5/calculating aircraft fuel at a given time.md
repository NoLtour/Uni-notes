---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How would you go about
## Calculating aircraft fuel at a given time
### Introduction
#### Rate of change
To calculate the fuel at a given time we need to know the rate at which fuel is used as well as starting fuel, luckily we already found the first part:

![[the rate at which aircraft weight decreases#^5a7c77]]

#### Weight
In reality the weight of the aircraft isn't just fuel, it also contains "aircraft bits" (that's the technical term) and sometimes valuable cargo such as the cocaine bricks hidden inside the chairs. So for this we need to describe what makes up the aircrafts weight:

![[weight of an aircraft]]

### Maths
Now we have starting conditions defined and rate of change, you can guess what comes next. Integration! (fun)

$$\begin{align*}
    \frac{dW}{dt} &= -sW \frac{C_D}{C_L}\\
\int \frac{1}{W} dW &= -s \frac{C_D}{C_L} \int  1 dt\\
\ln(W) &= -s \frac{C_D}{C_L} (t + k)\\
W &=e^{ -s \frac{C_D}{C_L} t + k} \\
&= ke^{ -s \frac{C_D}{C_L} t }& at\:t=0,\:\:\:W&=W_s+W_f\\
& & W_s+W_f &= k e^{0}\\
& & W_s+W_f &= k\\
&= (W_s+W_f)e^{ -s \frac{C_D}{C_L} t }\\
\frac{W}{(W_s+W_f) }&=e^{ -s \frac{C_D}{C_L} t }\\
\ln(\frac{W}{(W_s+W_f) })&=-s \frac{C_D}{C_L} t\\
\ln(\frac{W}{(W_s+W_f) })\frac{C_L}{C_D} \frac{-1}{s} &=  t\\
t &=\frac{1}{s} \frac{C_L}{C_D}  \ln( 1+\frac{W_f}{W_s })
\end{align*}$$

^d0cc24

#### Endurance equation
![[endurance]]

![[endurance equation]]

#### Implications
Now we have an equation for endurance we can see that to malaise endurance you need:
- As small a [[specific fuel consumption (aircraft)|s.f.c]] as possible. So you need as efficient engines as possible.
- As high [[lift to drag ratio]] as possible. So you need very efficient aerodynamic characteristics.
- As high a $W_f/W_s$ as possible. So you need to use light materials and optimize the structure to be as light as possible.