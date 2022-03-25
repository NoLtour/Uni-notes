---
aliases: ["combination","combinations","permutation","permutations"]
tags: ["Question","QFormat3"]
---

#### Describe methods for
## Finding the number of combinations
### [[mutually exclusive events|Mutually exclusive]] sequence of events
#### Theory
For many situations you have a discrete variable that can take on some number of states and then a squence of these variables, for some set length of sequence there is a set number of combinations possible, for example if a 6 sided dice is rolled twice the number of possible outcomes is $6^{2}=36$ so expressed mathamatically:

> ### $$ N = n^{r} $$ 
>> where:
>> $N=$ number of possible outcomes
>> $n=$ number of possible [[mutually exclusive events]] per outcome
>> $r=$ length of outcome list

#### Example
> Find the number of possible combinations of some hypothetical 3 sided coin with states {H,T,A} thrown 2 times
 
$3^{2} = 9$

(HH, HT, HA, TH, TT, TA, AH, AT, AA)

### Permutation
#### Theory
So basically take [[finding the number of combinations#mutually exclusive events Mutually exclusive sequence of events|the thing above]] but make it so that each event can only occur once and the action is repeated until you get a list containing all possible outcomes, the number of possible combinations for that situation is:
> ### $$ N = n! $$ 
>> where:
>> $N=$ number of possible outcomes
>> $n=$ number of possible [[mutually exclusive events]] per outcome

Note that what makes sequences unique here is the order of outcomes.

#### Example
> Find the outcomes for a permutation of some hypothetical 3 sided coin with states {H,T,A}
 
$3! = (3\times2\times1) = 6$

(HTA, AHT, TAH, THA, ATH, HAT)



### Combination
#### Theory
If you want to find the number of combinations where you have some set of discrete values and each value can only occur once in the generated sequence where order doesn't matter and you repeat it a bunch of times then the number of possible combintations would be the following:

> ### $$ N = \frac{n!}{r!\times(n-r)!} = \begin{pmatrix} n \\ r \end{pmatrix} = C^{n}_{r} $$ 
>> where:
>> $N=$ number of possible combinations
>> $n=$ number of unique values
>> $r=$ length of sequence

Note that what makes sequences unique here is the combination of which states occured.
 
#### Example
> Find the number of combinations of throwing a hypothetical 3 sided coin twice.
 
$\frac{3!}{ 2! (3-2)! } = 3$

(HT, HA, TA)