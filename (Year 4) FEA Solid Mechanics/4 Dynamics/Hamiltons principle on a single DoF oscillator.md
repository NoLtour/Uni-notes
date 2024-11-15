---
aliases: [""]
tags: []
---

## Hamiltons principle on a single DoF oscillator

If we take a simple oscillator:

![[Pasted image 20241112113607.png|260]]

The strain and kinetic energy are trivial to state, which can then form the [[Hamiltons principle|Lagrangian of the system]]:

$$\begin{align*}
T &= \frac{1}{2} m\dot{q}^{2} &&& U &= \frac{1}{2} k q^{2}
\end{align*}$$

Hence:

$$\begin{align*}
L &= T - U &&\to& L &= \frac{1}{2} m\dot{q}^{2} - \frac{1}{2} k q^{2}
\end{align*}$$

We cam then apply [[Hamiltons principle]]:

$$\begin{align*}
\frac{d}{dt} \left(\frac{\partial L}{\partial \dot{q}}\right) - \frac{\partial L}{\partial q} &=  0 &&\to& \frac{d}{dt} \left(\frac{\partial }{\partial \dot{q}}\left[\frac{1}{2} m\dot{q}^{2} - \frac{1}{2} k q^{2}\right]\right) - \frac{\partial }{\partial q}\left[\frac{1}{2} m\dot{q}^{2} - \frac{1}{2} k q^{2}\right] &=  0 &&\to& m\ddot{q} + kq &= 0
\end{align*}$$

That final equation should be familiar as it's 1D [[undamped free vibration (dynamics)]], as expected.


