---
aliases: ["pressure"]
tags: ["Question","QFormat3"]
---

#### What is
## Pressure (hydrostatics)
### Intro
Pressure within a fluid follows has the following properties:
- Pressure only acts at the normal of the adjasent surfaces

#### Proof
Take this situation:
![[Pasted image 20220113190959.png]]

We can use the [[pressure volume work]] equation and the [[pressure (hydrostatics)#^07ca11]] equations to proof that the pressure at the bottom is entirely dependent on h.
We can use conservation of energy and the work done at B and at A to proof the relation:
$$\begin{align*}
pV &= E_{B} \\
p A_{B} x_{B} &= E_{B}& dE_{A}= -dh\rho g h A_{A} \\
p A_{B} dx_{B} &= dE_{B}\\
p A_{B} dx_{B} &= -dh A_{A} \rho gh\\
p&= -\frac{dh}{dx_{B}} \frac{A_{A}}{A_{B}} \rho gh
\end{align*}$$

Now if we get a variable for the rate of movement of volume $dV$:

$$\begin{align*}
p &= -\frac{dh}{dx_{B}} \frac{A_{A}}{A_{B}} \rho gh & dh &= - \frac{dV}{A_{A}} & dx_{B} &= \frac{dV}{A_{B}}\\
&= -\frac{- \frac{dV}{A_{A}}}{\frac{dV}{A_{B}}} \frac{A_{A}}{A_{B}} \rho g h\\
&= \frac{ A_{B}dV}{A_{A}dV} \frac{A_{A}}{A_{B}} \rho g h\\
&= \rho g h
\end{align*}$$
Since $\rho g h$ is just used to represent the weight of a 1d column, this proof also works for compressible fluids where $\rho g h$ is replaced with some functionally equivilent function.

### Equations
The pressure due to the weight of the above an uncompressible fluid column can be determined using:
> ### $$ p = h\rho g $$ 
>> where:
>> $p=$ [[pressure (hydrostatics)]]
>> $h=$ hight of column
>> $\rho=$ density of fluid
>> $g=$ gravity

^07ca11

For uncompressible fluids you can take $\rho$ as constant, but for gases you might need to be more creative, this form should work:
> ### $$ d p = \rho(h) \times  g(h) \times d h $$ 
>> where:
>> $p=$ [[pressure (hydrostatics)]]
>> $h=$ hight of column
>> $\rho(h)=$ density of fluid as a function of h
>> $g(h)=$ gravity as a function of h

### Example
If we wanted to model the pressure in atmosphere at some hieght we could use the [[ideal gas law]] as well as the second version of this equation:

To make things easy I'm going to assume:
- Constant gravity
- Constant temperature
- Constant atmospheric composition
- Ideal gas law is valid

$$\begin{align*}
& & pV &= mRT\\
dp &= \rho g dh & \frac{p}{RT} &= \rho\\
\int 1 \cdot dp &= \int \frac{p}{RT} g \cdot dh\\
\int \frac{1}{p} \cdot dp &= \int \frac{1}{RT} g \cdot dh
\end{align*}$$
Now if we can define column hieght $h_P=H_{0}-H$ at pressure $P$, and then pressure for the entire column height to be a hieght of $H_0$ and pressure of $P_0$:
$$\begin{align*}
\int^{P_0}_{P} \frac{1}{p} \cdot dp &= \int^{H_0}_{H_0-H} \frac{1}{RT} g \cdot dh\\
[ \ln(p) ]^{P_0}_{P} &= [\frac{gh}{RT}]^{H_0}_{H_0-H}\\
\ln({P}) - \ln(P_{0})&= \frac{g}{RT}(H_0-H-H_0)\\
ln\left(\frac{P}{P_{0}}\right)&= -\frac{Hg}{RT}\\
\frac{P}{P_{0}}&=e^{-\frac{Hg}{RT}}\\
P&=P_{0} \times e^{-\frac{Hg}{RT}}
\end{align*}$$
And now you have an equation that (poorly) models the density of the atmosphere above some refrence pressure.