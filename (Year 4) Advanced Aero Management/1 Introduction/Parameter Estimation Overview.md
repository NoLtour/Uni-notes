---
aliases: 
tags:
  - NotesPage
---

# Parameter Estimation

#### Intro
Although we have all the fancy [[cumulative distribution function|CDF]]s that we introduced in [[Continuous Variations Overview|the last lecture]], in the real world (where engineers sadly have to work) we don't know the constants that define those fancy [[continuous distribution functions|distribution functions]]; nor do we even know the correct distribution function to use! So we use various techniques to determine reasonable approximations such that the samples fit our chosen distribution as accurately as possible.

There are lot's of methods for finding these parameters, and all useful estimation methods have the following properties (taken from slides):
- Unbiased – the estimator should not consistently under or overestimate the true value of the parameter
- Consistent – the estimator should converge to the true value as the sample size increases
- Efficient – the estimator should be consistent with a standard deviation in that estimate smaller than any other estimator for the same population
- Sufficient – the estimator should use all of the information about the parameter that the data sample possesses

#### Contents

- [[maximum likelihood estimation]]
- [[numerical maximum likelihood estimation]]
- [[maximum likelihood estimation confidence]]
## Expanded articles
![[maximum likelihood estimation]]
![[numerical maximum likelihood estimation]]
![[maximum likelihood estimation confidence]]
