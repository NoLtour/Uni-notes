---
aliases: ["turbojet diffuser","turbojet compressor","turbojet burner","turbojet turbine"]
tags: []
---

## [[steady flow energy equation|SFEE]] simplifications for propulsion application
### Setup of problem
We will now look at simplifications of the SFEE that we usually make when analysing a gas turbine. They will also apply for ramjets, but just without the compressor and the turbine. What we will show here are basically the ‘simplest’ forms and the most ideal processes. This should get you started in being able to analyse various propulsion systems. Later in the module, and also a little later in this chapter, you will make adjustments so your calculations can resemble reality more closely.

The first thing to note is that we would usually apply the [[steady flow energy equation|SFEE]] to individual components of a gas turbine: diffuser, compressor, burner, turbine, turbine, nozzle. For now, we will look at a turbojet engine, where each component has a single inlet and a single outlet. With that, we only have a single mass flow rate  $\dot{m}$, so we can divide both sides of the SFEE by $\dot{m}$:

$$\begin{align*}
q-w &= \left(h+ \frac{V^{2}}{2}\right)_{out} - \left(h+ \frac{V^{2}}{2}\right)_{in} 
\end{align*}$$
(note we instantly simplified out gravity since it's effect is negligible)

Symbols $q,w$ the [[specific properties (thermodynamics)|specific]] heat and work, respectively. Note that for the burner, there are technically two inlets (fuel and air), but for small [[momentum conservation applied to a jet engine|fuel to air ratios]]  the mass flow rate of fuel can be neglected (like what was done in [[aircraft jet engine efficiency|these calculations]]). 
We will now apply the equation above to the gas turbine schematically drawn
in below. 

![[Pasted image 20230213085156.png]]

(Note the numbers between each component, which we will use to indicate the states.)

### Diffuser

This is a passive component, where no work is done and no heat is transferred. It's just where the air comes in and slows the fuck down, no heat or work transfer (ideally).
Air typically flows in at a high velocity, but is slowed down significantly such that the outlet kinetic energy $\frac{1}{2}(V_{2})^{2}$ can be neglected.
So subbing into the [[steady flow energy equation|SFEE]] we end up with:
$$\begin{align*}
0 &= h_{2} - h_{1} - \frac{1}{2} V_{1}^{2}
\end{align*}$$

### Compressor

The compressor is doing work on the fluid, increasing its pressure and temperature. This is an [[adiabatic expansion or compression|adiabatic]] component (no heat transfer) and the kinetic energy can be neglected at the inlet and the outlet subbing into [[steady flow energy equation|SFEE]]:

$$\begin{align*}
-w_{23} &= h_{3}- h_{2}\\
w_{c}&= 
\end{align*}$$

### Burner
The combustion is modelled as a constant pressure ([[isobaric expansion or compression|isobaric]]) heat addition process. No work is done, and kinetic energy can be neglected:

$$\begin{align*}
 &= 
\end{align*}$$
