---
aliases: ["physical interpretation of Reynolds number"]
tags: []
---

## Turbulence at scale

![[Pasted image 20221031151014.png]]

Turbulence can be thought of as a recursive structure, each of the larger [[eddy (fluids)|eddies]] are made up of smaller eddies, with this pattern repeating till the scale is small enough such that inertial forces are dominated by viscous forces (and hence at that scale it's somewhat laminar so the recursion stops). In fact what [[Reynolds number]] can be thought of is just a measure of the size difference between the largest and smallest [[eddy (fluids)|eddies]] that exist in a flow, hence why small Reynolds numbers correspond to laminar and large to turbulant.

Since for accurate simulation of turbulant flow you need to an accurate simulation of all scales of these [[eddy (fluids)|eddies]] it becomes apparent why in fluid simulation a higher reynolds number is harder to simulate (since the increase in eddy count is somewhat exponential).

