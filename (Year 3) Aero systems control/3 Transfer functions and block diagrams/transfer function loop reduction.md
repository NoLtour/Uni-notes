---
aliases: [""]
tags: []
---

## Transfer function loop reduction

### Simple loops

Turns out even feedback loops can be reduced! Which is great since they are vital in [[control system loop types|closed-loop systems]] so pop up everywhere.

>![[Pasted image 20231029122222.png]]
> ### $$\begin{align*} \text{General:}& & \frac{C}{R} \equiv G &= \frac{\text{forward path}}{1 - \text{loop path}} \\ \text{This case:}&&  G &= \frac{G_{1}G_{2}}{1+ G_{1}G_{2}H} \end{align*}$$
>> where:
>> $G_{1}(s),\:G_{2}(s),\:H(s)=$ [[Laplace transform representation of a system|Laplace domain transfer function]], multiplying it by the input function gets the output function (in the Laplace domain)
>> $R(s),\:X(s)=$ [[Laplace transform|Laplace]] domain input function
>> $E(s),\:M(s),\:B(s)=$ [[block diagram parts|Signals]]
>> $C(s)=$ [[Laplace transform|Laplace]] domain response function

In this particular case we can see that we first used [[transfer function series manipulation|series trasnfer function reduction]]. Then once we had single path's for the forward and backward paths we could sub in getting $G$.
### Complex loops

There is nothing different to what's covered in simple loops, just the added [[real and real|realisation]] that often we'll have to cleverly use all the reductions found:
- [[transfer function series manipulation|series transfer function reduction]]
- [[transfer function parallel manipulation|parallel transfer function reduction]]
- [[transfer function junction manipulation|summing junction reduction]]

To get the paths in a form that the equation can be applied.

Assume that unless explicitly stated all signals are positive (too lazy to put +'s all over the place). Ok so let's take an abomination like:

![[Pasted image 20231029125647.png]]

Now to start with let's just do a [[transfer function series manipulation|series transfer function reduction]]:

![[Pasted image 20231029125746.png]]

Ok now let's get more ambitious, we'll [[transfer function junction manipulation|summing junction manipulation]], let's move $G_{1}$ backwards which allows us to merge the 2 summing junctions:

![[Pasted image 20231029125919.png]]

It'd be nice to merge our parallel branches, so let's move $G_{2}$ so we can do that:

![[Pasted image 20231029130035.png]]

Now we can perform a [[transfer function parallel manipulation|parallel transfer function reduction]] after performing a [[transfer function series manipulation|series transfer function reduction]] on each branch:

![[Pasted image 20231029130124.png]]

Now we've got a really simple backwards feedback loop, so we just apply [[transfer function loop reduction#Simple loops|simple loop reduction]]:

![[Pasted image 20231029130206.png]]

Now we finish with a final [[transfer function series manipulation|series transfer function reduction]]:

![[Pasted image 20231029130230.png]]

There you go! It can be imagined just how useful this sort of method can be for simplifying extremely complex systems. (NOTE: This is wrong, the signs on the bottom should be flipped!)

### Sample exam question

You now have all the tools to solve something slightly more complicated. The following is [[I solved this one in my sleep ngl|trivial]], as such it is left as an exorcize to the reader:

![[Pasted image 20231029132504.png]]
