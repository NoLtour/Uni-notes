---
aliases: ["maxamising aircraft range","max breguet range speed"]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Maximising the breguet range (in the stratosphere)
### Introduction
We know that the [[Breguet range equation (jets)]] allows us to calculate aircraft range, but we can use maths to find how to get a maximum value for a given fuel load.

### Math time
![[Breguet range equation (jets)#^20c05c]]

So to maxamise range we need to maxamise $\frac{VL}{D}$, so lets start by getting an equation interms of that.

We know $T/\sigma=k$ from [[jet thrust variation in the stratosphere]]:

$$\begin{align*}
   T = D &= \frac{1}{2}\rho V^{2} S C_D\\
&  & T&=k\sigma & \rho&=\rho_0 \sigma\\
k\sigma &= \frac{1}{2}( \rho_0 \sigma ) V^{2} S C_D\\
\frac{2k}{S\rho_0 }  &=V^{2} C_D\\
\therefore V^{2}C_D&=constant\\
 \therefore V&\propto \frac{1}{\sqrt{C_D}} & \frac{C_L}{C_D}&=1 \\
\therefore \frac{VL}{D} &\propto \frac{1}{\sqrt{C_D}} \frac{C_L}{C_D} \\
\end{align*}$$

Now to find the value of $C_L$ that achieves max range we need to differentiate $\frac{1}{\sqrt{C_D}} \frac{C_L}{C_D}$ with respect to $C_L$, then make that equal 0 to get the turning point.
(if you have been paying attention $C_D$ is a function of $C_L$ so this is about to become a [[hahaha I am in pain|shitstorm]].

$$\begin{align*}
  \frac{1}{\sqrt{C_D}} \frac{C_L}{C_D} &= \dfrac{C_L}{C_D^{\frac{3}{2}}} & C_D &= C_{Do} + \dfrac{K(C_L)^{2}}{\pi A}\\
&= \dfrac{C_L}{(C_{Do} + \dfrac{K(C_L)^{2}}{\pi A})^{\frac{3}{2}}}\\
&= C_L (C_{Do} + \dfrac{ K}{\pi A}(C_L)^{2})^{-\frac{3}{2}}\\
\frac{d}{dC_L} \cdot \frac{1}{\sqrt{C_D}} \frac{C_L}{C_D} &= \frac{d}{dC_L} \cdot C_L (C_{Do} + \dfrac{ K}{\pi A}(C_L)^{2})^{-\frac{3}{2}}\\
&= \dfrac{{\pi}AC_{Do}-2KC_L^2}{{\pi}A\left(\frac{KC_L^2}{{\pi}A}+C_{Do}\right)^\frac{5}{2}}\\
let \: 0&= \dfrac{{\pi}AC_{Do}-2KC_L^2}{{\pi}A\left(\frac{KC_L^2}{{\pi}A}+C_{Do}\right)^\frac{5}{2}} \\
0&={\pi}AC_{Do}-2KC_L^2\\
 2KC_L^2&={\pi}AC_{Do}\\
 C_L^2&=\frac{{\pi}AC_{Do}}{2K}\\
 C_L&=\sqrt{\frac{{\pi}AC_{Do}}{2K}} & C_{L_{MD}} &= \sqrt{\frac{\pi AC_{Do}}{ K  } } \\
C_L &= \frac{C_{L_{MD}}}{\sqrt{2}}
\end{align*}$$

Here we used [[min drag lift coefficient in steady level flight]] to get $C_{L_{MD}}$

Since $V \propto \frac{1}{\sqrt{C_D}}$:
$$\begin{align*}
  V_{opt\:range}  &= \sqrt[4]{2} V_{MD}
\end{align*}$$

#### Subbing back for $(VL/D)_{max}$
$$\begin{align*}
(V\frac{C_L}{C_D})_{max}  &= & \sqrt\frac{2k}{S\rho_0 C_D}  &=V  & C_{L_{maxR}}&=\sqrt{\frac{{\pi}AC_{Do}}{2K}} & C_D &= C_{Do} + \dfrac{K(C_L)^{2}}{\pi A}\\
&=  \frac{\sqrt\frac{2k}{S\rho_0 C_D} \cdot \sqrt{\frac{{\pi}AC_{Do}}{2K}}}{C_D} & & & & & &= C_{Do} + \dfrac{K(\sqrt{\frac{{\pi}AC_{Do}}{2K}})^{2}}{\pi A}\\
&=  \frac{\sqrt\frac{2k{\pi}AC_{Do}}{S\rho_0 C_D2K} }  {C_D} & & & & & &= C_{Do} + \dfrac{K\pi AC_{Do}}{\pi A2K}\\
&=  \frac{\sqrt{\dfrac{ k}{\rho_0}\dfrac{{\pi}AC_{Do} }{ S C_DK}} }  {C_D} & & & & & &= C_{Do} + \dfrac{C_{Do}}{2}\\
&& & & & & &=\dfrac{3C_{Do}}{2}\\
&= \frac{\sqrt{\dfrac{ k}{\rho_0}\dfrac{{\pi}AC_{Do} }{ S \dfrac{3C_{Do}}{2} K}} }  {\dfrac{3C_{Do}}{2}}\\
&= \frac{2\sqrt{\dfrac{ k}{\rho_0}\dfrac{2{\pi}A }{ 3S  K}} }  {3C_{Do}}\\
&= \frac{2 }  {3C_{Do}}\cdot \sqrt{\dfrac{ k}{\rho_0}\dfrac{2{\pi}A }{ 3S  K}}\\
&= \frac{2 }  {3C_{Do}}\cdot \sqrt{\dfrac{ k}{\rho_0} \dfrac{2}{3S} \dfrac{{\pi}A }{  K}}
\end{align*}$$

#### Subbing back to get max range equation
Remember that $T/\sigma=k$ from [[jet thrust variation in the stratosphere|this]]

$$\begin{align*}
R_{max} =& \frac{1}{s} (V \frac{C_L}{C_D})_{max} \ln\left(1+\frac{W_f}{W_s}\right)\\
R_{max} =& \frac{1}{s} \frac{2 }  {3C_{Do}}\cdot \sqrt{\dfrac{ k}{\rho_0} \dfrac{2}{3S} \dfrac{{\pi}A }{  K}} \cdot \ln\left(1+\frac{W_f}{W_s}\right)\\
\end{align*}$$

### Implications

> ### $$R_{max} = \frac{1}{s} \frac{2 }  {3C_{Do}}\cdot \sqrt{\dfrac{ k}{\rho_0} \dfrac{2}{3S} \dfrac{{\pi}A }{  K}} \cdot \ln\left(1+\frac{W_f}{W_s}\right)$$ 
>> where:
>> $S=$ [[Wing plan area|Gross wing area]] 
>> $s=$ [[specific fuel consumption (aircraft)|s.f.c]]
>> $C_{Do}=$ [[profile drag coefficient]]
>> $k=$  [[jet thrust variation in the stratosphere|constant from this]]
>> $\rho_0=$ [[International Standard Atmosphere|Sea level air density]]
>> $A=$ [[wing aspect ratio]]
>> $K=$ [[induced drag coefficient#^fce277|Constant related to wing shape]]
>> $me=$ [[in pain]]
>> $\ln\left(1+\frac{W_f}{W_s}\right)=\ln\left(\frac{W_1}{W_2}\right)$

> ### $$ V_{opt\:range} = \sqrt[4]{2} V_{MD} \approx 1.189 V_{MD} $$ 
>> where:
>> $V_{opt\:range}=$ speed that offers the optimum range
>> $V_{MD}=$ [[min drag speed in steady level flight|min drag speed]]

$V_{MD}$ varies with altitude so $V_{opt\:range}$ will also do so, this has further implications when you consider that some [[cruise pattern|cruise climb techniques]] change altitudes. So a truely optimum flight path is one at this optimum speed at as high an altitude possible.

[[aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaah|this took me a day to finish, all these notes... it's so annoying how unlinked everything in my refrence material is! Cool off with mememes]]
