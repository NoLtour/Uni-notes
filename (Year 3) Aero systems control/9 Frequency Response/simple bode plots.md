---
aliases:
  - bode plots
tags:
---

## Simple bode plots

### Intro

It's best to just give examples, but essentially bode plots are just plotting the gain and phase shift of some function over a frequency range, making use of the following:

> ### $$\begin{align*} M(j\omega) &= 20\log_{10} |F(j\omega)|  \end{align*}$$
> ### $$ \phi(j\omega)=\angle F(j\omega) $$
>> where:
>> $M(j\omega)=$ The magnitude of $F(j\omega)$ in [[the decibel|dB]], note that it's a function of frequency
>> $\phi(j\omega)=$ The phase of $F(j\omega)$, note that it's a function of frequency
>> $F(j\omega)=$ The function being computed, in this module it would be one of the [[sinusoidal loop gain function factors]]

As previously eluded to, transfer functions can impart phase and amplitude changes. In reality these changes depend on the frequency input, hence the need to [[much more of an approximate sketch though|plot em]].

### Bode plots for [[sinusoidal loop gain function factors|gain factors]]
#### Simple gain ($F=K$)

This is trivial, if we have some input sinusoidal wave then after applying a gain:
- The amplitude will increase 
- The phase will not change

Take a gain of $K=10$ and $K=2$ then:
$$\begin{align*}
M &= 20\log_{10}|F|= 20\log_{10}K & &\to & M &= 20\log_{10}2 =6.02\:dB\\
&& && M &= 20\log_{10}10=20\:dB
\end{align*}$$
$$\begin{align*}
 \phi &= \angle F= \angle K=0
\end{align*}$$

Now consider how does gain this change with frequency? Obviously it doesn't, the plots simple, just a flat line. 

Then consider the plot of phase change with frequency, it of course is just zero for everything!

![[Pasted image 20231208200027.png]]

#### Integrators and differentiators $\left(F=\frac{1}{(j\omega)^{n}}\right)$

Subbing the [[sinusoidal loop gain function factors|integrator]] function into the equations to get $M$ and $\phi$:

$$\begin{align*}
&&F &= \frac{1}{(j\omega)^{n}} \\
M &= 20\log_{10}|F| & &\to & M &= 20\log_{10}\left| \frac{1}{(j\omega)^{n}} \right| & &\to & M &= -n20\log_{10}\left| j\omega \right|& &\to & &M = -20n\log_{10}\left|  \omega \right| \\
\phi &= \angle F & &\to & \phi &=  \angle \frac{1}{(j\omega)^{n}}  & &\to & \phi &=  \angle j^{-n}  & &\to &
&\begin{aligned} 
\phi &=  \angle j^{-0} =0\degree\\
\phi &=  \angle j^{-1} =-90\degree\\
\phi &=  \angle j^{-2} =-180\degree\\
\phi &=  \angle j^{-3} =-270\degree\\
\phi &=  \angle j^{-4} =0\degree\\
&...\\
\end{aligned}
  \\
\end{align*}$$

Note that if $n$ is negative then we get a [[sinusoidal loop gain function factors|differentiator]] $\left(\frac{1}{(\omega j)^{-n}}\right) = (\omega j)^{n}$, which means that the $M$ gradient flips and the direction of rotation flips.

![[Pasted image 20231209115556.png]]

### Simple lag and lead $\left(F= \frac{1}{j\omega T_{i} + 1}\right)$

Here we take [[sinusoidal loop gain function factors|simple lag]]:

$$\begin{align*}
&&F &= \frac{1}{j\omega T_{i} + 1} \\
M &= 20\log_{10}|F| & &\to & M &= 20\log_{10}\left|\frac{1}{j\omega T_{i} + 1} \right|   & &\to &   M  &= 20\log_{10}\frac{1}{ \sqrt{ \omega^{2} T_{i}^{2} + 1} }     & &\to &   
&\begin{aligned} 
\left.M\right|_{\omega\to0} &=  20\log_{10}\frac{1}{ \sqrt{ (\to0) + 1} }=  20\log_{10} (\to1)=  0 \\
\left.M\right|_{\omega\to\infty} &=  20\log_{10}\frac{1}{ \sqrt{ (\to\infty) + 1} }=  -20\log_{10} (\to0)=  -\infty \\
\left.M\right|_{\omega T_{1}=1} &=  20\log_{10}\frac{1}{ \sqrt{ 1 + 1} }=  20\log_{10} \frac{1}{\sqrt2}= -0.1505\approx0 \\
\end{aligned}
\\\\
\\
\phi &= \angle F & &\to & \phi &=  \angle \frac{1}{j\omega T_{i} + 1}  & &\to & &   & &  & 
&\begin{aligned} 
\left.\phi\right|_{\omega\to0} &= \angle \frac{1}{j(\to0) T_{i} + 1} = \angle (\to1) =0\degree \\ 
\left.\phi\right|_{\omega\to\infty} &= \angle \frac{1}{j(\to\infty) T_{i} + 1} = \angle \left(\to \frac{1}{j}\right) =-90\degree \\ 
\left.\phi\right|_{\omega T_{1}=1} &= \angle \frac{1}{j  + 1} = -45\degree \\ 
\end{aligned}
\end{align*}$$

