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
![[Pasted image 20220428185859.png|400]]
Usually you wouldn't show $Z_{out}$ instead showing it [[how it usually looks|like this]] but I'm doing so to prove a point. Take $Z_{out}$ as the [[impedance]] of the unknown circuit and $Z_{F}$ the [[impedance]] of the filter. Knowing [[equivalent circuit impedance]] for [[equivalent circuit impedance#Parallel|parallel impedance]] to get $Z_{T}$:
![[Pasted image 20220428191112.png|300]]

$$\begin{align*}
Z_{T} &= \frac{1}{Z_{out} + Z_{F}} 
\end{align*}$$

Now consider that $Z_{F}$ can be represented as $Z_{F}=$

### Types of filter
![[AC high pass filter]]