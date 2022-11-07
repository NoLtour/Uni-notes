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

### Transfer between non intersecting orbits (Hohmann transfer)
As discussed previously a single impulse (without the use of external objects for things like gravity assists) cannot result in:
![[Pasted image 20221107113844.png]]
Hence if you want to achieve such a transfer it will require at least 2 burns. Hence the [[impulsive orbital transfers|Hohmann transfer]]:
- This is a transfer that uses two impulses, one at the 