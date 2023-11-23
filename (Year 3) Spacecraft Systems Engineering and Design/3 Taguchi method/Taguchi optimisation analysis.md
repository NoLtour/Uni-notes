---
aliases:
  - signal to noise ratio
tags:
---

## Taguchi optimisation analysis

### Performance matrix

Effectively what [[experiment design for the Taguchi method#Orthogonal matrices]] are, is a way of creating a set of unique parameter combinations for an experiment. 

Thing is we need both a set of [[design parameters and noise factors|design parameters]] and [[design parameters and noise factors|noise factors]] for an experiment, to do this we simply apply everything discussed to produce an orthogonal matrix for the [[design parameters and noise factors|noise factors]] also!

Then we rotate the [[design parameters and noise factors|noise factor]] matrix to align them such that each interception results in a unique experiment:

![[Pasted image 20231122202423.png]]

Then by taking the results of those experiments and characterising the overall performance we can populate that matrix with some score.

### Signal to noise ratio

> ### $$\begin{align*} \text{Min equation}& & S/N_{i}  &= -10 \log_{10} \left( \frac{1}{n_{T}} \sum\limits^{n_{T}}_{j=1} Q_{ij}^{2} \right) \\\\ \text{Max equation}& & S/N_{i}  &= -10 \log_{10} \left( \frac{1}{n_{T}} \sum\limits^{n_{T}}_{j=1} \frac{1}{Q_{ij}^{2}} \right)  \end{align*}$$
>> where:
>> The min equation is used in the case that minimising $Q$ is most desirable, while the max equation is used when maximising $Q$ is desirable
>> $S/N_{i}=$ Signal to noise ratio for a row
>> $n_{T}=$ Number of experiments per [[design parameters and noise factors|design parameter]] combination
>> $Q_{ij}=$ The performance metric result for a particular [[design parameters and noise factors|noise factor]] and [[design parameters and noise factors|design parameter]] combinations experiment

The signal to noise ratio can be calculated for each combination of [[design parameters and noise factors|design parameters]], it's effectively a measure of that configurations performance for all tested [[design parameters and noise factors|noise factors]] aka "robustness".

### Average signal to noise ratio

Signal to noise ratio only provides a specific combinations performance, if we want to understand how individual parameters contribute to performance we can make use of averages:

> ### $$\begin{align*} S/N_{avg\;X}  &= \frac{1}{n_{TX}}\sum\limits^{n_{TX}}_{r=1} S/N_{X,r} \end{align*}$$
>> where:
>> $S/N_{avg\;X}=$ average noise factor when a parameter has value $X$
>> $S/N_{X,r}=$ noise factor in experiment $r$ where a specific parameter has value $X$ 
>> $n_{TX}=$ number of experiments where a specific parameter has value $X$

Example:
![[Pasted image 20231122204824.png]]

### Selection

Instead of simply choosing the configuration with the highest noise factor, as seems intuitive... we can go one step further to increase robustness even more.

The average noise factor for each level of [[design parameters and noise factors|design parameters]] can be computed, then that value is what get's used as the "most robust" [[design parameters and noise factors|level]]. This is the core of the [[Taguchi Method Overview|Taguchi Method]].

![[Pasted image 20231122204908.png]]

### Limitations of Taguchi method

There are a bunch of limitations of this method

- Inner and outer array structure assumes no interaction between design parameters and noise factors
- It is possible that the "most robust" combination chosen has a terrible S/N value as assumption of independent performance is unlikely to hold
- Only accounts for one performance characteristic
- Assumes continuous functions (in computation of performance characteristic)

These limitations mean that in industry much more robust method's get used, but this provides a basic introduction into design optimisation.
