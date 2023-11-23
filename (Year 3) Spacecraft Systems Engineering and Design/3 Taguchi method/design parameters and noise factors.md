---
aliases: ["noise factors","design parameters","parameter levels","levels"]
tags: []
---

## Design parameters and noise factors
### Description

##### Design parameters

These are variables under the control of the designer, things like:
- Material choice in components
- Structural design
- Instrument size
- Shape

Generally about 20% of the [[design parameters and noise factors|design parameters]] lead to 80% of performance variability. Aka a tiny minority have disproportionate impact, it's critical to identify these:

![[Pasted image 20231122190849.png]]

##### Noise factors

Variables that cannot be controlled or are too expensive/impractical to control
- Atmospheric temperature
- Basically [[unless the mf wants to control space weather|any]] environmental property
- Risk of space debris impact

##### Parameter levels

Noise factors and [[design parameters and noise factors|design parameters]] by definition have more than one potential state. In some cases this is a continuous range, in others it is discrete. 

We call these potential states "levels", for the sake of making testing feasible we will convert continuous ranges into a constrained discrete sample.

### Robust design context

Quantifying robustness, means finding some objective performance characteristic(s) and optimising [[design parameters and noise factors|design parameters]] for that over a range of various [[design parameters and noise factors|noise factors]].

