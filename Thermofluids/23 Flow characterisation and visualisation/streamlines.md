---
aliases: ["streamline"]
tags: ["Question","QFormat3"]
---

#### What are
## Streamlines
### Definition
These are lines that connect tangential velocity points, or put simply: lines drawn through inline velocity arrows.
Demonstrated by this very well drawn diagram:
![[Pasted image 20220202113919.png]]
They are only drawn to represent velocities for a single moment of time, hence not useful to represent turbulent flow (unless if you rendered it in real time or something and could see how the lines shift over time)
They generally look more like:
![[Pasted image 20220202113951.png]]
Note that two streamlines can never cross, this is because that would imply two different velocities occupying the same point in space and time. This also means that no mass can cross a streamline, so inside a streamline mass must be cons.

### Particle representation
If we take a fluid particle and trace it's path through a fluid we can get it's [[pathlines|pathline]]:
![[Pasted image 20221017155055.png]]

It should be noted that in [[steady flow]] a [[pathlines|pathline]] is a [[streamlines|streamline]], also that the slope of a streamline at a certain point can be defined as (in 2D):
$$ \left.\frac{dy}{dx}\right|_{streamline} = \frac{V_{y}}{V_{x}} $$