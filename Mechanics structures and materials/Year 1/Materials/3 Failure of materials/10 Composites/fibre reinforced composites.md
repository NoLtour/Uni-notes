---
aliases: ["fibre reinforced composite"]
tags: ["Question","QFormat3"]
---

#### What are
## Fibre reinforced composites
### Basics
These are [[composites]] that use fibres as [[reinforcement (materials)|reinforcement]].

![[Pasted image 20211215162033.png]]

### Mechanics
#### Graphical analysis
![[Pasted image 20211215162305.png]]
The stress strain relationship of a [[composites|composite]] will generally lie somewhere inbetween the line of the [[matrix (materials)|matrix]] and the [[reinforcement (materials)|reinforcement]].

#### Directional behaviour
As you can imagine the behaviour under stress will vary directionally assuming the threads are aligned in specific directions. If we take the following example we can model it's behaviour under stress:
![[Pasted image 20211215162531.png]]

##### Longitudinal loading
Here if we assume a good interface between the fibre and matrix we can assume that strains are all the same:
$$\begin{align*}
F_c &= F_m + F_f \\
\sigma_c A_c &= \sigma_m A_m + \sigma_f A_f && & E &= \frac{\sigma}{\varepsilon}\\
E_c\varepsilon_c A_c &= E_m\varepsilon_m A_m + E_f\varepsilon_f A_f & \varepsilon_c &= \varepsilon_m = \varepsilon_f\\
E_c A_c &= E_m A_m + E_f A_f &&& V &\propto A\\
E_c V_c &= E_m V_m + E_f V_f & V_c &= V_m + V_f\\
\therefore E_c &= \frac{E_m V_m + E_f V_f}{V_m + V_f}\\
&\end{align*}$$
> ### $$ E_c = \frac{E_m V_m + E_f V_f}{V_m + V_f} $$ 
>> where:
>> $E_c=$ [[youngs modulus]] of composite (longitudional) 
>> $E_f=$ [[youngs modulus]] of fibres (longitudional) 
>> $E_m=$[[youngs modulus]] of matrix (longitudional) 
>> $V_f=$ volume of fibres
>> $V_m=$ volume of matrix

As you can see the stiffness is related to an average of the stiffnesses of the fibres and matrix weighted by volume proportions.

##### Transverse loading
Here we can assume all stresses are the same:
$$\begin{align*}
\varepsilon_c A_c &= \varepsilon_m A_m + \varepsilon_f A_f & E &= \frac{\sigma}{\varepsilon}\\
\frac{\sigma_c}{E_c} A_c &= \frac{\sigma_m}{E_m} A_m + \frac{\sigma_f}{E_f} A_f  &&& \sigma_c = \sigma_m = \sigma_f\\
\frac{A_c}{E_c}  &= \frac{A_m}{E_m}  + \frac{A_f}{E_f} \\
\frac{E_c}{A_c}  &= \frac{1}{\frac{A_m}{E_m}  + \frac{A_f}{E_f}}\\
\frac{E_c}{A_c}  &= \frac{E_m E_f}{A_mE_f  + A_fE_m}\\
E_c  &= \frac{E_m E_f (A_m+A_f) }{A_mE_f  + A_fE_m}& V &\propto A\\
\therefore E_c  &= E_m E_f \frac{ V_m+V_f }{V_mE_f  + V_fE_m}
\end{align*}$$
> ### $$ E_c  = E_m E_f \frac{ V_m+V_f }{V_mE_f  + V_fE_m} $$ 
>> where:
>> $E_c=$ [[youngs modulus]] of composite (transverse) 
>> $E_f=$ [[youngs modulus]] of fibres (transverse) 
>> $E_m=$[[youngs modulus]] of matrix (transverse) 
>> $V_f=$ volume of fibres
>> $V_m=$ volume of matrix

Now the stiffness is determined much more by the matrix.

