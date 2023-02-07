---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Maxamising range for a piston engined aircraft
Starting with:
![[Breguet range equation (piston engine)]]

We can see everything is going to be constant except lift to drag ratio, so depending on it's value our range will change.

#### Maxamising lift to drag
We already did this (pog): 
![[max lift to drag ratio#^570509]]

So:
$$\begin{align*}
   R =& \frac{\eta}{s'}\frac{L}{D}\cdot \ln\left( \frac{W_1}{W_2} \right)  & (L/D)_{max} &= \frac{1}{2} \sqrt{  \frac{1}{C_{Do}} \cdot \frac{ \pi A }{K }  }\\
R_{max} =& \frac{\eta}{s'}\frac{1}{2} \sqrt{  \frac{1}{C_{Do}} \cdot \frac{ \pi A }{K }  }\cdot \ln\left( \frac{W_1}{W_2} \right)
\end{align*}$$

### Conclusion
> ### $$ R_{max} = \frac{\eta}{s'}(L/D)_{max}\cdot \ln\left( \frac{W_1}{W_2} \right) \:\:=\:\: \frac{\eta}{s'}\frac{1}{2} \sqrt{  \frac{1}{C_{Do}} \cdot \frac{ \pi A }{K }  }\cdot \ln\left( \frac{W_1}{W_2} \right) $$ 
>> where:
>> $R_{max} =$ Max range
>> $\eta=$ [[propeller combined efficiency]]
>> $s'=$ [[fuel consumption of a piston engined aircraft|specific fuel consumption (engine)]]
>> $(L/D)_{max}=$ [[max lift to drag ratio]]
>> $W_1=$ Starting weight
>> $W_2=$ Final weight 

This occurs at [[calculating minimum drag|minimum drag]], so it occurs at the [[min drag speed in steady level flight]] and so all the implications of that also apply to this.