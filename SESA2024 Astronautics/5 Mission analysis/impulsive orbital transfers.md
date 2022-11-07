---
aliases: ["Hohmann transfer"]
tags: []
---

## Impulsive orbital transfers
It is common to make the assumption that a manoeuvre is impulsive, which is often a reasonable approximation given the relative time of an orbital period vs the engine burn time. This assumption doesn't hold when:
- Using a long burn propulsion method such as [[ion thruster]]s.
- In a orbit with a short orbital period, such as a low earth orbit (chemical burns will often be mins but the period is only like ~90 mins).

### Outcomes of impulses
When changing an orbit using an impulse it is impossible to achieve something such as the following:
![[Pasted image 20221107113844.png]]

Since for an impulsive manoeuvre it is obvious that the current position of the spacecraft will lie on the new orbital path and hence the new orbit must intercept the old orbit at least at the point where the burn occurs:
![[Pasted image 20221107114423.png]]
If the impulse acts in the direction of motion of the satellite then the orbit will only intercept it's previous orbit at the impulse point. Of course in the case where the impulse does not act in the direction of motion you can get additional intercepts between the past and present orbit:
![[Pasted image 20221107114826.png]]

There is also the possibility of the impulse being sufficient to get the object on an escape trajectory but that's a future issue.

### Transfer between non intersecting orbits  
As discussed previously a single impulse (without the use of external objects for things like gravity assists) cannot result in:
![[Pasted image 20221107113844.png]]
Hence if you want to achieve such a transfer it will require at least 2 burns. 

#### [[impulsive orbital transfers|Hohmann transfer]]:
This is a transfer that uses two impulses, to get between two circular orbits. The first burn can occur anywhere on the first orbit but the second burn to circularise must occur on the apogee:
![[Pasted image 20221107121606.png]]
The maths is simply using the equations from [[specific orbital energy]], first of all lets express equations to describe the velocity's $V_{1},V_{2},V_{Tp},V_{Ta}$: 
$$\begin{align*}
 V_{1} &= \sqrt{\frac{\mu}{r_{1}}} & V_{2} &= \sqrt{\frac{\mu}{r_{2}}} & -\frac{\mu}{r_{1}+r_{2}} &= \frac{V_{Tp}^{2}}{2} - \frac{\mu}{r_{1}} & -\frac{\mu}{r_{1}+r_{2}} &= \frac{V_{Ta}^{2}}{2} - \frac{\mu}{r_{2}}
\end{align*}$$
Which can then be easily rearranged into more convenient forms:
$$\begin{align*}
-\frac{\mu}{r_{1}+r_{2}} &= \frac{V_{Tp}^{2}}{2} - \frac{\mu}{r_{1}} & -\frac{\mu}{r_{1}+r_{2}} &= \frac{V_{Ta}^{2}}{2} - \frac{\mu}{r_{2}}\\
\sqrt{2\mu\left(\frac{1}{r_{1}}-\frac{1}{r_{1}+r_{2}}\right)} &= V_{Tp}  & \sqrt{2\mu\left(\frac{1}{r_{2}}-\frac{1}{r_{1}+r_{2}}\right)} &= V_{Ta} 
\end{align*}$$
Then to find the $\Delta V$ required for each impulse is also trivial:
$$\begin{align*}
\Delta V_{Tp} &= V_{Tp} - V_{1} & \Delta V_{Ta} &= V_{2} - V_{Ta} \\
&= \sqrt{2\mu\left(\frac{1}{r_{1}}-\frac{1}{r_{1}+r_{2}}\right)} -  \sqrt{\frac{\mu}{r_{1}}} & &= \sqrt{\frac{\mu}{r_{2}}} - \sqrt{2\mu\left(\frac{1}{r_{2}}-\frac{1}{r_{1}+r_{2}}\right)} \\
&= \sqrt{ \mu\left(\frac{1}{r_{1}}-\frac{2}{r_{1}+r_{2}}  \right)}   & &= \sqrt{\frac{\mu}{r_{2}}-  \mu\left(\frac{2}{r_{2}}-\frac{1}{r_{1}+r_{2}}\right)}  \\
\end{align*}$$
