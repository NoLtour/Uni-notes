---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What are
## AC filters
### Intro
It is sometimes desirable to have circuits capable of selectively filtering one frequency or range of frequencies out of a mix of different frequencies in a circuit. A circuit designed to perform this frequency selection is called a filter circuit, or simply a filter.

If you think back to [[electrical impudance|impudance]] you'll remember that by using [[capacitors]] and [[0]]s you can get different resistances at different frequencies, a filter basically just exploits that fact to only let certain types of waveform through.

### General filter [[UNFINISHED STUFF]] need to validate this something seems off
Take the following circuit, where the section highlighted in blue represents the filter:
![[Pasted image 20220428191539.png|500]]
Usually you wouldn't show $Z_{out}$ instead showing it [[how it usually looks|like this]] but I'm doing so to prove a point. Take $Z_{out}$ as the [[impedance]] of the unknown circuit and $Z_{F}$ the [[impedance]] of the filter. Knowing [[equivalent circuit impedance]] for [[equivalent circuit impedance#Parallel|parallel impedance]] to we can redraw the circuit using $Z_{T}$:
![[Pasted image 20220428191553.png|350]]
where:
$$\begin{align*}
Z_{T} &= \frac{1}{\frac{1}{Z_{out}} + \frac{1}{Z_{F}}} 
\end{align*}$$

We can also write an expression for $V_{out}$ as $V_{in} = V_{out} + IR$, also we know that $V_{out} = I Z_{T}$:
$$\begin{align*}
V_{in} &= I Z_{T} + IR  &  V_{out} &= I Z_{T}\\
&= I ( Z_{T} + R ) & \frac{V_{out}}{Z_{T}} &= I \\
&= \frac{V_{out}}{Z_{T}} ( Z_{T} + R )\\
&= V_{out} \left( 1 + \frac{R}{Z_{T}} \right)\\
V_{in}\frac{1}{1 + \frac{R}{Z_{T}}} &= V_{out} \\
\end{align*}$$
Now we can see from the equation above that if $Z_{T}$ is small then $\frac{R}{Z_{T}}$ tends to a large number and so $V_{out}$ will approach zero. Aka: small $Z_{T}$ means negligible $V_{out}$. So now if we take out expression for $Z_{T}$ from earlier and write $Z_{F}$ as $Z_{F}=R_{F} + D_{F}$ where $R_{F}$ is the resistance of the filter and $D_{F}$ is the imaginary part from [[capacitors in AC|capacitor impedance]]/[[inductance in AC|inductive impedance]]:
$$\begin{align*}
Z_{T} &= \frac{1}{\frac{1}{Z_{out}} + \frac{1}{Z_{F}}}  & \frac{1}{Z_{F}} &= \frac{1}{R_{F} + jD_{F}}\\
Z_{T} &= \frac{1}{\frac{1}{Z_{out}} + \frac{1}{R_{F} + jD_{F}} }
\end{align*}$$
Now if we assume the filter has negligible resistance so $R_F=0$:
$$\begin{align*}
Z_{T} &= \frac{1}{\frac{1}{Z_{out}} + \frac{1}{ jD_{F}} }\\
Z_{T} &= \frac{jD_{F} Z_{out} }{Z_{out} + jD_{F} }\\
Z_{T} &= \frac{jD_{F} Z_{out}(Z_{out} - jD_{F}) }{(Z_{out} + jD_{F})(Z_{out} - jD_{F}) }\\
Z_{T} &= \frac{ D_{F}^{2} Z_{out}+ jD_{F} Z_{out}^{2} }{ Z_{out}^{2} + D_{F}^{2} }\\
Z_{T} &= \frac{ D_{F}^{2} Z_{out} }{ Z_{out}^{2} + D_{F}^{2} } + j\frac{ D_{F} Z_{out}^{2} }{ Z_{out}^{2} + D_{F}^{2} }\\
\end{align*}$$
Although this looks like gibberish, what it's saying is that for a tiny value of $D_{F}$ (the imaginary component) $Z_{T}$ will also be tiny:
$$\begin{align*}
Z_{T} &= \frac{ 0.0000001^{2} Z_{out} }{ Z_{out}^{2} + 0.0000001^{2} } + j\frac{ 0.0000001 Z_{out}^{2} }{ Z_{out}^{2} + 0.0000001^{2} }\\
Z_{T} &\approx \frac{ 0 Z_{out} }{ Z_{out}^{2} + 0 } + j\frac{ 0.0000001 Z_{out}^{2} }{ Z_{out}^{2} + 0 }\\
&\approx j \frac{ 0.0000001 Z_{out}^{2} }{ Z_{out}^{2} }
\end{align*}$$

As you can see for small values of $D_{F}$ the value of $Z_{T}$ doesn't really matter, if your goal is just to work as a filter and drop the $V_{out}$ to zero it'll work. Now all you need to do is setup the circuit such that small $D_{F}$'s occur under certain conditions.

### Types of filter
![[AC high pass filter]]