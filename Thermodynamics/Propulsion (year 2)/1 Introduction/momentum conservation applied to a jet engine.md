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
(\dot{m}_{in}+\dot{m}_{fuel}) V_{jet} - \dot{m}_{in} V_{\infty} &= \sum\limits F  \\
(\dot{m}_{a}+\dot{m}_{f}) V_{jet} - \dot{m}_{a} V_{\infty} &= \sum\limits F  \\
\end{align*}$$

When dealing with jet engines we slap in a variable called "fuel to air ratio", it's definition is very unpredictable. It's the ratio of air to fuel! (shocking I know) The equation being $f= \frac{\dot{m}_{f}}{\dot{m}_{a}}$ by subbing that into the equation above it cleans up a bit:

$$\begin{align*}
(\dot{m}_{a}+\dot{m}_{f}) V_{jet} - \dot{m}_{a} V_{\infty} &= \sum\limits F & &\to & (\dot{m}_{a}+f\dot{m}_{a}) V_{jet} - \dot{m}_{a} V_{\infty} &= \sum\limits F& &\to & \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] &= \sum\limits F
\end{align*}$$

Then we know that sum of forces is just the sum of pressures plus the thrust force ([[control volume#Momentum conservation]]) $\sum\limits F= F + A_{j}(P_{j} - P_{a})$ subbing this into the equation above:
$$\begin{align*}
\dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] &= F + A_{j}(P_{j} + P_{a})
\end{align*}$$