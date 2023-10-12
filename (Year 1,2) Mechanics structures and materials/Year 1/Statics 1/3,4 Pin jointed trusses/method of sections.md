---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Method of sections
Sometimes the [[method of joints]] is annoying for [[pin jointed truss model]]s that are very looooong. eg/
![[Pasted image 20211022215254.png]]

For these cases it becomes convinient to use the [[method of sections]] (self link wow)

1) First you consider the truss as a single body and calculate what [[External forces]] are needed to keep it in eqaulibrium
2) Then you cut the truss to get the bars that you are intrested in (note when cutting trusses you must cut through bars, you cannot cut through joints)
3) You create a new [[Free body diagram]] for the truss section and basically do (1) on the section (ngl [[method of sections]] > [[method of joints]])

### Example
Find the force in bar ED:
![[Pasted image 20211022222434.png]]

You label the diagram:
![[Pasted image 20211022222635.png]]

1) 
> this step is ez since $H_C = 0$ and $V_A=V_C=\frac{1}{2}F$ (if you don't get it then... idk, learn maths)

2) 
> now we only care about ED so we can cut away to get a easy to analyse bit:
> ![[Pasted image 20211022222951.png]]

3) 
> Horizontal:
>> $$ T_{BA} + T_{ED} + T_{EB}\cos(45) = 0 $$
>
> Vertical:
>> $$ \begin{align*}
\frac{1}{2}F &= T_{EB}\cos(45)\\
\frac{1}{2 \cos(45)}F &= T_{EB} \\
&= \frac{\sqrt{2}}{2}F
\end{align*} $$
>
> Moments (about B):
>> $$ \begin{align*}
2L \frac{1}{2}F + L T_{ED} &= 0\\
T_{ED} &= -F
\end{align*} $$
>
> You can just stop here, since $T_{ED}$ is all you needed
