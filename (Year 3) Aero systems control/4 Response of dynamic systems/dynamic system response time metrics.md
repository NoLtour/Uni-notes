---
aliases: ["rise time","peak time","maximum overshoot","settling time"]
tags: []
---

## Dynamic system response time metrics

### Defs

![[Pasted image 20231030144046.png]]

#### Rise time ($T_{r}$)

The time for the response to reach (a certain percentage of) the steady state value.

#### Peak time ($T_{p}$)

The time for the response to rise to the first peak.

#### Maximum overshoot ($PO$)

The maximum percentage of the response above the steady state value.

It is often given as a percentage:

> ### $$\begin{align*} PO  &= \frac{c_{max}-c_{min}}{c_{final}} \times 100  \end{align*}$$
>> where:
>> $PO=$ maximum overshoot
>> $c_{max}=$ the maximum response of the response function
>> $c_{min}=$ the minimum response of the response function (often $\left.c(t)\right|_{t=0}=c_{min}$)
>> $c_{final}=$ the response at equilibrium ($\lim_{t \to \infty} c(t)=c_{final}$)

#### Settling time ($T_{s}$)

The time for the response to reach and stay within a range of the final value (e.g. 2%, 5%).


### Applied

![[Pasted image 20231030144046.png]]

Taking a second order system and applying a step response will produce the oscillatory motion seen above. A valid representation of this is as follows:

$$\begin{align*}
c(t) &= 1 - \frac{1}{\sqrt{1-\zeta^{2}}}e^{-\zeta\omega_{n}t} \sin \left(\omega_{n} t\sqrt{1 - \zeta^{2}} + \arctan \frac{\sqrt{1-\zeta^{2}}}{\zeta} \right)
\end{align*}$$

We'll now use this as our equation for getting each of these metrics from.

#### Peak overshoot

Not so hard, just find where $dc/dt=0$ and then take the first occurance above zero. This looks daunting, till you realise that $\zeta$ and $\omega_{n}$ are constants. Going to skip over most of it:

$$\begin{align*}
c(t) &= 1 - \frac{1}{\sqrt{1-\zeta^{2}}}e^{-\zeta\omega_{n}t} \sin \left(\omega_{n} t\sqrt{1 - \zeta^{2}} + \arctan \frac{\sqrt{1-\zeta^{2}}}{\zeta} \right) \\
&\downarrow\: \text{ Find } \frac{dc}{dx}=0 \text{, then rearrange}\\
\frac{\sqrt{{1-\zeta^{2}}}}{\zeta} &= \tan\left( \omega_{n}t\sqrt{1-\zeta^{2}} +\arctan\frac{\sqrt{1-\zeta^{2}}}{\zeta} \right)\\
&\downarrow\: \text{ Solve for }t\\
t &= \frac{n\pi}{\omega_{n}\sqrt{1-\zeta^{2}}} \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\: n=1,3,5 ...
\end{align*}$$

After considering that we only care about $n=1$ (first peak), peak time will be:
$$\begin{align*}
T_{p} &= \frac{\pi}{\omega_{n}\sqrt{1-\zeta^{2}}} = \frac{\pi}{\omega_{t}}
\end{align*}$$

We need to get all the things for peak overshoot:

$$\begin{align*}
PO  &= \frac{c_{max}-c_{min}}{c_{final}} \times 100 
\end{align*}$$

 

First $c_{max}$:


$$\begin{align*}  
c(T_{p}) &= 1 - \frac{1}{\sqrt{1-\zeta^{2}}}e^{-\zeta\omega_{n}\frac{\pi}{\omega_{n}\sqrt{1-\zeta^{2}}}} \sin \left(\omega_{n} \frac{\pi}{\omega_{n}\sqrt{1-\zeta^{2}}}\sqrt{1 - \zeta^{2}} + \arctan \frac{\sqrt{1-\zeta^{2}}}{\zeta} \right) \\
c_{max} &= 1 - \frac{1}{\sqrt{1-\zeta^{2}}}e^{-\zeta \frac{\pi}{ \sqrt{1-\zeta^{2}}}} \sin \left(   \pi  + \arctan \frac{\sqrt{1-\zeta^{2}}}{\zeta} \right) \\
\end{align*}$$

Then $c_{min}$:

$$\begin{align*}  
c(0) &= 1 - \frac{1}{\sqrt{1-\zeta^{2}}}e^{-\zeta\omega_{n}0} \sin \left(\omega_{n} 0\sqrt{1 - \zeta^{2}} + \arctan \frac{\sqrt{1-\zeta^{2}}}{\zeta} \right)  \\
c_{min} &= 1 - \frac{1}{\sqrt{1-\zeta^{2}}} \sin \left(\arctan \frac{\sqrt{1-\zeta^{2}}}{\zeta} \right)  \\
 &= 1-1\\
&= 0  \\

\end{align*}$$

Then $c_{total}$:
$$\begin{align*}  
\lim_{t\to\infty} c(t) &= 1 - \frac{1}{\sqrt{1-\zeta^{2}}}e^{-\zeta\omega_{n}t} \sin \left(\omega_{n} t\sqrt{1 - \zeta^{2}} + \arctan \frac{\sqrt{1-\zeta^{2}}}{\zeta} \right)  \\
c_{total} &= 1 - \frac{1}{\sqrt{1-\zeta^{2}}} \\

\end{align*}$$

Finally:

$$\begin{align*}
PO  &= \frac{c_{max}-c_{min}}{c_{final}} \times 100 & &\to & PO  &= \frac{1 - \frac{1}{\sqrt{1-\zeta^{2}}}e^{-\zeta \frac{\pi}{ \sqrt{1-\zeta^{2}}}} \sin \left(   \pi  + \arctan \frac{\sqrt{1-\zeta^{2}}}{\zeta} \right) }{ 1 - \frac{1}{\sqrt{1-\zeta^{2}}}} \times 100 
\end{align*}$$

Ok so just simplify that. I [[it is just that easy|did it in my head]], got this:

$$\begin{align*}
PO &= 100 \exp \left(- \frac{\pi\zeta}{\sqrt{1-\zeta^{2}}}\right)
\end{align*}$$

Easy.

#### Settling time

That can be suitably found after 4 time steps:

$$\begin{align*}
 c(T_{s})=c(4T) &\approx 4\%\text{ of fianl value}
\end{align*}$$

Here:
$$\begin{align*}
T=\frac{1}{\zeta \omega_{n}}
\end{align*}$$

#### Rise time

This is actually REALLY hard analytically, for this case it comes out as about:

$$\begin{align*}
T_{r} &= \frac{1.8}{\omega_{n}}
\end{align*}$$

This is a conservative estimate.
