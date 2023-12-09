---
aliases: [""]
tags: []
---

## Bode plot stability criteria

The whole reason for [[simple bode plots|bode plots]], is for determining the properties of some system. Mostly stability.

> ### $$\begin{align*} \text{Unstable if:}&&  \phi_{M} &< 0\degree &&\text{or}& GM&<0 \:dB\end{align*}$$
>> where:
>> $\phi_{M}=$ [[gain and phase margin|phase margin]]
>> $GM=$ [[gain and phase margin|gain margin]]

Something else worth noting is that both [[gain and phase margin|phase margin]] and [[gain and phase margin|gain margin]] contribute to stability, with larger values of both indicating a more stable system. Beyond that they also introduce a level of safety, when linearizing and approximating systems for modelling a low margin could indicate that one of your assumptions is falsely leading to stability; a large margin means even approximated systems can give a high amount of confidence in stability predictions.
