---
aliases:
  - general rules of probability
  - mutually exclusive events
  - simple Baye’s Theorem
  - Baye’s Theorem
  - independent events
tags:
---

## Basic rules of probability

These are basic mathematical rules, which define some useful relations using [[probability convention for advanced management|previous probability logic convention]].

#### General rules

The following are rules that apply in all situations, 

> ### $$\begin{align*} P(\bar{A})  &= 1 - P(A) &&& P({A})  &= 1 - P(\bar{A})  \end{align*}$$
> ### $$\begin{align*} P(A+B) &= P(A) + P(B) - P(AB)  \end{align*}$$
> ### $$\begin{align*} P(AB) &= P(A) + P(B) - P(A+B)  \end{align*}$$
> ### $$\begin{align*} P(AB) &= P(A)P(B|A) = P(B) P(A|B) \end{align*}$$
> ### $$\begin{align*} \text{Simple Baye’s Theorem:}&&&& P(A|B) &= \frac{P(B|A) P(A)}{P(B)} &&& P(A|B)P(B) &=P(B|A) P(A)  \end{align*}$$
>> Notation of [[probability convention for advanced management|probability logic convention]] is used.

If dealing with a situation with consecutive event's, then the total chance of $A$ occurring would be the sum of the chance of the probability of each sequence that lead's to $A$. Put mathematically:

> ### $$\begin{align*} P(A)  &= \sum\limits_{i} P(A|E_{i}) P(E_{i})  \end{align*}$$
>> where:
>> $P(E_{i})=$ The probability that some event occurs
>> $P(A)=$ The overall probability that the outcome $A$ occurs
#### Mutually Exclusive Rules

(also see [[mutually exclusive events]])

Mutually exclusive events are when one outcome means another will not occur. For instance, when rolling a dice it will only land on one face; it cannot land on both 1 and 5. Hence for a single roll the probability at it lands on 1 and 5 is zero ($P(1)P(5)=0$), so then what are the chances we get a 1 or a 5?

$$\begin{align*}
&&&&&&P(1\land6)&= 0\\
P(A+B) &= P(A) + P(B) - P(AB) &&\to& P(1+5) &= P(1) + P(5) - P(1\land6) &&\to& P(1+5) &= P(1) + P(5)
\end{align*}$$

Or put formally, for a mutually exclusive event:

> ### $$\begin{align*} P(AB)  &= 0  \end{align*}$$
> ### $$\begin{align*} P(A+B)  &= P(A) + P(B)  \end{align*}$$
>> where:
>> $P(AB)=$ Probability that $A$ and $B$ occur at the same time
>> $P(A+B)=$ Probability that either $A$ or $B$ occur

Of course, given 2 rolls it becomes possible that over those two rolls $A$ and $B$ occur, even though the rolls themselves have mutually exclusive behaviour.

#### Independent Events

This is where the outcome of one event doesn't influence the outcome of another event, mathematically it can be defined as:

> ### $$\begin{align*} P(A|B)  &= P(A) &&& P(B|A) &= P(B) \end{align*}$$

Hence, if we take the [[basic rules of probability|general rule of probability]] $P(AB) = P(A)P(B|A) = P(B) P(A|B)$ then:

$$\begin{align*}
&& P(B|A) &= P(B)\\
P(AB) &= P(A)P(B|A) &&\to& P(AB) &= P(A)P(B) 
\end{align*}$$

As you'd expect.

> ### $$\begin{align*}   P(AB) &= P(A)P(B)    \end{align*}$$

#### Example 1
![[Pasted image 20241001141251.png]]
![[Pasted image 20241001141314.png]]

#### Example 2

![[Pasted image 20241001141347.png]]

![[Pasted image 20241001141358.png]]

