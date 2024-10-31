---
aliases:
  - active redundancy
  - standby defenitions
  - hot standby
  - warm standby
  - cold standby
tags:
---

## Inactive redundancy

In real systems redundant components may not be in use until failure occurs, for instance a backup generator only needs to be turned on if the primary power system fails first. This is called [[inactive redundancy]], in contrast to what was discussed in [[complex reliability model|parallel reliability systems]] which were [[complex reliability model#Parallel Reliability Model|active redundancy systems]] (where the component is assumed to be in normal operation).

![[Pasted image 20241029145150.png]]

We can write out the failure condition for both of these as:

$$\begin{align*}
R_{active} &= 1 - P(\bar{A}\bar{B}) = 1- P(\bar{A}) P(\bar{B}|\bar{A}) &&& R_{inactive} &= 1 - P(\bar{A}\bar{B}) = 1- P(\bar{A}) P(\bar{B}|\bar{A})
\end{align*}$$

Although identical here, the difference comes in the value of $P(\bar{B}|\bar{A})$, in the active system they are probably [[basic rules of probability|independent events]] but [[inactive redundancy]] demands them to be dependent!

### Standby cases

There are a few possible cases for how $B$ is on standby:
- Hot standby - Here the standby component has the same [[probability density function|PDF]] as the primary component, this is basically our [[inactive redundancy|active redundancy]] case.
- Warm standby - Here the standby component has a reduced chance of failure compared to the primary component prior to engagement, this is a realistic case where even without being engaged the component has some degradation
- Cold standby - Here the standby component has zero chance of failure prior to being engaged, essentially it's "lifetime" starts the moment the primary component fails

If we were to put this into [[continuous distribution functions#Exponential Distribution|exponential distribution]] terms, it's [[hazard function|hazard rate]] prior to engagement is:

$$\begin{align*}
\lambda_{hot} &= \lambda_{primary} &&& \lambda_{warm} &< \lambda_{primary} &&& \lambda_{cold} &= 0
\end{align*}$$

### [[inactive redundancy|Cold standby]] example

The time taken before switching on $B$ (since $A$ was operating smoothly) adds to the total operational time. Hence we have to integrate over all the possible failure times for $A$ when defining the reliability with [[inactive redundancy]]:

> ### $$\begin{align*} R_{sb} (t) &=  R_{A}(t) + \int^{t}_{\tau=0} f_{A}(\tau) R_{B}(t-\tau) d\tau \end{align*}$$
>> where:
>> $R_{sb} (t)=$ [[reliability function]] of a cold standby sytem
>> $R_{A}(t)=$ [[reliability function]] of component $A$
>> $R_{B}(t)=$ [[reliability function]] of component $B$
>> $f_{A}(\tau)=$ [[probability density function]] of $A$
>> $t=$ time
>> $\tau=$ time taken for component $A$ to fail

Note this formula could be adjusted to work for the [[inactive redundancy|warm standby]] case, by defining $R_{B}$ such that it's also got some absolute time $t$ dependency rather than just time since activated.

![[Pasted image 20241029150945.png]]


### Examples

![[Pasted image 20241029151625.png]]
![[Pasted image 20241029151636.png]]

![[Pasted image 20241029151647.png]]

