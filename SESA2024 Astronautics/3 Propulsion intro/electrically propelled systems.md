---
aliases: [""]
tags: []
---

## Electrically propelled systems

### Description

Electrical propulsion systems use electrical power to accelerate the propellant gas out of the rocket nozzle. Electrically propelled systems tend to have very high [[specific impulse]], even multiple times higher than traditional [[bi propellant systems]], the trade off is they require large amounts of power as well as are quite low thrust (thrust being mainly limited by electricity generation).
Something else worth noting is although for more traditional propellant systems the burn time is negligible compared to orbital period such that it can be approximated by an impulse, since electrically propelled systems might burn for weeks, months even years this assumption is often not applicable.

### Maths

When working with electrically propelled systems the importance of the effect of the power plant mass should be considered, a larger power plant of course generates more power allowing for a greater thrust but also increases the mass ([[phat generator|obviously]]).

Let's define a set of equations to describe the properties of the spacecraft and it's subsystems:
- Here $\beta$ is the specific power of the plant (Watts per kg) $\beta=W/M_W$, this measures the power to generator weight efficiency
- The initial mass of the vehicle $M_{0}$ can be described interms of it's components $M_{p}=$ payload mass, $M_W=$ power plant mass, $M_{e}=$ propellant mass