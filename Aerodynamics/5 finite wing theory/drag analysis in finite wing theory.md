---
aliases: [""]
tags: []
---

## Drag analysis in finite wing theory

Well first we need to get an equation for drag coefficients, which is pretty easy:

$$\begin{align*}
C_{D} &= D_{Do} + C_{Di}
\end{align*}$$

We've got an [[general lift distrobution for a finite wing#Equations|equation for induced drag]] which can be subbed in, then we can get drag by multiplying by $\frac{1}{2}\rho V_{\infty}^{2}S$:

$$\begin{align*}
\frac{1}{2}\rho V_{\infty}^{2}S C_{D} &= \frac{1}{2}\rho V_{\infty}^{2}S (D_{Do} + C_{Di})  & C_{Di} &=  \frac{C_{L}^{2}}{\pi eA}\\
D &= \frac{1}{2}\rho V_{\infty}^{2}S \left(D_{Do} + \frac{C_{L}^{2}}{\pi eA }\right) \\
 &= \frac{1}{2}\rho V_{\infty}^{2}S \left(D_{Do} + \frac{L^{2}}{\pi eA } \frac{1}{ \left(\frac{1}{2}\rho V_{\infty}^{2}S\right)^{2} }\right) & W&= L \:(\text{steady level flight}) \\
&= \frac{1}{2}\rho V_{\infty}^{2}S D_{Do} + W^{2} \frac{1}{\frac{1}{2} \rho V_{\infty}^{2} S} \frac{1}{\pi eA}
\end{align*}$$

This equation shows us that the effect of [[induced drag coefficient|induced drag]] is inversely proportional to speed squared while the effect of [[profile drag coefficient|profile drag]] is proportional to speed squared. Meaning it's clear that induced drag's effect is significant during take off while profile drag is significant during landing:
![[Pasted image 20221222140544.png]]

