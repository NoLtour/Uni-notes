---
aliases: [""]
tags: []
---

## Block diagram

![[Pasted image 20231014160347.png]]

Block diagrams are a visual way to represent systems and their interconnections. They use blocks to represent components or subsystems and arrows to show the flow of signals or information between these components. Block diagrams simplify complex systems, making it easier to understand their behaviour, analyse their performance, and design control strategies.

Descent examples of block diagrams can be found in [[simplified model of a cars dynamics]].

Practically they allow for better understanding/prediction of a systems response:
- What is the response of the system to a step input, a sinusoid or a short pulse?
- Is the system stable?
- How does the system response change with the value of a coefficient

We will often use block diagrams to represent the input/output relationships of (linear) systems:
![[Pasted image 20231014160548.png]]

If we know the input/output behaviour we can estimate the dynamics – system identification
We can also determine how the system behaves at different frequencies – the frequency response
