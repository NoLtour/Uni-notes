---
aliases: 
tags:
  - NotesPage
---

# Systems Reliability Models Overview

#### Intro
Up to now we've mostly been focusing on single events, but now we'll consider systems. Real life models consist of long chains of events with lots of branching, so this acts as an introduction to that.

Fundementally the entire study of engineering is trying to be able to predict how real things work, the performance of a product, it's variability in quality lead into what's actually important: it's profitability. From complex probabalistic models we can predict maintenance costs and such before having to deploy the thing to market. 

The ideal test case is to take the final product, test it properly a few thousand times and then understand it's behaviour. Obviously that's impractical for PREDICTION, so we generally rely on lower level, component level analysis then construct a (less) accurate model to estimate performance.

The lower the level we start our predictions from, the more numerically complex it is and the less reliable it is. In exchange we generally have more practical testing, not all components need to be tested, instead some can be entirely approximated with descent mathamatical models (recall [[fatigue life (material fatigue)|fatigue life calculations]]!). Common limitations are:
- (Often) Failure is highly dependent on human actions, which are a REAL pain to try and predict
- Models need to be appropriate, garbage in -> garbage out
- Conservative models can help, but they must not be so conservative they make unrealistic predictions

#### Contents

- [[complex reliability model]]
- [[reliability block diagrams]]
- [[common mode failures]]

## Expanded articles
![[complex reliability model]]
![[reliability block diagrams]]
![[common mode failures]]
