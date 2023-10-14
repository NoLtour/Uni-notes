---
aliases: ["primary energy source","energy converter","power regulator","power distribution and protection"]
tags: []
---

## Designing a reliable power system

### Overview

![[Pasted image 20231013081322.png]]

To provide power at the desired voltage(s) and current(s) a bunch of components are required. In the above diagram you can see how each of them connect.

### Primary energy source
Note that this is different to [[primary and secondary power system|primary power system (year 2)]], since this is just the raw source. The year 2 one is = primary energy source + energy converter.

This is the input into the system that gets converted into power, such as radiation, solar radiation, chemical fuel ect.

### Energy converter
This converts the input into useful energy, examples include a solar panel, thermoelectric generator, dynamo ect.

### Power regulator
(expanded on in [[power regulation in spacecraft]])

This converts the electric power from the converter into electricity forms required throughout the satellite. The constraints on voltage and current variance will depend on the components being supplied, for instance batteries require very specific charging conditions to not be damaged.

![[primary and secondary power system#Secondary power system (rechargeable energy storage)]]

### Power distribution and protection
Simply the wires and insulation that [[DISTROBUTE|roll credits]] power around the satellite to the various components. It also contains the external switches which can be used to cut power to specific components (may be needed in the event of a short circuit). 