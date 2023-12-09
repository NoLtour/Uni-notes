---
aliases: [""]
tags: []
---

## Complex bode plots

### Plot summation

In [[simple bode plots]] we demonstrated how to make [[simple bode plots|bode plots]] for [[sinusoidal loop gain function factors]]. So how would we find the plot for something like:

$$\begin{align*}
F &= \frac{1}{(T_{1}s+1)(T_{2}s+1)}
\end{align*}$$

This is clearly just 2 [[sinusoidal loop gain function factors|simple lag]]s. It can actually be factorised into them, and we can just sum up their contributions to get the "total" plot:

$$\begin{align*}
F &= \frac{1}{(T_{1}s+1)(T_{2}s+1)} &&\to& F &= \frac{1}{T_{1}s+1} \frac{1}{T_{2}s+1}
\end{align*}$$

Of course it is also possible to go the traditional route and calculate the outcome for each frequency, but that is not practical during an exam! Though it is recommended to use limit's ($0,\infty,1$) to check correspondence.

> ### $$\begin{align*}   G_{c}GH  &=  \frac{K}{(j\omega)^{n}} \frac{S_{1}S_{2}...\:Q_{1}Q_{2}...}{S_{k+1} S_{k+2} ...\: Q_{l+1} Q_{l+2}...} = K \cdot \frac{1}{(j\omega)^{n}}  \cdot S_{1}  \cdot S_{2} \cdot \:...\:  \cdot Q_{1}  \cdot Q_{2} \cdot \:...\: \cdot \frac{1}{S_{k+1}}  \cdot \frac{1}{S_{k+2}} \cdot \:...\: \cdot \frac{1}{Q_{l+1}} \cdot \frac{1}{Q_{l+2}} \cdot \:... \end{align*}$$
> ### $$\begin{align*} \text{Bode}(G_{c}GH) &= \sum\limits\text{Bode}(\text{Factors}) \end{align*}$$

The final plot is then useful for determining stability ([[bode plot stability criteria]]).

### Example $F= \frac{4}{(2s+1)(0.2s+1)}$

Looking at the function, it's got 3 components a [[sinusoidal loop gain function factors|gain]] and 2 [[sinusoidal loop gain function factors|simple lag]]s:

$$\begin{align*}
 &\frac{4}{(2s+1)(0.2s+1)} &&\to& K \frac{1}{T_{1}s+1}\frac{1}{T_{2}s+1} &&\to& K \frac{1}{S_{k+1}}\frac{1}{S_{k+2}}
\end{align*}$$

Using what we know from [[simple bode plots]] we know that the gain plot will be made up of the components:

Gain with $K=4$, this will not contribute to the phase plot, but does lead to a gain increase of $20\log_{10}4=12.04$

The approximation for where the phase change is half complete for [[sinusoidal loop gain function factors|simple lag]]s is:
$$\begin{align*}
\omega_{s} &= \frac{1}{T}
\end{align*}$$
$$\begin{align*}
\omega_{s1} &= \frac{1}{2}=0.5 & \omega_{s2} &= \frac{1}{0.2} =5
\end{align*}$$
We know from [[simple bode plots]] that this change can be approximated as a linear gradient reducing the phase by $90\degree$ over the course of 2 decades, the magnitude drop occurs at a steady rate of $20\:dB/decade$ one decade after $\omega_{s}$. Plotted this results in:

![[Pasted image 20231209170002.png]]

Here we see the green line is the sum of all the individual components.

### Example PI controller

Here's the [[PID controller|PI controller]]:

$$\begin{align*}
G_{c} &= K_{p} + \frac{K_{i}}{s} = 0.25 + \frac{2}{s}
\end{align*}$$

First we rearrange it into a more standard form:

$$\begin{align*}
&0.25 + \frac{2}{s} & &\to & & 2\:\frac{\frac{1}{8} s+1}{s} & &\to & & 2\cdot\left(\frac{1}{8} s+1\right)\cdot\frac{1}{s}
\end{align*}$$

Now we can see it's made of 3 components:
- Gain $K=2$
- [[sinusoidal loop gain function factors|Simple lead]] $T_{1}= \frac{1}{8}$
- [[sinusoidal loop gain function factors|A Integrator]] $n=1$ 

The gain's plot is easy, just a gain of $20\log_{10}2=6.02$ and no phase change.

The simple lead has a inflection frequency of $1/T_{1}=1/(1/8)=8$, at which point:
- Gain will start to increase by $20\:dB/decade$
- Phase will be half way through increasing to $90\degree$ from zero

Then the integrator can be figured out from [[simple bode plots]]:
- It's got a constant gain of $-20\:dB/decade$, being zero at $\omega=1$
- It's got a constant phase shift of $-90\degree$

![[Pasted image 20231209175006.png]]

### Example simple lead, lag

Here the function is:

$$\begin{align*}
F &= \frac{s+0.5}{0.25s+2}
\end{align*}$$

This can be rearranged and factorised:

$$\begin{align*}
\frac{s+0.5}{0.25s+2}&  & &\to &  0.25\frac{2s+1}{0.125s+1}&   & &\to &  0.25\cdot(2s+1)\cdot\frac{1}{0.125s+1}&  
\end{align*}$$

Which makes it obvious that this is a gain, simple lead and simple lag. Getting the important features is easy

$$\begin{align*}
\text{Gain magnitude:}&&20\log_{10}0.25 &\approx -12 \\
\text{Lead freq:}&& \frac{1}{T_{lead}}=\frac{1}{0.5}&= 2 \\
\text{Lag freq:}&& \frac{1}{T_{lag}}=\frac{1}{0.125}&= 8 \\
\end{align*}$$

A faster layout for determining the state of the graphs is as follows:

$$\begin{align*} 
\begin{matrix}
             & K && S_{lead} && S_{lag} \\
\phi_{init}= & 0\degree &+& 0\degree &+& 0\degree & =0\degree\\
\phi_{final}= & 0\degree &+& 90\degree &+& -90\degree & =0\degree\\\\

M_{init}= & -12 &+& 0 &+& 0 & =-12\\
M_{final}= & -12 &+& \infty &+& -\infty & =\:\:\:???\\
\end{matrix}\\
\end{align*}$$

(Note that since the lead and lag doesn't start at the same point, the infinities don't cancel. Though in this case the $M_{final}$ should be finite since both lead and lag have equal and opposite gradients (using infinity in equations,  mathematicians can just [[cope seeth and mald|cry about it lmao]]))

![[Pasted image 20231209184858.png]]

Note that if the $T$'s of the lead and lag where close enough, you could probably approximate it as a singular flat line.

![[Pasted image 20231209185125.png]]
Also here's the real function for comparison, you can see that I [[story of my life|suck at sketching]] these lol. But the idea is there. Also note that if you flip the $T$ values around you get the obvious behaviour:

![[Pasted image 20231209185525.png]]



