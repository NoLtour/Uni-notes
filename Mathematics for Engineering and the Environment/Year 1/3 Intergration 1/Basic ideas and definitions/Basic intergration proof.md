---
aliases: ["Intergration proof"]
tags: ["Question","QFormat3"]
---

#### What's the method for the
## Basic intergration proof
Consider you want to find the area under a graph, it's simple enough for a basic graph like:
![[Pasted image 20211020103932.png]]

But for a more complex graph:
![[Pasted image 20211020103951.png]]
Finding the area becomes much more difficult, here you could approximate the area by calculating the area of stips of the graph:
![[Pasted image 20211020104122.png]]
Here the inaccuracy of b and c will decrease as the frequency of bars increases. (if you remember [[Proof of basic differentiation|Differentiation proof]] then you see whats going on here)

If we take this method to an extreem and we keep decreasing the stip width it can be expressed formally as:

$$ \lim_{\substack{ \Delta x \rightarrow 0 \\ n \rightarrow \infty}} \sum\limits^{n}_{r=1} f(x^{*}_r)\Delta x_{r-1} $$

But normally we just use [[Intergration notation]]

( Look there is alot more to this but for now I don't think we will be tested so /shrug )