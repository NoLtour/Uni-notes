---
aliases: [""]
tags: []
---

## M-out-of-n balanced model

Previously we covered [[complex reliability model|m-out-of-n redundancy models]], a balanced system is simular but now it requires other components to be shut down when one fails to balance the system. Think of a lander with 4 thrusters, it must maintain balance between the thruster pairs, if one fails it may have to disable it's pairing opposite:

![[Pasted image 20241029141258.png]]

If we had 2 out of 4 required from the [[complex reliability model|m-out-of-n redundancy model]] it's [[complex reliability model|reliability model]] would look like the left one, but in the balanced case it'd be the right one:

![[Pasted image 20241029141957.png]]


(Note that the right one is identical to a [[complex reliability model|parallel reliability model]] since in this case $m=1$)

So effectively, we just need to collapse those [[complex reliability model|series paths]] then we can perform regular [[complex reliability model|m-out-of-n redundancy analysis]]. It's quite clear that a balanced system will be less reliable than a normal redundant system given the same number of components, hence when dealing with balanced redundant systems we need to consider the benefits of redesigning it to not require balancing or adding more redundancy.



