---
aliases: ["time-variant", "time-invariant","time-invariant system","time variant", "time invariant"]
tags: []
---

## Time-variant system

A system is said to be time-invariant where the coefficients are constant with respect to time. For example:

$$ \alpha_{1} \frac{d^{2}y}{dx^{2}} + \alpha_{2} \frac{dy}{dx} = c $$

Here $\alpha_{1},\alpha_{2},c$ are constant's.

But contrast that with:
$$\begin{align*}
\alpha_{1} \frac{d^{2}y}{dx^{2}} + \alpha_{2}(t) \frac{dy}{dx} = c
\end{align*}$$

This is a time-variant system as it has at least one coefficient that is time dependent. Note that the following is also a case of time dependence:

$$\begin{align*}
\alpha_{1} \frac{d^{2}y}{dx^{2}} + \alpha_{2}(v) \frac{dy}{dx} = c
\end{align*}$$

Here it's because $v$ is some function of time.

Time-invariance holds different meanings depending on the context of application:
- Describing a variable as 'time-invariant' signifies that the variable remains constant over time. (so time invariant variable is identical to a constant)
- When referring to 'time-invariant systems,' it pertains to the consistency of the system's coefficients or parameters. Even though the system's output can vary with different inputs, the internal properties of the system, represented by these coefficients, remain unchanged.

