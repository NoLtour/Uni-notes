---
aliases: ["spacecraft bus voltage selection","spacecraft bus voltage selection chart"]
tags: []
---

## Selection of system voltage

The [[spacecraft electrical bus|bus]] voltage is critical, as it effects much of the electrical system design. 

### [[yes I did use that word|Minmaxing]] voltage
 
#### Why it should increase forever
Ideally you want a really high bus voltage, since it reduces electrical losses in wires improving efficiency and reducing probably undesirable heating. Think back to the power equation:

$$ P = I^{2} R $$

You want current to be as low as possible to reduce losses from wire resistance, to do so while delivering target power you therefor need to increase voltage.

#### Issues with increasing it

Of course there are issues with increasing voltage, such as the transformers required to step up/down voltage which could lead to losses that exceed the savings from increased voltage, so the trade offs need to be considered. 

It should be noted that 160V is about the maximum that you can practically use for a bare conductor bus as at this voltage you can get interaction with space plasma (this effect is especially bad in LEO). Losses through this vector increase exponentially. (look at [[the Paschen minimum]])

Beyond that there is also just simply increased wear on parts handling higher voltages generally, so part lifespan becomes a increasingly significant factor as you deal with higher voltages.

#### Estimating the voltage

Balancing the mass/cost change to find the perfect voltage based on power demand could be a real pain in the ass... luckily we have the people who came before us who did all that hard work already! So instead we can just use the empirical law's they've observed! The following chart quantifies the general ranges for optimal bus voltage with total power draw:

![[Pasted image 20231013084645.png]]

A mathematical version of this is just:
![[Pasted image 20231013091649.png]]

So a 5000W system would be optimal at about 125V ($0.025\times5000=125$)

### Choosing a band

Instead of choosing some "optimal" voltage like 85.2341 V it's generally preferred to stick to standard bands (eg: 28, 50, 100, 120V) as seen in the chart above, doing so allows for more easy integration of standard components reducing rnd.


