---
aliases:
  - normal shock
tags:
---

## Normal shock properties equations


### Property changes
The main take away regarding normal shocks is that:
- Entropy increases
- Energy is conserved

With that in mind how other properties change is easy to predict:
- [[stagnation points in a compressible flow|Stagnation temperature]]  is constant as it's just a representation of energy ([[enthalpy]] = temp = energy in [[ideal gas law|ideal gas]]), which we know is conserved
- Stagnation pressure drops, because the useful energy decreases since [[entropy]] increases, which is also why temperature increases
- Density increases because of the speed drop

#### Entropy

Something else to keep in mind is that the magnitude of these changes increases exponentially with [[Mach number]], with a negligible change with normal shocks occurring at Mach 1. So we can reduce entropy increase by avoiding normal shocks far away from Mach 1!
![[Pasted image 20231026103726.png]]

### Equations

Something to keep in mind, is these are derived under the assumption of a [[perfect gas]].

> ### $$\begin{align*} M_{2}^{2}  &= \frac{(\gamma - 1) M_{1}^{2} + 2}{2\gamma M_{1}^{2} - (\gamma - 1)}  \end{align*}$$
> ### $$\begin{align*} \frac{P_{2}}{P_{1}} &= \frac{2\gamma M_{1}^{2} - (\gamma - 1)}{\gamma+1} \end{align*}$$
> ### $$\begin{align*} \frac{\rho_{2}}{\rho_{1}} &= \frac{M_{1}^{2} (\gamma + 1)}{(\gamma-1)M_{1}^{2} + 2} \end{align*}$$
> ### $$\begin{align*} \frac{P_{02}}{P_{01}} &= \left[\frac{(\gamma+1)M_{1}^{2}}{(\gamma-1)M_{1}^{2} + 2}\right]^{\frac{\gamma}{\gamma-1}} \left[ \frac{\gamma+1}{2\gamma M_{1}^{2} - (\gamma-1)} \right]^\frac{1}{\gamma-1} \end{align*}$$
> ### $$\begin{align*} T_{01} &= T_{02} \end{align*}$$
>> where:
>> $P_{0n}=$ [[stagnation pressure]]
>> $\rho_{n}=$ density
>> $P_{n}=$ [[static pressure]] 
>> $\gamma=$ [[specific heat ratio]]
>> $M_{n}=$ [[Mach number]]
>> $T_{0n}=$ [[stagnation points in a compressible flow|stagnation temperature]], constant since process is [[adiabatic expansion or compression|adiabatic]]
>> In this context $X_{1\to2}$ is across a normal shock, hence $M_{1}>1>M_{2}$ 

