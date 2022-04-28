---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What are
## AC filters
### Intro
It is sometimes desirable to have circuits capable of selectively filtering one frequency or range of frequencies out of a mix of different frequencies in a circuit. A circuit designed to perform this frequency selection is called a filter circuit, or simply a filter.

If you think back to [[electrical impudance|impudance]] you'll remember that by using [[capacitors]] and [[inductor]]s you can get different resistances at different frequencies, a filter basically just exploits that fact to only let certain types of waveform through.

### General filter
Take the following circuit, where the section highlighted in blue represents the filter:
![[Pasted image 20220428191539.png|500]]
Usually you wouldn't show $Z_{out}$ instead showing it [[how it usually looks|like this]] but I'm doing so to prove a point. Take $Z_{out}$ as the [[impedance]] of the unknown circuit and $Z_{F}$ the [[impedance]] of the filter. Knowing [[equivalent circuit impedance]] for [[equivalent circuit impedance#Parallel|parallel impedance]] to we can redraw the circuit using $Z_{T}$:
![[Pasted image 20220428191553.png|350]]
where:
$$\begin{align*}
Z_{T} &= \frac{1}{\frac{1}{Z_{out}} + \frac{1}{Z_{F}}} 
\end{align*}$$

Now consider that $Z_{F}$ can be represented as $Z_{F}=R_{F} + jD_{F}$ where $D_{F}$ represents the [[magnetic reluctance|reluctance]] component of the filters [[impedance]].
$$\begin{align*}
Z_{F} &= R_{F} + jD_{F}\\
\frac{1}{Z_{F}} &= \frac{1}{R_{F} + jD_{F}}\\
\frac{1}{Z_{F}} &= \frac{R_{F} - jD_{F}}{(R_{F} + jD_{F})(R_{F} - jD_{F})}\\
&= \frac{ R_{F} - jD_{F} }{ R_{F}^{2} + D_{F}^{2}}
\end{align*}$$
We can also write an expression for $V_{out}$ as $V_{in} = V_{out} + IR$, also we know that $V_{out} = I Z_{T}$:
$$\begin{align*}
V_{in} &= I Z_{T} + IR  &  V_{out} &= I Z_{T}\\
&= I ( Z_{T} + R ) & \frac{V_{out}}{Z_{T}} &= I \\
&= \frac{V_{out}}{Z_{T}} ( Z_{T} + R )\\
&= V_{out} \left( 1 + \frac{R}{Z_{T}} \right)\\
V_{in}\frac{1}{1 + \frac{R}{Z_{T}}} &= V_{out} \\
\end{align*}$$
Now we can see from the equation above that if $Z_{T}$ is small then $\frac{R}{Z_{T}}$ tends to a large number and so $V_{out}$ will approach zero. Aka: small $Z_{T}$ means no $V_{out}$

### Types of filter
![[AC high pass filter]]