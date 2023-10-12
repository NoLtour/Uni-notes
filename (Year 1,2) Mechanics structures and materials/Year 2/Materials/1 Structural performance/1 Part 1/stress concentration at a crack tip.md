---
aliases: ["plastic zone","process zone"]
tags: []
---

## Stress concentration at a crack tip
### Process zone
Remember how stresses deflect around defects leading to concentrations which are highest along the crack tip? ([[stress concentration|these notes]]) 

![[Pasted image 20230201192718.png]]

If stress is highest at the tip then it's clear failure processes will begin here, so then here's the question lets say we have a elastic material where the local stress at the crack tip exceeds [[yield strength|yield stress]]? The answer is the local material undergoes plastic deformation (we call this region the plastic zone/process zone):

![[Pasted image 20230201193005.png]]

The deformation of the material redistributes the excess stress to be within the yield, note that the total area of the black and blue curves are the same (conservation of [[I want a meme|energy init]]). 

It is clear that since the plastic zone is experiencing sufficient stress for plastic deformation before the surrounding regions it will be the origin of localised failures (it's the weakest link).  Which means for crack analysis this in the important region!

### Energy release rate

Recall from the [[Griffith approach]], we can model the expansion of a crack under load using energy balance by considering the energy that the crack can store vs the strain energy in the crack. If the strain energy exceeds it's storage capacity then the cracks going to expand till it can fit that energy or fracture (that part is all [[now the new shit starts|just recap]]).

Previously we just considered the energy required to expand the crack as what the cracks walls can handle, but consider the plastic zone we just discussed; to expand the plastic zone you will need additional work. The additional work needed to expand the plastic zone can be accounted for with an additional term $\gamma_{p}$ (plastic zone yield stress) which is then added onto the surface energy per unit area term (for the crack) $\gamma_{e}$ then by subbing this sum into the [[Griffith approach for critical stress]] equation we can get a new one:

$$\begin{align*}
\sigma_{f} &=  \sqrt\frac{2E\gamma}{\pi a} & \gamma &= \gamma_{e} + \gamma_{p}\\
\sigma_{f} &=  \sqrt\frac{2E (\gamma_{e} + \gamma_{p})}{\pi a}\\
\frac{\sigma_{f}^{2} \pi a }{E} &=2 (\gamma_{e} + \gamma_{p})
\end{align*}$$

> ### $$\begin{align*}  \frac{\sigma_{f}^{2} \pi a }{E} &=2 (\gamma_{e} + \gamma_{p}) \end{align*}$$
>> where:
>> $\sigma_{f}=$ global fracture stress
>> $a=$ defect length (half of the actual length)
>> $E=$ material youngs modulus
>> $\gamma_{p}=$ plastic area yield stress (plastic area work term)
>> $\gamma_{e}=$ surface energy per unit area (crack area work term)

We know from previous materials stuff that plastic deformation can take a lot more energy in than elastic deformation hence why $\gamma_{p}>>\gamma_{e}$. Which helps explain why materials which can experience plastic deformation (such as ductile materials) tend to be much [[toughness|thougher]] than [[ductility|brittle]] materials.

