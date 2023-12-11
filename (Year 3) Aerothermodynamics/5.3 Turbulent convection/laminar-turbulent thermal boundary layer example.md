---
aliases: [""]
tags: []
---

## Laminar-turbulent thermal boundary layer example

![[Pasted image 20231211014550.png]]

##### Assuming that the flow turns turbulant at $x=7.5cm$, what is $\bar{h}$?

Firstly, the laminar part is just what was done previously in [[convection heat transfer coefficient#Example]]:

$$\begin{align*}
P &= \rho RT &&\to& \rho_{\infty} &= \frac{P_{\infty}}{R_{\infty}T_{\infty}}=2.42\:kg/m^{3}\\
\end{align*}$$


$$\begin{align*}
&& \text{Nu}&= \frac{hL}{k} \\
\text{Nu}_{x}&= 0.332\:\text{Re}_{x}^{\frac{1}{2}}\:\text{Pr}^{\frac{1}{3}} &&\to& \frac{h_{x}x}{k}&= 0.332\:\text{Re}_{x}^{\frac{1}{2}}\:\text{Pr}^{\frac{1}{3}} &&\to&
h_{x} &= 0.332k\:\frac{\rho U }{x\mu}^{\frac{1}{2}}\:\text{Pr}^{\frac{1}{3}}
\end{align*}$$

To find average laminar heat transfer:

$$\begin{align*} 
\bar{h}_l &= \frac{1}{0.5L}\int^{0.5L}_{0} h\: dx &&\to&       \bar{h}_l &= \frac{1}{L}\int^{0.5L}_{0} 0.332k\:\frac{\rho U }{x\mu}^{\frac{1}{2}}\:\text{Pr}^{\frac{1}{3}}\: dx 
 &&\to&       \bar{h}_l &= \frac{1}{0.5L} 0.332k \frac{\rho U }{ \mu}^{\frac{1}{2}}  \text{Pr}^{\frac{1}{3}}\int^{0.5L}_{0}\: x^{-\frac{1}{2}}\:\: dx 
 &&\to&       \bar{h}_l &=\frac{4}{L} 0.332k \frac{\rho U }{ \mu}^{\frac{1}{2}}  \text{Pr}^{\frac{1}{3}}  \left[ \sqrt x \right]^{0.5L}_{0}\\
&&&&&&&&&&&&&= 56.19
\end{align*}$$




Note that the formula for laminar and boundary layer thickness is different in this module, compared to aero (because [[why should it be explained|fuck you]]). The equations for boundary layer thickness in the laminar and turbulant cases are:

$$\begin{align*}
\delta_{l} &= \frac{5x}{\text{Re}^{0.5}} & \delta_{t} &= \frac{0.37x}{\text{Re}^{0.2}} \\
\delta_{l} &= \frac{5x}{\left(\frac{\rho x U_{\infty}}{ \mu}\right)^{0.5}} & \delta_{t} &= \frac{0.37x}{\left(\frac{\rho x U_{\infty}}{ \mu}\right)^{0.2}} \\
\delta_{l,x} &= 5\frac{\mu}{\rho U_{\infty}}^{0.5} x^{0.5} & \delta_{t,x} &= 0.37\frac{\mu}{\rho U_{\infty}}^{0.2} x^{0.8}\\
\end{align*}$$

The boundary layer thickness at the transition point will be:
$$\begin{align*}
\delta_{l,m} &= 5\frac{\mu}{\rho U_{\infty}}^{0.5} 0.075^{0.5} =1.313\:mm\\
\delta_{t,m} &= 0.37\frac{\mu}{\rho U_{\infty}}^{0.2} 0.075^{0.8} =2.89\:mm
\end{align*}$$
Then the true thickness from that point on would be:

$$\begin{align*}
\delta_{T,x} &= (\delta_{l,m} - \delta_{t,m}) + \delta_{t,x}\\
&=  -0.001577 + 0.37\frac{\mu}{\rho U_{\infty}}^{0.2} x^{0.8}
\end{align*}$$


This may be needed if the question asked about boundary layer thickness, note it's different from what we learned from last year aerodynamics ([[calculating drag across a plate with a transition region]])

Then calculating the turbulant convection coefficient:


$$\begin{align*}
&& \text{Nu}&= \frac{hL}{k} \\
\text{Nu}_{x}&= 0.0296\:\text{Re}_{x}^{\frac{4}{5}}\:\text{Pr}^{\frac{1}{3}} &&\to& \frac{h_{x}x}{k}&= 0.0296\:\text{Re}_{x}^{\frac{4}{5}}\:\text{Pr}^{\frac{1}{3}} &&\to&
h_{x} &= 0.0296\: \frac{k}{x} \left(\frac{\rho x U_{\infty}}{ \mu}\right)^{\frac{4}{5}}\:\text{Pr}^{\frac{1}{3}} &&\to&
h_{x} &= 0.0296\: k \left(\frac{\rho  U_{\infty}}{ \mu}\right)^{\frac{4}{5}}\:\text{Pr}^{\frac{1}{3}} x^{-\frac{1}{5}}
\end{align*}$$

$$\begin{align*} 
\bar{h}_t &= \frac{1}{0.5L}\int^{L}_{0.5L} h\: dx &&\to&    
\bar{h}_t &= \frac{2}{L} 0.0296\: k \left(\frac{\rho  U_{\infty}}{ \mu}\right)^{\frac{4}{5}}\:\text{Pr}^{\frac{1}{3}} \int^{L}_{0.5L}   x^{-\frac{1}{5}} dx &&\to&       
\bar{h}_t &= \frac{2}{L} 0.0296\: k \left(\frac{\rho  U_{\infty}}{ \mu}\right)^{\frac{4}{5}}\:\text{Pr}^{\frac{1}{3}} \left[ \frac{5}{4} x^{\frac{4}{5}}\right]^{L}_{0.5L} \\
&&&&&&&&&=        69

 
\end{align*}$$

So then to total average will be:

$$\begin{align*}
\bar{h} &= \frac{\bar{h}_{t} + \bar{h}_{l}}{2}=62.59
\end{align*}$$

Note the discontinuity in the [[convection heat transfer coefficient]]:

![[Pasted image 20231211203428.png]]

At the moment of transition there is a sudden increase in heat transfer, which makes sense considering turbulant boundary layers have better flow mixing and at this point the thickness is the same. It should be noted that the graph would be more natural in a real case, since we are ignoring the [[features of the boundary layer|complex transition region]].

