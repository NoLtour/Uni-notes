---
aliases: ["C_{L_{MD}}","C_LMD"]
tags: ["Question","QFormat3"]
---

#### What is the
## Min drag lift coefficient in steady level flight ($C_{L_{MD}}$)
### Maths
We use:
![[min drag speed in steady level flight#^c26ec7]]

$$\begin{align*}
   L &= \frac{1}{2}\rho V^{2}S C_L\\
\frac{2L}{\rho V^{2} S} &= C_L & V_{MD} &= \sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{ \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   }\\
\frac{2L}{\rho (\sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{ \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   })^{2} S} &= \\
\frac{2L\rho S}{\rho { W }S \cdot \sqrt{ \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   } } &= & L&=W\\
\frac{2 }{ 2\sqrt{ \frac{ K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   } } &=\\
\sqrt{\frac{1}{ \frac{ K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   } } &=\\
\sqrt{\frac{\pi AC_{Do}}{ K  } } &=
\end{align*}$$

### Equation
Now we have an equation for the coefficient of lift at minimum drag
> ### $$ C_{L_{MD}} = \sqrt{\frac{\pi AC_{Do}}{ K  } } $$ 
>> where:
>> $C_{L_{MD}}=$ lift coefficient at minimum drag
>> $K=$ [[induced drag coefficient|a constant related to wing planform]]
>> $A=$ [[wing aspect ratio]]
>> $C_{Do}=$ [[profile drag coefficient]]