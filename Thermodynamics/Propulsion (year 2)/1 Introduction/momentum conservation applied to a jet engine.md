---
aliases: ["fuel to air ratio"]
tags: []
---

## Momentum conservation applied to a jet engine

This is just [[momentum conservation applied to a rocket engine]] but with mass flow in also entering the control volume:

![[Pasted image 20230207150622.png]]

Here we can define momentum flow with the following equations:
$$\begin{align*}
M_{out} - M_{in} &= \sum\limits F & M_{in} &= \dot{m}_{in} V_{\infty} & M_{out} &= \dot{m}_{out} V_{jet}\\
&& && &= (\dot{m}_{in}+\dot{m}_{fuel}) V_{jet}\\
(\dot{m}_{in}+\dot{m}_{fuel}) V_{jet} - \dot{m}_{in} V_{\infty} &= \sum\limits F  
\end{align*}$$

When dealing with jet engines we slap in a variable called "fuel to air ratio", it's definition is very unpredictable. It's the ratio of air
