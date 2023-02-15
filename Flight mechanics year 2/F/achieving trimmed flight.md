---
aliases: [""]
tags: []
---

## Achieving trimmed flight

This was done in year 1 [[Basic aircraft trimming|trimmed flight]], but this is the year 2 [[shortened version of version|ver]] which has slightly different symbols used n stuff.

![[Pasted image 20230215192133.png]]

This diagram is the starting point, but we'll simplify it a lot using the following assumptions:
- Small angle of attack, so $T,D,D_{T},W\sin(\gamma)$ are all in the same axis
- Along that axis the forces balance $\sum\limits F_{x}=0$ or $T = D+D_{T} + W\sin \gamma$
- The tail plane is small and symmetrical such that the moment around it's quarter chord is zero $M_{T_{0}}=0$
- The moments caused by thrust, drag and tail drag are small relative to other moments such that they can be negated

Putting all that into a diagram:

![[Pasted image 20230215192908.png]]

Now we just need to find [[Basic aircraft trimming|trimmed flight]], aka $\sum\limits M=0$. Here we take moments about the centre of gravity:
$$\begin{align*}
M_{0} + L(h-h_{0})c - L_{T}(l - (h-h_{0})c) &= 0 & &\to & M_{0} + (L+L_{T})(h-h_{0})c - L_{T} l &= 0\\
\end{align*}$$

Assuming steady flight we also know that:
$$\begin{align*}
L* &= W\cos\gamma\\
L+L_{T} &= 
\end{align*}$$

Everything can be non dimensionalised then subbed back into the equations above to get more useful identities:

$$\begin{align*}
&L* & &\to & L* &= C_{L*} \frac{1}{2}\rho V^{2} S\\
&L & &\to & L &= C_{L} \frac{1}{2}\rho V^{2} S\\
&W & &\to & W &= C_{W} \frac{1}{2}\rho V^{2} S\\
&L_{T} & &\to & L_{T} &= C_{L_{T}} \frac{1}{2}\rho V^{2} S_{T}= C_{L_{T}} \frac{1}{2}\rho V^{2} S \frac{S_{T}}{S}\\
&M_{0} & &\to & M_{0} &= C_{M_{0}} \frac{1}{2}\rho V^{2} Sc\\
\end{align*}$$

Note that for $L*$ the reason we use $S$ and not $S+S_{T}$ is just because it makes the maths easier and often $S>>S_{T}$, we can non dimensionalise with any arbitrary area so it just makes sense to do it this way. Then subbing these into the moment and force balance equations:
$$\begin{align*}
 M_{0} + (L+L_{T})(h-h_{0})c - L_{T} l &= 0 & L+L_{T} &= W\cos\gamma\\
C_{M_{0}} \frac{1}{2}\rho V^{2} Sc + \left(C_{L} \frac{1}{2}\rho V^{2} S+C_{L_{T}} \frac{1}{2}\rho V^{2} S \frac{S_{T}}{S}\right)(h-h_{0})c - C_{L_{T}} \frac{1}{2}\rho V^{2} S \frac{S_{T}}{S} l &= 0 & C_{L} \frac{1}{2}\rho V^{2} S+C_{L_{T}} \frac{1}{2}\rho V^{2} S \frac{S_{T}}{S} &= C_{W} \frac{1}{2}\rho V^{2} S\cos\gamma\\
C_{M_{0}} + C_{L*} ( h - h_{0} ) - C_{L_{T}} K &= 0 & C_{L*} &= C_{L} + C_{L_{T}} \frac{S_{T}}{S} = C_{W}\cos\gamma
\end{align*}$$

Here we've introduced the variable $K$ known as [[tail volume fraction]].
