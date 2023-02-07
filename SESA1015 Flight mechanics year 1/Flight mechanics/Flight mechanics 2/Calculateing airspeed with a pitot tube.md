---
aliases: [""]
tags: ["Question","QFormat3","SESA1015"]
---

#### How would you go about
## Calculateing airspeed with a pitot tube
![[Pasted image 20211019121415.png]]

$\Delta h$ can be used to determin the pressure difference between $p$ and $p_0$.

Using [[Bernouillis equation]] we know the difference between the pitot pressure and the static pressure is:

$$ p_0 - p = \frac{1}{2} \rho V^2 $$

If the two sides of the [[pitot-static tube|pitot tube]] are connected to a differential pressure guage we can get a value for $p_0-p$ and hence for $\frac{1}{2} \rho V^2$ (this value is called the [[dynamic pressure]]).

Hence true airspeed can be found by rearranging the previous equation to:

$$ V = \sqrt{ \dfrac{2(p_0-p)}{\rho} } $$

This however presents a new problem as we dont know density ($\rho$). In reality however we usually don't know air density and it can be difficult to mesure because you are moving through it, this is why instead you can use sea level density ($\rho_0 = 1.226 kg/m^3$) and therefor pressure ($p_0$) doing this while still using the equation above will give you a value called [[Equivalent Airspeed]] ($V_E$):

$$ V_E = \sqrt{ \dfrac{2(p_0-p)}{\rho_0} } $$

(Note that $\rho V^{2}= \rho_0 V_E^2$) 
