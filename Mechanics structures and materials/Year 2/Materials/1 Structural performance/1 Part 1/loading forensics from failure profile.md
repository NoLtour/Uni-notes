---
aliases: [""]
tags: []
---

## Loading forensics from failure profile

![[Pasted image 20230207001511.png]]

Here each row shows: low [[Stress safety factor|safety factor]] case, high [[Stress safety factor|safety factor]] case and then a dagram showing loading conditions that likely caused it.

What I mean by [[Stress safety factor|safety factor]] is the region of material required for operation without experiencing final failure (object is still overall below it's [[ultimate tensile strength]]). We know that the region with the [[beach marks]] is just crack, so it cannot support a tensile load, hence the only part supporting the load is the remaining region. If we know the materials [[ultimate tensile strength]] is something like 9 GPa then by calculating the region over which final failure occured  and multiplying we can get estimations of load. (useful and cook)

If something has a high [[Stress safety factor|safety factor]] then we know that the region where final failure occurred will me a small proportion of the failure surface and vice versa.

The chart also shows the difference between cases where there is severe and no stress concentation.

1) The first state (row) is a tensile stress state.
2) Second is for the bend case, it can be hard to tell from the fracture surface if it was a bend or tensile stress state since the profiles are simular so in that case you'll often have to consider external conditions to figure it out.
3) Reverse bend, this is where the force is alternating between two sides, leads to crack propigation from both sides (as you'd expect)
4) Off-axis loading in a rotating thingy.