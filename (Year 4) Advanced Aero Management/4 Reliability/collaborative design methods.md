---
aliases: [""]
tags: []
---

## Collaborative design methods

These are methods that use a [[distributed framework]] hence it relies on [[implementing design decomposition|system decomposition]].

Sensitivity equations can be created to define the impact of a designer changing their local variable on a non-local response. (E.g. a designer changes the propeller diameter what is the impact (sensitivity) of the engine fuel consumption)

This information is used to solve a constraint on each interface by an overarching system-level coordination process. 

The problem with this approach is it requires considerable automation and analysis. Requiring automation of:
- Geometry creation
- Meshing and post processing (for FEA)
- Performance quantification

It also assumes that designers will stick to a set of variables for easy parsing. Of course designers change their designs radically over time, hence the parameter sets parsed change and then lots of work needs to be done re implementing inter-sub-system coordination!

