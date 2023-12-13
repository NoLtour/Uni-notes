---
aliases:
  - convection
tags:
---

## Thermal boundary layer

### Heat transfer

As hinted at in [[forced convection]], there is such thing as a thermal boundary layer. 

![[Pasted image 20231210165019.png]]

The shape is just like a normal [[boundary layer]] but smaller and with a delated start. The [[parallel and series 1D heat conduction|thermal resistance]] analogy can be extended to work on this boundary layer, but obviously along the length of the plate this layer varies in thickness!

> ### $$\begin{align*} \dot{Q}  &= hA \:\Delta T &&& \dot{q}  &= h \:\Delta T  \end{align*}$$
> ### $$\begin{align*} R &= \frac{1}{hA}  \end{align*}$$
>> where:
>> $\Delta T=$ temp gradient
>> $\dot{Q},\dot{q}=$ normal and unit area [[heat transfer rate]]
>> $h=$ [[convection heat transfer coefficient]]

Note the primary difference between this and [[fundamental heat conduction (thermodynamics)|simple conduction]] resistance is the lack of the $L$ term, since in the convection case that becomes the "thickness" of the boundary layer and is too complex to model linearly so we capture it with just a $h$.

### Example

As stated above, we can continue the resistance analogy. Take the following case, state the resistance across this entire 1D transfer diagram, where there are constant thickness [[thermal boundary layer]]s on both sides with [[convection heat transfer coefficient]]s of $h_{1}$ and $h_{2}$.

![[Pasted image 20231210165724.png]]

The answer it pretty simple, this is just [[parallel and series 1D heat conduction|1D series heat conduction]]. So the total resistance is:

$$\begin{align*}
R_{T} &= R_{12} + R_{23} + R_{34} + R_{45} &\to&& R_{T} &= \frac{1}{A} \left( \frac{1}{h_{1}} + \frac{L_{A}}{k_{A}} + \frac{L_{B}}{k_{B}} + \frac{1}{h_{2}} \right)
\end{align*}$$

