---
aliases: ["DC generator with one coil"]
tags: ["Question","QFormat3"]
---

#### Describe a
## Basic DC generator
Recalling the design for a simple AC generator:
![[Pasted image 20220210172634.png]]

A DC generator basically works the same way, except instead of 2 slip rings there is only one, and the slip ring is split into two halfs:

![[Pasted image 20220210172708.png]]

The cut is made in a way so that the contacts reverse at the instant the current changes directions, hence AC becomes DC. The ring cannot be called a [[slip ring]] anymore, it is a [[commutator]].

Of course even with the currents direction corrected, the magnitude of [[electromotive force|EMF]] still follows a sin wave in the form $E=k|\sin t|$ which makes for a pretty shitty waveform for most applications, this is where a [[DC generator with many coils]] comes in.