---
aliases: ["observability"]
tags: []
---

## System observability

This is a measure of how well internal states of a system can be inferred from knowledge of its external outputs.

Often there are lot's of properties of a system that we can not directly measure, but using other measurements can deduce their values. This is the core goal in [[system observability]].

A mathematical way to determine if a system is [[system observability|observable]]

> $\:$
> ### $$\begin{align*} \text{Observable if:}&&&&\text{rank}(\bf{\theta})  &= n   \end{align*}$$
> ### $$\begin{align*} \bf{\theta} &= \begin{bmatrix}  \bf{C}\\\bf{C}\bf{A}\\\bf{C}\bf{A}^{2}\\... \\\bf{C}\bf{A}^{n-1}\end{bmatrix}  \end{align*}$$
>> where:
>> $\bf{A}=$ [[state space form|state matrix]]
>> $\bf{C}=$ [[state space form|output matrix]]
>> $\bf{\theta}=$ 
>> $n=$ 
>> uses [[matrix rank|rank of a matrix]]
