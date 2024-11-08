---
aliases:
  - design for six sigma
  - design for reliability
  - DFSS
  - DfR
tags:
---

## Design for six sigma and design for reliability

### Comparison

Note that the [[design for six sigma and design for reliability|DFSS]] discussed here is the "traditional form", more modern forms focus less on just manufacturing.

| Name                         | Purpose                                                                                                                                                                    | Approach                                                                                                                                                                                                                                      | Focus                                                                                                                                                 |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Design for Six Sigma (DFSS)  | To ensure that products or processes meet customer requirements and perform consistently within specified limits, reducing variability and defects.                        | Utilizes statistical tools and methodologies (e.g., DMAIC - Define, Measure, Analyze, Improve, Control) to improve design processes and validate performance against Six Sigma quality standards (3.4 defects per million opportunities).     | Primarily on achieving process optimization, quality, and defect reduction by controlling and minimizing variations within the production process.    |
| Design for Reliability (DFR) | To enhance product reliability by ensuring it consistently performs over its intended life span under expected conditions, reducing failures and maintenance requirements. | Integrates reliability engineering principles, testing, and analysis (e.g., Failure Mode and Effects Analysis - FMEA, reliability testing, stress testing) early in the design phase to predict, prevent, and manage potential failure modes. | Emphasizes long-term durability, reliability, and customer satisfaction by proactively addressing failure risks rather than just controlling defects. |

DFSS focuses on minimizing defects and variability within a process, while DfR centers on designing products to withstand stressors over time, enhancing long-term reliability.

### Design for reliability process
![[Pasted image 20241106122410.png]]

The high level overview is seen in this diagram. 

#### Identify

This is the process whereby the system requirements are understood, then translated into harder reliability requirements. With the top level requirements defined, we can allocate them to subsystem designers.

From here teams will begin to collect data about [[system usage profiles]] and [[reliability benchmarking data|benchmarking data]]. Additionally early work on reliability and risk modelling will look at legacy hardware and how much we deviate from it, identifying specific technology changes. Finally some idea's of future testing and validation costs may be predicted.

![[system usage profiles]]

![[reliability benchmarking data|benchmarking data]]
#### Design
The “Design” stage defines the specific activities associated with design, at this stage we start to gain a picture of the system’s layout and its component parts.

This information means that more formal reliability analysis techniques can begin to be used:
- [[reliability block diagrams]]
- [[fault tree analysis]]
- FMECA
- HAZOPS

Regular peer reviews at this stage help highlight possible issues.

#### Analyse

Here potential causes of failure are further analysed once the design has been more physically defined.
- Physics based analysis/simulation comes into play, eg FEA, CFD
- Results of these analyses can be related to, or used in other models, to assess component, sub-system or system reliability

Results of any analysis may be fed back to the design stage to update the design in an iterative manner. Automated optimisation loops may even be employed with reliability as a design objective or constraint.

The modern design process puts heavy emphasis on such simulations within the process due to their relative speed and cost effectiveness.

#### Verify

At this stage a prototype is available and physical tests can be performed, such as:
- Accelerated life testing can be carried out (increase loading several times above typical usage, to get several times faster wear)
- Failure tests and degradation tests
- Performance tests under environmental uncertainty
- Typically this is at a sub-system or component level rather than at the full system level

Results from the verification stage can be used to make design changes. However, ideally we want these changes to be a few as possible (remember the cost of changes graph). As we’re at a component level changes cost less than when at the system level.

Results of this process can also be used to help future designs and increase confidence in their reliability predictions.

#### Validation

This is where we (hopefully) start wrapping up, we start running system level tests and ensure reliability requirements are met. If there is any unresolved issues that are noticed, we resolve them. From this point on we want NO changes to be required!

#### Control

The final stage of DfR aims to control the manufacturing process and reduce variability, since variability in production can lead to considerable reductions in reliability! This stage has lots in common with the [[design for six sigma and design for reliability|design for six sigma]] technique as it's focused on manufacture.

In reality some of these control aspects are employed through the entire design process e.g. design for uncertainty etc.

