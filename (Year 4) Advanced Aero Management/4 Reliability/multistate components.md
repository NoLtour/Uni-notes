---
aliases: [""]
tags: []
---

## Multistate components

So far we've only looked at components with two states: working or [[yooooo litterally me|not]]. Real components may not only have multiple loading states (dependent on the failure of others) but also have different types of failure, in such cases we may find that adding too many redundant components actually increases chance of failure.

### Example

A simple example is a [[diode]], individually it could have 3 states:
- Normal operation
- Failure causing infinite resistance (acts like a open circuit)
- Failure causing zero resistance (acts like a short circuit)

Intuitively you can get an idea on the effects of trying to mitigate failure:
- If we want to prevent short circuits we stack them in series, such that if one shorts the next can still ensure current flows in the correct direction. Unfortunately this increases the risk posed by open circuit failure cases.
- If we want to prevent open circuit failure, we stack them in parallel, such that if one fails the other paths provide a route for current. This increases the risk posed by short circuit failure cases!

Hence it becomes a optimization problem, dependent of the pdf of both the open and short circuit case!
