---
aliases:
  - preventive maintenance, replacements and inspection
  - PMRI
  - CIRP
  - constant interval replacement policy
  - downtime minimisation
  - availability maximisation
tags:
---

## Maintenance optimization

#### Preventive maintenance, replacements and inspection (PMRI) schedules

The primary function of such schedules is to control the condition of the system to ensure high [[maintenance key definitions|availability]]. 

The trade off can be summarised as:
- High frequencies of part replacement reduces costs due to failures but increases cost due to maintenance (and maintenance downtimes)
- Low frequencies of part replacement increases costs due to failures but decreases costs due to maintenance (and maintenance downtimes)

There's going to exist some optimal schedule that maximises productivity.

##### Constant interval replacement policy (CIRP)

The simplest preventive replacement policy is where a component is replaced after a constant interval. It's basically an or statement on:
- Replace the part every $X$ days
- Replace the part after it fails

So our cost is the sum of costs due to regular replacement and modelled failure:

> ### $$\begin{align*} c(t_{p})  &= \frac{\text{Total expected cost}}{\text{Length of interval}}  \end{align*}$$
> ### $$\begin{align*} c(t_{p})  &= \frac{c_{p} + c_{f} M (t_{p})}{t_{p}}  \end{align*}$$
>> where:
>> $c=$ cost per unit time
>> $c_{p}=$ preventative replacement cost
>> $c_{f}=$ failure replacement cost
>> $M(t)=$ [[expected number of failures]] during $t_{p}$
>> $t_{p}=$ interval between preventative replacement

Take the following example:
- A bearing wears out according to a normal distribution with $\sigma=1e5$ and $\bar{x}=1e6$ cycles
- The preventative replacement cost is $50 and the failure replacement cost is $100
- Use a discrete time interval of $1e5$ cycles (discretisation of [[expected number of failures]])

The plotted cost against replacement interval is:
![[Pasted image 20241114144741.png|400]]

We can see the previously predicted relationships taking effect here (shown in the plot below), so we want to schedule replacement at 800k cycles. 

![[Pasted image 20241114145010.png|500]]

Something worth keeping in mind is the previous work on [[optimisation under uncertainty|robust optimization]] when doing real world maintenance optimization!

#### Replacement at Predetermined Age

You're probably thinking that [[maintenance optimization|CIRP]] is inefficient, "what if the part fails and is replaced 5 mins before it's scheduled to be replaced. Then we waste money replacing it twice".

That's because it is, the advantage's are the practicality of implementation. It's far simpler to say "replace X every Y days" than "keep track of all previous replacement times, then replace after X days". That said, we will now look at the latter case. In "Replacement at Predetermined Age" we replace the part when either:
- It breaks
- It's been a certain amount of time since the last replacement

Going to skip over the proof, but the equation ends up being:

> ### $$\begin{align*} c(t_{pa})  &= \frac{\text{Total expected replacement cost per cycle}}{\text{Expected length of cycle}}  \end{align*}$$
> ### $$\begin{align*} c(t_{pa})  &= \frac{c_{p} R(t_{pa}) + c_{f} [1 - R(t_{pa})] }{t_{pa}R(t_{pa}) + [1-R(t_{pa})] \int^{t_{pa}}_{-\infty} t\:f(t)\cdot dt }  &&&= \frac{c_{p}  + c_{f} \left[\dfrac{1}{R(t_{pa})} - 1\right] }{t_{pa} + \left[\dfrac{1}{R(t_{pa})}-1\right] \int^{t_{pa}}_{-\infty} t\:f(t)\cdot dt }  \end{align*}$$
>> where:
>> $c=$ cost per unit time
>> $c_{p}=$ preventative replacement cost
>> $c_{f}=$ failure replacement cost
>> $f(t)=$ component [[probability density function]]
>> $R(t)=$ component [[reliability function]]
>> $t_{pa}=$ interval between preventative replacement relative to last replacement

(Personally I don't get why we use the first form, when we can clean it up so much)

If we use the same example from [[maintenance optimization#Constant interval replacement policy (CIRP)]] we will get a plot of:
![[Pasted image 20241114150138.png|500]]

We can see that the shapes different, but in this specific case we get about the same optimum (often isn't the case!).


#### Downtime minimisation ([[maintenance key definitions|availability]] maximisation)

There are many situations where availability is much more important than the cost of repair or maintenance, in such cases the consequences of any downtime may exceed any measurable cost.

Hence, it’s more appropriate to minimise the total downtime experienced by the system.

We will cover the equations for minimising downtime, but if both the [[maintenance key definitions|availability]] and repair costs are significant drivers of profitability (as is often the case), you can simply use the prior cost based equations and account for the additional costs imparted due to lost [[maintenance key definitions|availability]] in the $c_{p}$ and $c_{f}$ values.

##### CIRP downtime minimisation

> ### $$\begin{align*} D_{CIRP} (t_{p}) &= \frac{M(t_{p} ) T_{f} + T_{p} }{T_{p} + t_{p}}  \end{align*}$$
>> where:
>> $D=$ Downtime
>> $T_{p}=$ time taken for preventative replacement
>> $T_{f}=$ time taken for replacement after failure
>> $M(t)=$ [[expected number of failures]] during $t_{p}$
>> $t_{p}=$ interval between preventative replacement

##### Predetermined age downtime minimisation

> ### $$\begin{align*} D_{ARP} (t_{p}) &= \frac{T_{p} R(t_{pa}) + T_{f}[1-R(t_{pa})]}{ (t_{pa} + T_{p})R(t_{pa}) + [1-R(t_{pa})]\int^{t_{pa}}_{-\infty } t\:f(t) \cdot dt }  \end{align*}$$
>> where:
>> $D=$ Downtime
>> $T_{p}=$ time taken for preventative replacement
>> $T_{f}=$ time taken for replacement after failure
>> $f(t)=$ component [[probability density function]]
>> $R(t)=$ component [[reliability function]]
>> $t_{pa}=$ interval between preventative replacement relative to last replacement


