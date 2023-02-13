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

### The bits of the engine
#### Diffuser

This is a passive component, where no work is done and no heat is transferred. It's just where the air comes in and slows the fuck down, no heat or work transfer (ideally).
Air typically flows in at a high velocity, but is slowed down significantly such that the outlet kinetic energy $\frac{1}{2}(V_{2})^{2}$ can be neglected.
So subbing into the [[steady flow energy equation|SFEE]] we end up with:
$$\begin{align*}
0 &= h_{2} - h_{1} - \frac{1}{2} V_{1}^{2}
\end{align*}$$

#### Compressor

The compressor is doing work on the fluid, increasing its pressure and temperature. This is an [[adiabatic expansion or compression|adiabatic]] component (no heat transfer) and the kinetic energy can be neglected at the inlet and the outlet subbing into [[steady flow energy equation|SFEE]]:

$$\begin{align*}
-w_{23} &= h_{3}- h_{2}\\
w_{c}&= 
\end{align*}$$

#### Burner
The combustion is modelled as a constant pressure ([[isobaric expansion or compression|isobaric]]) heat addition process. No work is done, and kinetic energy can be neglected:

$$\begin{align*}
q_{34} &= h_{4} - h_{3}
\end{align*}$$

#### Turbine

The turbine extracts work from the fluid, decreasing its pressure and temperature. Like the compressor (basically reverse compressor), it is an adiabatic component and kinetic energies can be neglected.

$$\begin{align*}
-w_{45} &= h_{5} - h_{4}\\
-w_{t} &= 
\end{align*}$$

An important aspect is that all the work that the turbine delivers is used to drive the compressor, so we can combine it back with the compressor equation:

$$\begin{align*}
w_{c} &= w_{t}\\
h_{3}- h_{2} &= -(h_{5} - h_{4})
\end{align*}$$

#### Bozzle
A nozzle is effectively the inverse of a diffuser. It is an adiabatic component and no work is done. The inlet kinetic energy can be neglected, but we need to account for the kinetic energy at the outlet:

$$\begin{align*}
0 &= h_{6} - h_{5} + \frac{1}{2} V^{2}_{6}
\end{align*}$$

### Assumptions

So that the maths is more manageable we will be making the assumption that:
- All processes are [[reversible and irreversible processes|reversible]]
- The gas is a [[perfect gas]] (hence we can use $\delta h=c_{p} (\Delta T)$)

The reversibility means that all [[adiabatic expansion or compression|adiabatic processes]] are [[isentropic process|isentropic]], this plus the fact that we are dealing with a [[perfect gas]] means that (combing temp equation with [[adiabatic expansion or compression#^7c299a|this adiabatic equation]]):
$$\begin{align*}
\frac{T_{2}}{T_{1}} &= \left(\frac{P_{2}}{P_{1}}\right)^\frac{\gamma-1}{\gamma}
\end{align*}$$

### Entropy

Real turbines, compressors, nozzles and diffusers are not isentropic due to irreversibilities. This means that the isentropic relations are not valid anymore to relate changes in pressure to changes in temperature and density. In this section we will look at how we can take non-isentropic effects into account in our calculations. We will start with some fundamental concepts of entropy and how to calculate changes in entropy.