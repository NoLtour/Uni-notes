---
aliases:
  - FTA
  - fault tree analysis symbols
tags:
---

## Fault tree analysis

This is a reliability/safety design analysis technique, that starts from the high level failure effects and proceeds to break them down into the lower level events that do/can lead to it.

![[Pasted image 20241031115225.png]]

The basic event and undeveloped event nodes are the roots, at the bottom of every tree you'll find these. The primary difference between them is we can probably break down "undeveloped event" nodes further, but choose not to and instead use a model that just captures it without expanding the node further. Effectively, they serve to provide a means of reducing complexity of our tree.