Note that we assumed $T=1$, different values of $T$ would change the location where the $45\degree$ occurs away from $\omega=1$. Plotting this:

![[Pasted image 20231209122745.png]]

Here the blue line is exact, but if you need to sketch this then we use the red line. There are a few key lessons, for a [[sinusoidal loop gain function factors|simple lag]]:
- The [[linear system sinusoidal response|sinusoidal gain]] is zero until $\omega T=1$ at which point it decreases by $20\:dB/\text{decade}$ 
- The [[linear system sinusoidal response|sinusoidal phase shift]] is zero until a decade before $\omega T=1$, where it head's down to $-90\degree$ 2 decades later

I [[as long as the link works lol|proved]] that the $T$ determines where that inflection occurs on desmos https://www.desmos.com/calculator/jecms8rbsy and https://www.desmos.com/calculator/8op3d1hajv

In the case of [[sinusoidal loop gain function factors|simple lead]] the equation flips to $F= j\omega T_{i} + 1$, this flips the $\phi$ about $\phi=0$ and flips $M$ about $M=0$. Becoming obvious when you realise:
$$\begin{align*}
M &= 20\log_{10}\left|F \right|  \\
M &= 20\log_{10}\left| \frac{1}{F} \right| = -20\log|F|
\end{align*}$$

### Quadratic lag $\left(F=\frac{1}{\left(\frac{j\omega}{\omega_{n}}\right)^{2} + 2 \zeta  \frac{j\omega}{\omega_{n}} + 1}\right)$

$$\begin{align*}
&&F &=\frac{1}{\left(\frac{j\omega}{\omega_{n}}\right)^{2} + 2 \zeta  \frac{j\omega}{\omega_{n}} + 1} \\
M &= 20\log_{10}|F| & &\to & M &= 20\log_{10}\left| \frac{1}{\left(\frac{j\omega}{\omega_{n}}\right)^{2} + 2 \zeta  \frac{j\omega}{\omega_{n}} + 1} \right|   & &\to &   
M &= -20\log_{10}  \sqrt{ \left(1-\frac{\omega^{2}}{\omega_{n}^{2}}\right)^{2} + \left(\frac{2\zeta\omega}{\omega_{n}}\right)^{2} } 
     & &\to &   
&\begin{aligned} 
\left.M\right|_{\omega\to0} &=...=  0 \\
\left.M\right|_{\omega\to\infty} &= ...= - \infty \\
\left.M\right|_{\omega W=1} &=...\approx0ish \:\zeta\text{ dependent} \\
\end{aligned}
\\\\
\\
\phi &= \angle F & &\to & \phi &=  \angle \frac{1}{\left(\frac{j\omega}{\omega_{n}}\right)^{2} + 2 \zeta  \frac{j\omega}{\omega_{n}} + 1}  & &\to & &   & &  & 
&\begin{aligned} 
\left.\phi\right|_{\omega\to0} &=... =0\degree \\ 
\left.\phi\right|_{\omega\to\infty} &=... =-180\degree \\ 
\left.\phi\right|_{\omega \omega_{n}=1} &=... =-90\degree \\ 
\end{aligned}
\end{align*}$$


![[Pasted image 20231209131324.png]]

The graph for this one is more complex, but the main thing is that the only factor that contributes to shifting the rotation point is adjusting $\omega_{n}$, "[[these interactive things are really nice|proved]]" here https://www.desmos.com/calculator/gki7dvnpow.

Changing damping factor only shift's the peak up/down.
- The [[linear system sinusoidal response|sinusoidal gain]] is zero until $\omega \omega_{n}=1$ at which point it decreases by $40\:dB/\text{decade}$ 
- The [[linear system sinusoidal response|sinusoidal phase shift]] is zero until a decade before $\omega \omega_{n}=1$, where it head's down to $-180\degree$ 2 decades later

Quadratic lead is similar but with lot's of thing's flipped.
