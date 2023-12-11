---
aliases:
  - Nusselt number
  - Stanton number
tags:
---

## Convection heat transfer coefficient ($h$)

### Calculating it

Calculating $h$ is much easier said than done, although there are some exact derived relations in special laminar cases, generally it's very messy.
You know what that means, just use [[the cheat code for not having to understand something|empirical relations]]!


> ### $$\begin{align*} \text{Laminar pipe flow:}&& \text{Nu} &=  \left\{ \begin{aligned} &4.364, &&\text{ if wall heat flux is uniform} \\  &3.658, &&\text{ if wall temperature is uniform} \end{aligned} \right. \\\\\text{Turbulant pipe flow:}&& \text{Nu}_{x} &=  \left\{ \begin{aligned} &0.023\:\text{Re}_{x}^{\frac{4}{5}}\:\text{Pr}^{0.4}, &&\text{ if flow being heated} \\  &0.023\:\text{Re}_{x}^{\frac{4}{5}}\:\text{Pr}^{0.3}, &&\text{ if flow being cooled} \end{aligned} \right. \\\\ \text{Laminar boundary layer:}&& \text{Nu}_{x} &=  \left\{ \begin{aligned} &0.453\:\text{Re}_{x}^{\frac{1}{2}}\:\text{Pr}^{\frac{1}{3}}, &&\text{ if wall heat flux is uniform} \\  &0.332\:\text{Re}_{x}^{\frac{1}{2}}\:\text{Pr}^{\frac{1}{3}}, &&\text{ if wall temperature is uniform} \end{aligned} \right. \\\\ \text{Turbulant boundary layer:}&& \text{Nu}_{x} &=  \left\{ \begin{aligned} &0.0308\:\text{Re}_{x}^{\frac{4}{5}}\:\text{Pr}^{\frac{1}{3}}, &&\text{ if wall heat flux is uniform} \\  &0.0296\:\text{Re}_{x}^{\frac{4}{5}}\:\text{Pr}^{\frac{1}{3}}, &&\text{ if wall temperature is uniform} \end{aligned} \right. \\\\ \text{General form:}&& \text{Nu} &= C\:\text{Re}^{n}\:\text{Pr}^{m} \\\\\end{align*}$$ 
> ### $$\begin{align*}\text{Nu}  &=  \text{St} \cdot \text{Re} \cdot\text{Pr}&&& \text{Nu}  &= \frac{hL}{k} &&& \text{St}  &= \frac{h}{\rho V c_{p}} \end{align*}$$
>> where:
>> $\text{Nu}=$ Nusselt number
>> $\text{St}=$ Stanton number
>> $\text{Re}=$ [[Reynolds number]]
>> $\text{Pr}=$ [[Prandtl number]]
>> $h=$ [[convection heat transfer coefficient]]
>> $L=$ characteristic length, may be subbed in for $x$ when working with boundary layers
>> $V=$ characteristic velocity
>> $k=$ [[material thermal conductivity|thermal conductivity]]
>> $c_{p}=$ [[constant pressure specific heat]]
>> $\text{Nu}_{x}=$ Nusselt number at distance $x$ from the start of the plate

The reason these relations are useful is the definition's of [[convection heat transfer coefficient|Nusselt number]] and [[convection heat transfer coefficient|Stanton number]]. Since they contain $h$ we can solve for it!

When trying to find the heat transfer over a developing boundary layer's length, it's common to find mean [[convection heat transfer coefficient]].

> ### $$\begin{align*} \bar{h}  &= \frac{1}{L} \int^{L}_{0} h\: dx  \end{align*}$$
>> where:
>> $L=$ plate length
>> $\bar{h}=$ mean [[convection heat transfer coefficient]]
>> $h=$ [[convection heat transfer coefficient]]
>> $x=$ position along plate

### Example

![[Pasted image 20231210173302.png]]


Part b:
$$\begin{align*}
P &= \rho RT &&\to& \rho_{\infty} &= \frac{P_{\infty}}{R_{\infty}T_{\infty}}=2.42\:kg/m^{3}\\
\end{align*}$$


$$\begin{align*}
&& \text{Nu}&= \frac{hL}{k} \\
\text{Nu}_{x}&= 0.332\:\text{Re}_{x}^{\frac{1}{2}}\:\text{Pr}^{\frac{1}{3}} &&\to& \frac{h_{x}x}{k}&= 0.332\:\text{Re}_{x}^{\frac{1}{2}}\:\text{Pr}^{\frac{1}{3}} &&\to&
h_{x} &= 0.332k\:\frac{\rho U }{x\mu}^{\frac{1}{2}}\:\text{Pr}^{\frac{1}{3}}
\end{align*}$$

To find average heat transfer:

$$\begin{align*} 
\bar{h} &= \frac{1}{L}\int^{L}_{0} h\: dx &&\to&       \bar{h} &= \frac{1}{L}\int^{L}_{0} 0.332k\:\frac{\rho U }{x\mu}^{\frac{1}{2}}\:\text{Pr}^{\frac{1}{3}}\: dx 
 &&\to&       \bar{h} &= \frac{1}{L} 0.332k \frac{\rho U }{ \mu}^{\frac{1}{2}}  \text{Pr}^{\frac{1}{3}}\int^{L}_{0}\: x^{-\frac{1}{2}}\:\: dx 
 &&\to&       \bar{h} &=\frac{2}{L} 0.332k \frac{\rho U }{ \mu}^{\frac{1}{2}}  \text{Pr}^{\frac{1}{3}}  \left[ \sqrt x \right]^{L}_{0}\\
&&&&&&&&&&&&&= 39.74
\end{align*}$$

For one plate:

$$\begin{align*}
\dot{Q} &= \bar{h} A \:\Delta T =14.91W
\end{align*}$$
