---
aliases: ["skin friction velocity","viscous sub-layer","log-layer","buffer-layer"]
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

### Near wall profile

Under the [[wall units (fluid dynamics near wall analysis)|near wall normalisation]] discussed above the following relationship exists:

> ## $$ U^{+} = \begin{dcases} y^{+} &,\: y^{+}<5 \\ \frac{1}{k} \ln(y^{+})+B &,\: y^{+}>5 \: \underline{\text{and}} \: \frac{y}{\delta}<0.2 \end{dcases}  $$ 
>> where:
>> $\delta=$ [[boundary layer thickness]]
>> $U^{+}=$ [[wall units (fluid dynamics near wall analysis)|near wall normalised]] form of tangential velocity
>> $y^{+}=$ [[wall units (fluid dynamics near wall analysis)|near wall normalised]] form of normal displacement
>> $k=0.4$ 
>> $B=5.0$ 

When referring to the different parts of this equation we refer to the first section as "viscous sub layer" and the second part as "log layer". It can clearly be seen that in between these layers is undefined, this is due to the simple fact "it's too fucking hard, we have no clue what causes the variation and it's usually not important anyway.", this is common in fluid dynamics [[I did say this is far too common|lmao]]. We call this region that is in-between the layers and just an ambiguous mess the "buffer-layer".

![[Pasted image 20221101134659.png]]

Another thing to note is that the log region being $y^{+}>5 \: \underline{\text{and}} \: \frac{y}{\delta}<0.2$ is also an approximation, as can be seen in the example above the log region there starts much sooner at about $y^{+}\approx25$, same thing with the viscous sub layer though to .