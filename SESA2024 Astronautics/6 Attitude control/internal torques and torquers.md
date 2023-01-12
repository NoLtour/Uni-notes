---
aliases: ["angular momentum storage","control motion gyroscopes","reaction control wheels","momentum wheels","wheel saturation"]
tags: []
---

## Internal torques and torquers

These are torques that apply [[internal and external torques|internal torque]]s (aka don't effect total [[moment of linear momentum|angular momentum]]). 

### Disturbance torques

These are undesired torques that effect the spacecraft in annoying ways:

- Mechanical mechanisms
- Movement of fuel
- Movement of astronauts and robots
- Pumping of fluids

### Controllable torques
These are intentional torques used for manipulating the attitude of the spacecraft.

- Flywheels (momentum wheel), these can make the spacecraft resistant to torques ([[gyroscopic rigidity]]), their primary purpose is too maintain a high velocity. (high velocity and maintain one direction)
- Reaction wheels, these spin at a lower velocity and are for manoeuvring not primarily for momentum bias unlike momentum wheel (low velocity both directions).
- Control motion gyroscopes, this makes use of [[gyroscopic procession]] and is quite neat, essentially you rotate a something on an axis different to its current rotation to create a force ([[gyroscopic procession]]), this is generally only done on large spacecraft.

Reaction wheels and control motion gyroscopes are essentially just storage devices for [[moment of linear momentum|angular momentum]] hence it is possible for them to be saturated (reach max speed), to desaturate a reaction wheel without changing the rotation of the main spacecraft body would require some external torque such as cold gas thrusters.

#### Real world application

A common use of reaction wheels beyond just actively maintaining stability is for applications where you need a constantly changing attitude; such as maintaining pointing at a planet while in an elliptical orbit.

![[Pasted image 20221018123710.png]]

By charting the angular momentum stored over time it is possible to calculate the min storage capacity required.

![[Pasted image 20221018123744.png]]

It is also possible to have something such as a periodic [[internal and external torques|external torque]] such as dipping into the atmosphere, in this case the reaction wheels would slowly become saturated to fight off the disturbances effect:
![[Pasted image 20221018124001.png]]

Before saturation occurs and you loose control of the spacecraft, you can desaturate using any of the [[controllable external torquers]], of course to use slower ones such as [[controllable external torquers|magnetorquers]] you'll need to plan ahead a bit.