---
aliases: [""]
tags: []
---

## Stability in state space

### Determining stability

If we want to evaluate the stability of a [[state space form]] system, then it's obvious that the stability is determined by the feedback loop part:

![[Pasted image 20231109230540.png]]

So let's focus on the equation relevant to it:

$$\begin{align*}
\dot{\bf{x}} &= \bf{A}\bf{x} + \bf{B}\bf{u}
\end{align*}$$

Then we can get it into a nice time function (after assuming no control input, $\bf{B}\bf{u}=0$):

$$\begin{align*}
\dot{\bf{x}} &= \bf{A}\bf{x} + \bf{B}\bf{u} & &\to & \frac{d\bf{x}}{dt} &= \bf{A}\bf{x}   & &\to & \int\frac{1}{\bf{x}} d\bf{x} &= \int dt \bf{A} & &\to & \bf{x} &= e^{\bf{A}t}
\end{align*}$$

Problem comes in evaluating, a matrix in the exponential is complicated. Luckily there is a short cut and I can [[my hands hurt from handling too much latex|skip over the proof]]:

> ### $$\begin{align*} e^{\bf{A} t} &= V  e^{\Lambda t} V^{-1} = V   \begin{bmatrix} e^{\lambda_{1}t} & 0 & ... & 0\\ 0 & e^{\lambda_{2}t}   & ... & 0\\... & ... &... & ...\\ 0 & 0 & ... & e^{\lambda_{n}t}\end{bmatrix} V^{-1}  \end{align*}$$
>> where:
>> $V=$ a something, doesn't matter here
>> $\Lambda=$ The [[diagonal matrix of eigenvalues]] from $\bf{A}$
>> $\lambda=$ The [[eigenvalues and eigenvectors|eigenvalues]] of $\bf{A}$
>> $\bf{A}=$ some square matrix

The only part that's important is the [[eigenvalues and eigenvectors|eigenvalues]], if any of them have a positive real component it will result in the response going to infinity. Hence making the system unstable.

### Example

![[Pasted image 20231109232716.png]]
