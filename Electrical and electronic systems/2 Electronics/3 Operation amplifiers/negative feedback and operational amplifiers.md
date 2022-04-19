---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Negative feedback and operational amplifiers
You get some usefull behaviour when you use negative feedback with an [[operational amplifier]]:
![[Pasted image 20220419143555.png]]
Initially the voltage at $V_{+}$ would make $V_{out}$ spike to a really high value (usually createing a square wave as seen in [[operational amplifier#Generating square waves]]) but in this case since $V_{out}$ feeds back to $V_{-}$ you get the following set of equations:
$$\begin{align*}
V_{out} &= A_{OL}(V_{+}-V_{-}) & V_{-} = V_{out}\\
V_{out} &= A_{OL}(V_{+}-V_{out})\\
V_{out} + A_{OL}V_{out} &= A_{OL}V_{+}\\
V_{out} &= V_{+} \frac{A_{OL}}{1+A_{OL}}\\
V_{out} &= V_{+} \frac{1}{\frac{1}{A_{OL}}+1}\\
&& A_{OL} &>100000\\
V_{out} &\approx V_{+}
\end{align*}$$
Since $A_{OL}$ is so large we can basically assume that $V_{out}=V_{+}$, but whats more useful is the further implications of this