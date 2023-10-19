---
aliases: ["determining"]
tags: []
---

## Array voltage and current

As discussed in [[solar layout terms|solar arrays]], parallel and series count determine voltage and current output.

> ### $$\begin{align*} N_\text{series cells}  &= \frac{\text{target array voltage}}{V_{mp}}  \end{align*}$$
> ### $$\begin{align*} N_\text{array strings}  &= \frac{\text{target array current}}{I_{mp}}  \end{align*}$$
>> where:
>> $N_\text{series cells}=$ length of [[solar layout terms|strings]]
>> $N_\text{array strings}=$  size of [[solar layout terms|array]]
>> $V_{mp}=$ voltage per cell
>> $I_{mp}=$ current per [[solar layout terms|string]]

Here the $N$ numbers you get out are very unlikely to be integers, so you will need to round:
- $N_\text{series cells}$- Can be rounded either up or down, choice depends on wide range of factors. Generally if you can round down while keeping in tolerance DO IT since it saves on mass!
- $N_\text{array strings}$ - Must be rounded up, otherwise there will be insufficient power



![[Pasted image 20231017205211.png]]