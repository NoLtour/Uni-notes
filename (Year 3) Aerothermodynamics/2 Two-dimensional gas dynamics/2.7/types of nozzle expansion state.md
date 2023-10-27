---
aliases: [""]
tags: []
---

## Types of nozzle expansion state

![[Pasted image 20231027191029.png]]

For this analysis of a [[converging diverging nozzles|converging diverging nozzle]] what must be kept in mind is the condition for a shock to occur:
- The flows internal pressure falls below ambient
- The geometry forces supersonic compression (convergence in the case of a nozzle)

Since our nozzle only has divergence in it's supersonic region, the shock will form in response to an adverse pressure gradient.

##### 1 Zero flow
Since there is no flow through the nozzle, the pressures don't change hence the flat line for pressure across the nozzles length.

##### 2 Completely subsonic flow
The flow doesn't exceed Mach 1 at any point in the nozzle, assuming some friction we can expect the output pressure to be slightly lower due to losses.

##### 3 Only supersonic at throat
For this to occur the back pressure must equal the critical pressure. In which case since the Mach number is 1, the "[[normal shock properties equations|normal shock]]" which occurs is barely a true shock (since there is no/negligible entropy increase). This results in a similar result to what's seen in 2.


##### 4 Normal shock within diverging region
Here the back pressure exceeds the flow pressure within the diverging region. Here Mach number has exceeded 1 so the entropy increase will be significant across the corresponding [[normal shock properties equations|normal shock]]. This results in terrible loss of efficiency.

##### 5 Normal shock at exit
Although nearly ideal, the consequences are basically identical to what was seen in point 4. It's actually worse considering the higher Mach number will mean even greater entropy increases.

##### 6 Over expanded exhaust
Here we have supersonic flow exiting the nozzle, but as it exits it falls below ambient pressure leading to a complex series of shocks and expansions. Although generally still practical it is still sub optimal as the excessive shocks lead to loss of useful energy.

##### 7 At design condition
Here supersonic flow is once again exiting the nozzle, in this case it continues in the supersonic regime and "smoothly" mixes with the atmosphere. Here we reach optimal efficiency as the lack of shock formation minimises entropy.

##### 8 Under expanded exhaust
Here we have supersonic flow exiting the nozzle, but as it exits it falls above ambient pressure leading to a complex series of shocks and expansions. Although generally still practical it is still sub optimal as the excessive shocks lead to loss of useful energy.

##### Critical note on 6 and 8

Since information cannot back propagate in supersonic flows these points are incorrect when dealing with an [[inviscid flow]]!

But consider what was described with subsonic boundary layers in [[simple observation of oblique shocks in viscous flows]]. This is the mechanism for information back propagation in cases 6 and 8. The subsonic boundary layer allows inefficiency causing phenomena to negatively effect performance within the nozzle.