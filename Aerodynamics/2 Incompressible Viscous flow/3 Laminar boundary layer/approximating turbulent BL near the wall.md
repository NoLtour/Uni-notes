---
aliases: ["skin friction velocity"]
tags: []
---

## Approximating turbulent BL near the wall

### Appropriate scales for non dimensionalising the profile near wall

We've already discussed the problems with the [[approximating a turbulent BL profile#Issues with the approximation|previous approximation near the wall]], it's scale was adjusted using freestream to scale velocity and [[boundary layer thickness]] to scale distance; in the case of being near the wall the effect of [[viscosity]] and shear is clearly greatly increased, so it makes sense to somehow use that as a part of the non dimensionalisation near the wall.

By using [[buckingham pi]] to try to find something that makes sense as a velocity scale considering the focus on the effect of shear and looking at a length scale while focusing on the effect of viscosity, we end up with the following:

> ### $$ U_{\tau} = \sqrt{\frac{\tau_{\omega}}{\rho}} $$ 
> ### $$ l = \frac{\nu}{U_{\tau}}$$ 
>> where:
>> $U_{\tau}=$ velocity scale for near wall velocity profile non dimensionalisation (this specifically is known as [[approximating turbulent BL near the wall|skin friction velocity]])
>> $\tau_{\omega}=$ [[local wall shear stress]]
>> $\rho=$ fluid density
>> $\nu=$ [[kinematic viscosity]]
>> $l=$ length scale for near wall velocity profile non dimensionalisation

^41fd5a

The derivation of the above pretty much comes down to:
- Find relationships between relevant input variables of a problem using [[buckingham pi]]
- Use experimentation/substitution and see what can be useful for non dimensionalisation

So it's educated guess work, which works [[this sort of thing is far too common lmao|:trol:]].

![[wall units (fluid dynamics near wall analysis)|wall units]]

### More stuff


