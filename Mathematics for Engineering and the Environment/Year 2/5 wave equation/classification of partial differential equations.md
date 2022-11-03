---
aliases: ["classification of PDEs"]
tags: []
---

## Classification of partial differential equations
### Intro
If you thought the previous content about [[ordinary differential equation|ODEs]] was bad, then look at this [[abdombidination|abomination]]:

$$ a \frac{\delta^{2} u}{ \delta x^{2} } + 2b \frac{\delta^{2}u}{\delta x \delta y} + c \frac{\delta^{2} u}{\delta y^{2}} + d \frac{\delta u}{\delta x} + e \frac{\delta u}{\delta y} + fu = 0 $$

Here $u=u(x,y)$ and $a,b,c,d,e,f$ are all functions independent of $x,y$. To be able to solve that [[it really does look bad|abomination]] we need to classify the given equation into a category so that we can apply appropriate tools to solve it. These categories are:
- [[hyperbolic partial differential equations]]
- [[parabolic partial differential equations]]
- [[elliptic partial differential equations]]

Some don't fall into these categories, but for engineering it isn't common to deal with such equations so who cares.

### Embeds