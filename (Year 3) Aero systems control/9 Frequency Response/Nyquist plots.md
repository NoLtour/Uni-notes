---
aliases: [""]
tags: []
---

## Nyquist plots

These aren't so bad, basically it's just a plot of how magnitude and phase shift correlate as you vary the angular frequency. If that sounded like exactly what a [[simple bode plots|bode plot]] is, well that's because it displays the same* information! The difference is it combines both [[simple bode plots|bode plots]] into a single one, using a polar axis:

![[Pasted image 20231209204435.png]]

Here this graph was constructed by taking a sample at $\omega=0$ from the [[simple bode plots|bode plots]], getting the phase to use as the angle and the magnitude amplification to use as length. Then repeat this over $-\infty<\omega<\infty$... of course since bode plots tend to just reach some limit, we don't need to go to infinity.

[[because my format is a universal standard|Formally]]:

> $$\:$$
> ### $$\begin{align*} \text{plot}_{N}(\alpha, r)  &= r ( j\sin\alpha + \cos\alpha )  \end{align*}$$
> ### $$\begin{align*} \alpha(\omega) &=\angle F(\omega) =\phi(\omega) &&& r(\omega) &= |F(\omega)|= 10^{M(\omega)/20}\end{align*}$$
>> where:
>> $\alpha,r=$ polar coordinates for plotting
>> $\phi(\omega)=$ phase shift as a function of frequency
>> $M(\omega)=$ gain in $dB$ as a function of frequency
>> $F(\omega)=$ the thing being [[simple bode plots|bode plotted]]

Something important to note is these plots are symmetric about the real axis, and they have a direction which MUST be annotated!


