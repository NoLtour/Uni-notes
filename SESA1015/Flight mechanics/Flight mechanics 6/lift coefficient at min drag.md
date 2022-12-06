---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Lift coefficient at min drag
### Value
> ### $$C_{LminD} = \sqrt\frac{C_{Do}\pi A}{K} = \sqrt\frac{C_{Do}}{k} $$ 
>> where:
>> $C_{LminD}=$ [[lift coefficient]] at min drag 
>> $C_{Do}=$ [[form drag]] coefficient
>> $A=$ [[Wing aspect ratio]]
>> $K=$ [[induced drag coefficient#^fce277|Constant related to wing shape]]
>> $k=$ [[induced drag coefficient#^438b96|Another constant relating to wing shape]]

### Proof
Using [[min drag speed in steady level flight]]:
$$\begin{align*}
   L = W &= \frac{1}{2} \rho SC_L V^{2}   & V &= \sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{ \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   }\\
 W &= \frac{1}{2} \rho SC_L \left(\sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{ \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   }\right)^{2}\\
 W &= \frac{W\rho SC_L}{2 \rho S} \cdot \sqrt{ \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   }\\
 W &= \frac{W C_L}{2 } \cdot \sqrt{ \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   }\\
1 &= \frac{ C_L}{2 } \cdot \sqrt{ \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   }\\
1 &= \frac{ C_L^2}{4} \cdot { \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   }\\
1 &= { \frac{ KC_L^2}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   }\\
\sqrt\frac{C_{Do}\pi A}{K} &= C_{LminD}
\end{align*}$$

