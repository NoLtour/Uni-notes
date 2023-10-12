---
aliases: ["DoD","Depth of discharge","energy storage capacity","specific energy","energy density","charge rate","battery discharge voltage"]
tags: []
---

## Battery characteristics
### Examples
![[Pasted image 20221123151532.png]]

### Noteable preformance characteristics
#### Charge/discharge cycles
Generally you won't simply have "total charge/discharge cycles", since the level of charge/discharge per cycle as well as discharge rate and environmental conditions can all effect this. Also the battery doesn't just suddenly fail after like 1000 cycles it's really a slow decrease in preformance over the course of it's lifetime:

![[Pasted image 20221123152248.png]]
Sidenote: [[except this one this car has no skill issues|cars have a skill issue]]

#### Battery capacity $C$

Often measured in ampere hours:

> ### $$ C = It $$ 
>> where:
>> $C=$ ampere hour capacity
>> $I=$ current (amps)
>> $t=$ time (hours)

(really basic)

#### Depth of discharge (DoD)
There are 2 defenitions, [[look I do not make these stupid rules retards of the past do|figure out the one they mean]] based on context:
- The fraction or percentage of the battery's capacity which is currently removed from the battery with regard to its (fully) charged state.
- The maximum fraction or percentage of a battery's capacity (given in Ah) which is removed from the charged battery on a regular basis.

#### Energy stored ($\varepsilon$)
This is just the total energy the battery can store, it's simply the capacity $C$ multiplied by voltage, often measured in watt hours.

> ### $$ \varepsilon = C V_{B} $$ 
>> where:
>> $\varepsilon=$ Energy stored (Watt hours)
>> $C=$ battery capacity (amp hours)
>> $V_{B}=$ average battery discharge voltage

#### Energy density ($\bar{\varepsilon}$)
Also called specific energy, simply energy stored/mass of battery:

> ### $$ \bar{\varepsilon} = \frac{{\varepsilon}}{M} $$ 
>> where:
>> $\bar{\varepsilon}=$ energy density
>> ${\varepsilon}=$ energy stored
>> $M=$ mass of battery

(I don't get the choice of symbol tbh $\bar{\varepsilon}$, makes no sense since bar is usually reserved for mean value's, also wtf do we use watt hours, just use watt seconds you [[I have a extreme hate towords use of non basic SI units without good cause|annoying FUCKS]])

#### Charge rate ($R$)
The rate at which the battery can be charged, usually measured in amps.

#### Average battery discharge voltage ($V_{B}$)
This is the overall average discharge voltage of the battery, it can be found by summing the average discharge voltage of all cells in series.
