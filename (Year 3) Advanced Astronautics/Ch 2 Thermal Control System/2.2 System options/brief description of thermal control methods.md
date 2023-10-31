---
aliases: ["geometry for thermal control","isolation blanket","space blanket","sun shield","radiator fin","heat pipe","types of passive thermal control options","types of active thermal control options","heaters","heat pumps","cryostat cooling","space refrigeration","louvers","shutters"]
tags: []
---

## Brief description of thermal control methods

### Passive vs active

Active is very powerful, but resource intensive and doesn't play nice with [[spacecraft maintenance problem|the spacecraft maintenance problem]]. So when reasonable we'll always opt for the passive approaches.

![[Pasted image 20231031165236.png]]

### Passive methods

#### Geometry
This is where the layout and component shape is manipulated to improve temperature characteristics:
- Configuring the spacecraft to provide the required thermal radiating area
- Placing low-temperature objects in shadow
- Exposing high-temperature objects to the sun
- Manipulation of the spacecraft to optimise thermal control

#### Isolation blanket
Also known as "space blankets" they are the thin layers you see on the outside of most spacecraft:
- Multilayer design consisting of several layers of aluminised Mylar or other plastics, spaced with nylon or Dacron mesh
- External coatings of fibreglass or Dacron may be used to protect against UV radiation, atomic oxygen erosion and micrometeoroid damage.
- They act as barriers to thermal radiation (and other types), allowing you to impair direct emission into space from the body and vice versa

![[Pasted image 20231031161833.png]]

#### Sun shield
This is effectively an evolution of the [[brief description of thermal control methods|isolation blanket]], if you __really__ don't want radiation stack up a tone of em in the direction of the sun.
- Sun shields may use less traditional materials since they are dealing with a rather extreme case

![[Pasted image 20231031162454.png]]

#### Fin
These are "hot" surfaces which rely on [[real body emission|emittance]] to cool down:
- Dissipate large amount of high temp heat or small amounts at low temperature
- Scale with surface area, often quite large
- Need to be positioned effectively as to not emit thermal radiation in a problematic manor ([[view factor]] issue)
- Can have scaling (in length) issues due to inefficiencies caused by thermal gradients (hotter near root)

![[Pasted image 20231031162557.png]]

#### Heat pipe
Tubular devices containing a wick running the length of the pipe, which is partially filled with a fluid. They are vectors for moving heat between components:
- Connected between a portion of the spacecraft from which heat is to be removed and a potion to which it is to be dumped
- Conducts energy when there is a temperature differential and crease to do so if the differential disappears, making use of fluids which naturally move to transfer heat (not actively pumped)
- Limited control can be achieved using valves and reservoirs
- Internal fluid must be selected such that phase change due to extreme conditions cannot cause issues
- Additional complications due to limited experience with fluids in zero gravity.

![[Pasted image 20231031163035.png]]


### Passive thermal control

#### Heater

Simple, resistor goes brr then electricity $\to$ heat. Controlled by computers or other simpler electrical means.

#### Heat pump (cooler)
This is where we use electricity to create a temperature gradient allowing cooling of one side and heat to be transported away.

Peltier Cooling/[[thermoelectric cooling]]:
- Uses the Peltier effect to create a temperature gradient.
- Electric current passes through materials, absorbing heat on one side and releasing it on the other.
- Compact and solid-state, but less efficient; suitable for small-scale cooling applications in spacecraft.

Cryostat for Cryogenic Cooling:
- Utilizes a cryogenic system to maintain extremely low temperatures.
- Involves the use of superconducting materials and cooling agents.
- Essential for cooling sensors, detectors, and instruments requiring ultra-low temperatures in space missions.

Refrigeration Cycles in Zero-Gravity:
- Traditional refrigeration cycles adapted for use in space.
- Use of compressors, condensers, and evaporators to circulate refrigerants.
- Challenges include managing fluids in microgravity, ensuring proper heat exchange, and maintaining system integrity during space missions.

#### Shutters/louvers

Basically, it's one step up from passive cooling. We are using shutters to control the [[view factor]] to control temperature:
- Most common active thermal control system (because it's awsome)
- Poses mechanical risks but low power use

![[fig6-25-2553287988.jpg]]

#### Actively pumped fluid loop

Pretty much heat pipe but with a pump:
- Conceptually identical to the cooling system in an automotive engine
- Long history of spaceflight applications
- Tube or pipe containing the working fluid is routed to a heat exchanger in the area or region to be heated or cooled.
- Heat transfer via forced convection into the fluid
- Working fluid: air, water, methanol, water/methanol, water/glycol, Freon, carbon tetrachloride


