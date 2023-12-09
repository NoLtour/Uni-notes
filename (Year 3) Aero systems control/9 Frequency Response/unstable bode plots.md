---
aliases: [""]
tags: []
---

## Unstable bode plots

If we take the [[sinusoidal loop gain function factors|simple lag]] case in [[simple bode plots]] examples:

![[simple bode plots#Simple lag and lead $ left(F= frac{1}{j omega T_{i} + 1} right)$]]

Then we can clearly see that the root is positive, hence stable.  What happens if the sign is flipped and it's unstable?
$$\begin{align*}
&&F &= \frac{1}{j\omega T_{i} - 1} \\
M &= 20\log_{10}|F| & &\to & M &= 20\log_{10}\left|\frac{1}{j\omega T_{i} - 1} \right|   & &\to &   M  &= 20\log_{10}\frac{1}{ \sqrt{ \omega^{2} T_{i}^{2} + 1} }     & &\to &   
&\begin{aligned} 
\left.M\right|_{\omega\to0} &=  20\log_{10}\frac{1}{ \sqrt{ (\to0) + 1} }=  20\log_{10} (\to1)=  0 \\
\left.M\right|_{\omega\to\infty} &=  20\log_{10}\frac{1}{ \sqrt{ (\to\infty) + 1} }=  -20\log_{10} (\to0)=  -\infty \\
\left.M\right|_{\omega T_{1}=1} &=  20\log_{10}\frac{1}{ \sqrt{ 1 + 1} }=  20\log_{10} \frac{1}{\sqrt2}= -0.1505\approx0 \\
\end{aligned}
\\\\
\\
\phi &= \angle F & &\to & \phi &=  \angle \frac{1}{j\omega T_{i} - 1}  & &\to & &   & &  & 
&\begin{aligned} 
\left.\phi\right|_{\omega\to0} &= \angle \frac{1}{j(\to0) T_{i} - 1} = \angle (\to-1) =-180\degree \\ 
\left.\phi\right|_{\omega\to\infty} &= \angle \frac{1}{j(\to\infty) T_{i} - 1} = \angle \left(\to \frac{1}{j}\right) =-90\degree \\ 
\left.\phi\right|_{\omega T_{1}=1} &= \angle \frac{1}{j - 1} =\angle \frac{j+1}{- 2} = -135\degree \\ 
\end{aligned}
\end{align*}$$

So there is no magnitude change, but the phase plot clearly changes!

