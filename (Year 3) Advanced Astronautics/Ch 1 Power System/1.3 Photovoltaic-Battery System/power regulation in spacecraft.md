---
aliases: ["power regulation"]
tags: []
---

## Power regulation in spacecraft
### Intro
Power regulation is quite unique in spacecraft (this is a [[cake|lie]], it is literally the same as normal power regulation). 

### Layout overall
![[Pasted image 20231013134936.png]]

Generally, you'll connect each system in parallel from the main [[spacecraft electrical bus|bus]] (seen at the top) to a regulator which then outputs some target voltage to it's target system with some resistors thrown in there for reasons (electrical magic, out of scope). (In the diagram V_ref is essentially space ground)

### Individual regulator detail

Fundamentally a regulator is a component that controls the output voltage and or current to try to reach some target based on either a pre-set (potentially hard coded through physical design) or controlled by a computer to reach some changing target. (AKA it regulates)

![[Pasted image 20231013135336.png]]

If some component needs a specific voltage then it's regulator would be setup to "maintian X voltage".

Something like a [[batteries in spacecraft|battery]] is going to require a very specific voltage and max current, which is of course handled by it's regulator.

#### Shunting

You can see there is a [[shunts and dump loads in spacecraft|shunt]] regulator, this is to allow for excess power to be dumped from the bus (in the event [[primary and secondary power system|the secondoary power system]] can't handle the excess).
Obviously this regulator doesn't "hold X voltage across the dump resistor", instead it allows power through in response to the excess power case. (regulators are [[need to put a thing here|awesome]])

#### Realistic layout example

![[Pasted image 20231013140450.png]]
