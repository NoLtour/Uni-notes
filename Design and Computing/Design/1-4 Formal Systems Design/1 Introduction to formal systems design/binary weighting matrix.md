---
aliases: [""]
tags: []
---

## Binary weighting matrix
### Intro
Trying to figure out what requirements need to be given more importance than others things can get messy especially in situations with lots of requirements.
An effective method of determining an non bias estimate the relative importance of requirements is the [[binary weighting matrix]].

### How the thing works
- 2D grid with requirements a,b,c... on top and left.
- Add an indication whether the requirement for the column is more important than the requirement in the row.
- Total the number of ticks at the end of the row for that specific requirement, this gets it's total importance.

![[Pasted image 20221009103016.png]]

It should always be kept in mind that an importance score of zero doesn't mean ignore it, this is simply a tool for getting an overall feel for what should be priortised.

### Example
#### Medical device
![[Pasted image 20221009103125.png]]
![[Pasted image 20221009103203.png]]

#### [[Racist]] helmet
![[Pasted image 20221009104518.png]]