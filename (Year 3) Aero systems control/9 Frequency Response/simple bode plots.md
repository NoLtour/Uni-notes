---
aliases: [""]
tags: []
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

#### Integrators $\left(F=\frac{1}{(j\omega)^{n}}\right)$

$$\begin{align*}
&&F &= \frac{1}{(j\omega)^{n}} \\
M &= 20\log_{10}|F| & &\to & M &= 20\log_{10}\left| \frac{1}{(j\omega)^{n}} \right|\\
\phi &= \angle F& &\to & \phi &= 20\log_{10}|F|\\
\end{align*}$$
