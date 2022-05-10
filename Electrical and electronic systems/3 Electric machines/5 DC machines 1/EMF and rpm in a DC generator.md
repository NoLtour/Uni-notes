---
aliases: ["EMF equation for a DC generator","rpm equation for a DC generator"]
tags: ["Question","QFormat3"]
---

#### Explain and define mathamatically the
## EMF and rpm in a DC generator
### The physics
Just like with [[synchronous generators|AC generators]] the current is produced due to [[faraday's law]], an induced current in the wire causes a force perpendicular to the magnetic field lines due to the [[Lorentz's force law|lorentz force]], this resaults in a force that acts against the driving force... hence greater currents result in a greater driving force needed:

![[Pasted image 20220210181948.png]]

I'm not going to write out the maths, but for a single coil of wire $EMF \propto sin\alpha$ hence as it rotates the magnitude of the emf in the coil changes (this is where [[DC generator with many coils|DC generators with many coils]] come in).

### The equation
This equation gives you the emf production from a DC generator (note it does not factor in losses due to inefficiencys so you need to use the [[equivalent circuit of a DC generator]] when applying it):

> ### $$ E = K_{E} \omega $$ 
> ### $$ E = K_{E} \frac{\omega_{rpm}\times2\pi}{60} $$ 
>> where:
>> $E=$ [[electromotive force|EMF]] from generator (volt)
>> $\omega=$ angular velocity (rad/sec)
>> $\omega_{rpm}=$ rpm
>> $K_{E}=$ [[EMF constant (DC generator)]]

^9a26aa
