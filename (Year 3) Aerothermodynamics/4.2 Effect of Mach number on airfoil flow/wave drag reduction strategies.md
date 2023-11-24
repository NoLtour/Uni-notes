---
aliases: ["supercritical foil geometry","supersonic area rule"]
tags: []
---

## Wave drag reduction strategies

### Supercritical foil geometry

For transonic applications we often use supercritical foil geometry. The purpose of these is 2 fold:
- Increase the value of [[2D CFD for supersonic airfoil examples|critical Mach number]] to increase $M_{\infty}$ required for wave drag to occur
- Decrease the strength of shocks that do occur

This is achieved through this flattening of the airfoil's top.

![[Pasted image 20231123191543.png]]

### Wing [[wing sweep|sweep]]

![[Pasted image 20231123192005.png]]

- Effective oncoming Mach number is $M_{\infty}\cos \beta$, where $\beta$ is the leading edge sweep angle
- Used in transonic and supersonic regions to reduce the effective Mach number seen by the airfoil section

### Area rule

The are rule is where we maintain a smooth streamwise variation of total cross sectional area of the vehicle:

![[Pasted image 20231123192157.png]]

Doing so means that the total air compression around the vehicle can vary in a smoother manor, reducing shocks and hence entropy increases.
