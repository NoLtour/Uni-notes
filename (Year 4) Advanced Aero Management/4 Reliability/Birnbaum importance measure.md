---
aliases:
  - Birnbaum's importance measure
tags:
---

## Birnbaum importance measure

> ### $$\begin{align*} I^{i}_{B}(t)  &=  \frac{\partial G(q(t)) }{\partial q_{i}(t)} = G(1_{i} ,q) - G(0_{i},q) \end{align*}$$
>> where using [[importance metrics notation]]:
>> $P(X_{i}=0)=q_{i}=$  The probability that the $i_{th}$ component is not working
>> $q=$ The set describing the probability of the components of the system not working
>> $G=$ the [[importance metrics notation|system unreliability function]]
>> $G(0_{i}, q)=$ The system unavailability when component $i$ is working
>> $G(1_{i}, q)=$ The system unavailability when component $i$ is not working
>> $I^{i}_{B}(t)=$ The probability that the $i_{th}$ component is critical to the systems functioning at time $t$

Obviously, according to this metric whatever has the highest $I^{i}_{B}(t)$ is the most important component.

### Example

We have a galvanometer which contains four batteries with [[hazard function|hazard rates]] of $\lambda_{1}=0.005,\:\lambda_{2}=0.009,\:\lambda_{3}=0.003\:,\lambda_{4}=0.05$ what is the reliability measure in [[complex reliability model|series and parallel]] at t=40 for this system?


Constant hazard rate, hence [[reliability function]] for each component is [[continuous distribution functions|exponential distribution]]:
$$\begin{align*}
R_{i}(t) &= e^{-\lambda_{i} t}
\end{align*}$$
Hence:
$$\begin{align*}
&&&&&&q_{i} &= 1-R_{i}(t)\\&&&&&&&=1-e^{-\lambda_{i} t}
\\\\
G_{srys}(t) &= \prod e^{-\lambda_{i}t} &&\to& G_{srys}(t) &=  e^{-\lambda_{1}t} \:e^{-\lambda_{2}t} \:e^{-\lambda_{3}t} \:e^{-\lambda_{4}t} &&\to&
G_{srys}(40) &= (1-q_{1})(1-q_{2})(1-q_{3})(1-q_{4}) 
\\\\
G_{prll}(t)(t) &= 1-\prod (1-e^{-\lambda_{i} t}) &&\to& G_{prll}(t) &= 1-(1-e^{-\lambda_{1}t})(1-e^{-\lambda_{2}t})(1-e^{-\lambda_{3}t})(1-e^{-\lambda_{4}t})
&&\to& G_{prll}(40) &= 1-q_{1}\:q_{2}\:q_{3}\:q_{4}\\\\
&&&&&&q_{1} &= e^{-\lambda_{1}40}=0.181\\
&&&&&&q_{2} &= e^{-\lambda_{2}40}=0.302\\
&&&&&&q_{3} &= e^{-\lambda_{3}40}=0.113\\
&&&&&&q_{4} &= e^{-\lambda_{4}40}=0.864\\
\end{align*}$$

Then subbing into the [[Birnbaum importance measure]] for the series system:

$$\begin{align*}
I^{i}_{B}(t)  &= G(1_{i} ,q) - G(0_{i},q) &&\to&  I^{1}_{B}(40)  &= G(1_{1} ,q) - G(0_{1},q) &&\to&  I^{1}_{B}(40)  = (1-1)(1-q_{2})(1-q_{3})(1-q_{4})  -(1-0)(1-q_{2})(1-q_{3})(1-q_{4})  &= 0.084\\
&&&...&& &&\to&  I^{2}_{B}(40)  = (1-q_{1})(1-1)(1-q_{3})(1-q_{4})  -(1-q_{1})(1-0)(1-q_{3})(1-q_{4})  &= 0.098\\
&&&...&& &&\to&  I^{3}_{B}(40)  =\:...  &= 0.077\\
&&&...&& &&\to&  I^{4}_{B}(40)  =\:...  &= 0.507
\end{align*}$$

Hence we can see that in series component 4 is the most important! Which makes intuitive sense, as it's got the highest chance of failing first.

So then we can also sub in for the parallel system:

$$\begin{align*}
I^{i}_{B}(t)  &= G(1_{i} ,q) - G(0_{i},q) &&\to&  I^{1}_{B}(40)  &= G(1_{1} ,q) - G(0_{1},q) &&\to&  I^{1}_{B}(40)  = [1-1\:q_{2}\:q_{3}\:q_{4}]-[1-0\:q_{2}\:q_{3}\:q_{4}]  &= 0.029\\
&&&...&& &&\to&  I^{2}_{B}(40)  = [1-q_{1}\:1\:q_{3}\:q_{4}]-[1-q_{1}\:0\:q_{3}\:q_{4}]   &= 0.018\\
&&&...&& &&\to&  I^{3}_{B}(40)  =\:...  &= 0.047\\
&&&...&& &&\to&  I^{4}_{B}(40)  =\:...  &= 0.006
\end{align*}$$

Then in the parallel system component 2, which is the most reliable is the most important. This also makes sense, as it's the last line of defence to keep the system running.

Although for a simple series and parallel system the "most important" seems obvious, when you start dealing with [[m-out-of-n balanced model]]s or increasingly complex systems such results become less intuitive. 

It's also worth noting that for more complex stems, the "most important" component may not be consistent across $t$!
