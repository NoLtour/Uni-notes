---
aliases: ["GSI","Ground projected sample interval","calculating spatial resolution"]
tags: []
---

## Ground-projected sample interval

[[remote sensing (aerospace)|Spatial resolution]] can be defined using the [[ground-projected sample interval]] (kinda it's inverse):

GSD refers to the physical distance on the ground that each pixel in the image represents. It is determined by the pixel size and the altitude of the satellite. Lower GSD values mean smaller ground coverage per pixel, which leads to higher spatial detail in the image.

> ### $$\begin{align*} \text{GSI}  &= w \times \frac{H}{f}  \end{align*}$$
> ### $$\begin{align*} \text{GSI}  &= d \times \frac{H}{f}  \end{align*}$$
>> where:
>> $w=$ [[sensor sample terms|inter-detector spacing]]
>> $d=$ [[sensor sample terms|spatial sample rate]]
>> $H=$ [[satellite scanner pixel characteristics|sensor altitude]]
>> $f=$ [[satellite scanner pixel characteristics|focal length]]

It can clearly be seen that GSI can be decreased (improving resolution) by:
- Decreasing the [[satellite scanner pixel characteristics|sensor altitude]] (lower orbit)
- Increasing the [[satellite scanner pixel characteristics|focal length]] (has satellite size constraints)
- Packing the sensors more densely (technical and cost constraints)
