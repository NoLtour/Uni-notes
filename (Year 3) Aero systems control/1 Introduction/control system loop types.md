---
aliases: ["open-loop system","closed-loop system","open loop system","closed loop system"]
tags: []
---

## Control system loop types


#### Open-loop system
In an open-loop system, the output does not affect the control input. The system's behaviour is predetermined by the input, and it doesn't respond to changes in the output or the environment. Think of it as a one-way process without feedback. 

![[Pasted image 20231014124800.png]]

It'd be like remote controlling a car without knowing it's state, or setting a cheap fan to "speed 1". No feedback just set output.

#### Closed-loop system

In a closed-loop system (also known as feedback control system), the output is compared to a reference input, and any difference (error) between the two is used to adjust the system's behaviour. This feedback loop enables the system to self-correct and maintain stability in the presence of disturbances or changes. Closed-loop systems are more adaptive and accurate compared to open-loop systems

![[Pasted image 20231014125300.png]]

This is much closer to how people actually drive, you try to keep a target speed by constantly adjusting pedal input in response to wind, gradient, road condition ect.