---
aliases: ["conservation of mass flow equation","area flow rate equation"]
tags: ["Question","QFormat3"]
---

#### What is the equation and theory assosiated with
## Conservation of mass in flow
### Into 
Basically for most cases (no fancy $E=mc^{2}$ or $\frac{dm}{dt}_{system}\neq 0$) since mass cannot just disapear, mass in = mass out (mass is not created or destroyed). Using this fact we can derive useful equations for modelling flow in a system.

### Equation

Note when applying this equation it is applied to the cross sectional area of the fluid not the pipe, because for a pipe that isn't full these two things arn't the same!

> ### $$ k = U_{1} A_{1} $$
> ### $$ U_{1} A_{1} = U_{2} A_{2} $$ 
>> where:
>> $k=$ a constant
>> $U_{x}=$ Flow velocity across a given cross section 
>> $A_{x}=$ Cross sectional area of flowing fluid
>> 
>> assuming:
>> - no change in total system mass
>> - constant density fluid (not compressible)

^90d47a

Alternative form which is alwayse valid (assuming no mass gets yeeted $E=mc^{2}$ style):

> ### $$ \frac{dm_{system}}{dt} = A_{1} \left(\frac{dx}{dt}\right)_{1} \rho_{1} - A_{2} \left(\frac{dx}{dt}\right)_{2} \rho_{2} $$ 
>> where:
>> (you can figure them out using the proof below, since this probably isn't needed I [[but you went through all the effort to add this message and meme|cba]] to label it properly)

^4e4ed8

### Proof
Given some shape we can define a bunch of equations to describe mass flow:
![[Pasted image 20220209120434.png]]

The mass in and mass out can be described using:
$$\begin{align*}
\frac{dm_{1}}{dt} &= A_{1} \left(\frac{dx}{dt}\right)_{1} \rho_{1} & \frac{dm_{2}}{dt} &= A_{2} \left(\frac{dx}{dt}\right)_{2} \rho_{2} \\
\frac{dm_{1}}{dt} &= A_{1} U_{1} \rho_{1} & \frac{dm_{2}}{dt} &= A_{2} U_{2} \rho_{2} 
\end{align*}$$

Then we can describe the total mass of the system using:
$$\begin{align*}
\frac{dm_{system}}{dt} &= \frac{dm_{1}}{dt} - \frac{dm_{2}}{dt}
\end{align*}$$
And sub in the equation for earlyer:

$$\begin{align*}
\frac{dm_{system}}{dt} &= A_{1} U_{1} \rho_{1} - A_{2} U_{2} \rho_{2} \\
\end{align*}$$

Now if we assume that the fluids density is constant (it's not compressible) and that there is no mass accumulation in the sytem:

$$\begin{align*}
0 &= A_{1} U_{1} \rho - A_{2} U_{2} \rho \\
A_{2} U_{2} &= A_{1} U_{1} \\
\end{align*}$$

Now since the $A_{1}$ and $U_{1}$ are constant we can also express this as:

$$ k = AU $$

So if we can find the flow rate or cross section at any point in the pipe if we know it at one point.