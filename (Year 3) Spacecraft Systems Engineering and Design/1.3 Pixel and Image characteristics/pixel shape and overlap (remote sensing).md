---
aliases: ["pixel shape and overlap","calculating IFOV","calculating GIFOV","pixel data size","swadth width"]
tags: []
---

## Pixel shape and overlap (remote sensing)

### Overlap

You'd think that sensors would split the earth into [[you can tell by the way this is written it wont last|beautiful clean]] squares, and setup each sensor to scan one pixel exactly:

![[Pasted image 20231017175526.png]]

But in real life there are not only technical reasons why this nice allocation is difficult to achieve, but also some cases where there are benefits in overlap or sample sparseness:

![[Pasted image 20231017175545.png]]

(Whelp there [[this is why humanity can not have nice things|goes my clean layout]])

### Calculating features

![[Pasted image 20231017173144.png]]

#### Calculating [[satellite scanner pixel characteristics|IFOV]] and [[satellite scanner pixel characteristics|GIFOV]]

Note that in the following we approximate using small angle approximations, considering how [[unrelated but look at this vomit|tiny]] the [[satellite scanner pixel characteristics|IFOV]] will be there's going to be basically no accuracy loss in the approximation (at least for most sensor applications).

> ### $$\begin{align*} \text{IFOV}  &=  2 \arctan\left( \frac{w}{2f} \right)  \approx \frac{w}{f} \end{align*}$$
> ### $$\begin{align*} \text{GIFOV}  &=  2 H \tan\left( \frac{\text{IFOV}}{2} \right)  \approx w \frac{H}{f} \end{align*}$$
> ### $$\begin{align*} \text{GFOV}  &=  \text{GIFOV} N \end{align*}$$
>> where:
>> $\text{IFOV}=$ [[satellite scanner pixel characteristics|IFOV]]
>> $\text{GIFOV}=$ [[satellite scanner pixel characteristics|GIFOV]]
>> $\text{GFOV}=$ [[satellite scanner pixel characteristics|swadth width]]
>> $N=$ pixel count ([[scanning methods|pushbroom]])
>> $w=$ [[sensor sample terms|inter-detector spacing]]
>> $f=$ [[satellite scanner pixel characteristics|focal length]]
>> $H=$ [[satellite scanner pixel characteristics|sensor altitude]]

#### Data size

The "data size" is going to obviously be a function of the number of potential states a pixel has and the pixel count. The number of unique states a binary number can hold is [[trivialize deez|trivial]] to calculate:

> ### $$\begin{align*} N_{DN}  &= 2^{Q}  \end{align*}$$
>> where:
>> $N_{DN}=$ Denary (base 10) potential number of states for $Q$ length binary number
>> $Q=$ binary number length

So we can use this ^ to help characterize data size. There is also the option of lossy compression (instead of sending all the data we remove unimportant bit's), allowing for a smaller $Q$ size.

Total (lossless uncompressed) data size can be calculated pretty trivially. Simply multiply the binary representation length ($Q$) by the total number of pixels to get total image length.
