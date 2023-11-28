---
aliases: [""]
tags: []
---

## Root locus plot rules

I am going to skip the optional proof.

Using these rules together will result in a root locus plot, showing all potential positions of the roots as the gain is varied.

So without further to do, here are the ~~[[clean your fucking room|12 rules for life]]~~, 9 rules for loci:

> Given the generic equation:
> ### $$\begin{align*} G_{CL}  &=   \frac{(s - z_{M })...(s - z_{3})(s - z_{2})(s - z_{1})}{(s - p_{N})...(s - p_{3})(s - p_{2})(s - p_{1})} & & & G_{OL}  &=  K \frac{(s - z_{m})...(s - z_{3})(s - z_{2})(s - z_{1})}{(s - p_{n})...(s - p_{3})(s - p_{2})(s - p_{1})}   \end{align*}$$
>> where:
>> $m=$ number of [[system transfer function feature definitions|zeros]] for the [[control system loop types|open-loop]] version
>> $n=$ number of [[system transfer function feature definitions|poles]] for the [[control system loop types|open-loop]] version
>> $M=$ number of [[system transfer function feature definitions|zeros]] for the [[control system loop types|closed-loop]] version
>> $N=$ number of [[system transfer function feature definitions|poles]] for the [[control system loop types|closed-loop]] version
>> $z_{i}=$ a [[system transfer function feature definitions|zero]]
>> $p_{i}=$ a [[system transfer function feature definitions|pole]]
>> $K=$ [[control system loop types|open loop]] gain
> 
>> #### Rule 1
>> Redundant so ignoring
> 
>> #### Rule 2
>> Redundant so ignoring
> 
>> #### Rule 3
>> If $n=m$ then: Each branch starts at the open loop pole (when $K=0$), as $K$ increases the closed loop pole approaches the open loop zeros.
>> ![[Pasted image 20231126180057.png]]
> 
>> #### Rule 4
>> If $n<m$ then: Branches that have no available zero's will tend to infinity along an asymptote where: 
>> $$ \text{number of asymptotes} = n-m $$
>> 
>> ![[Pasted image 20231126180428.png]]
> 
>> #### Rule 5
>> Asymptotes have equal angle spacings and a single origin, alternatively use the equation:
>> $$ \text{angle} = \pm \frac{(2i+1)180}{n-m}, \:\:\:\:\:\:\:\:\: i=\text{any integer} $$
>> ![[Pasted image 20231126181153.png]]
> 
>> #### Rule 6
>> All asymptotes intercept the real axis with separation from origin $\rho$ (assume negative real):
>> $$ \rho = \frac{\sum\limits \text{OL poles} - \sum\limits \text{OL zeros}}{\text{numb OL poles} - \text{numb OL zeros}} = \frac{\sum\limits p_{i}- \sum\limits z_{i}}{n-m} $$
>> ![[Pasted image 20231126181843.png]]
> 
>> #### Rule 7
>> This rule is simply a way to check working: Loci lines are symmetric about the real axis
> 
>> #### Rule 8
>> Starting from the (infinite) [[that is not what I mean|far right]], we can tell if the region should have loci intercepting on the real axis if the total zeros and poles is an odd number:
>> ![[Pasted image 20231126183637.png]]
> 
>> #### Rule 9
>> There may exist points of breakaway or arrival from the real axis, for these sketches we generally place them in the "middle" of our poles or zeros.
>> ![[Pasted image 20231126184127.png]]

