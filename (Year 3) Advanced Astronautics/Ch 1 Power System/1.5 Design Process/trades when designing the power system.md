---
aliases: ["spacecraft level trades"]
tags:
  - NotesPage
---

# 1.5 Design Process for the power system

Note that if you want to complain about layout, then how about not? The slides have a bad layout so I'm trying [[bad thing is my best sucks lmao|my best here]].

### Starting

Repeated we've shown that for a spacecraft, every choice creates trade offs which apply across subsystems. This issue exists in all design but is [[because space is cool|especially strong]] with spacecraft, which can make starting difficult.

We start with analysing the orbit parameters, the load power requirement and heritage data on similar satellites built and flown earlier. Similar missions faced similar issues, if they worked then we can clearly learn something from them.

Then we perform a [[top-level trade analysis]], to get a rough outline of the design.

(Power system mass as a percentage of the satellite dry mas can range from 25% in LEO satellites to 45% in GEO satellites)

## Trades

![[Pasted image 20231017194344.png]]

The scope needed to consider when looking at trade offs can be limited to allow for more practical analysis.

For all trades cost and subsequently mass are always of key importance. Of course the exact definition of [[optimal design]] depends on mission goal.

A general overview of the selection order may be:
![[Pasted image 20231017195937.png]]

[[you can tell I made this late with the amount of shitposting|Obviously]] this selection won't really be so linear, but it demonstrates a common order for initial consideration.

Something to keep in mind is that missions often last years, so you need to design something to last in unbelievably extreme conditions without any maintenance for fucking years. 

### Spacecraft level trades

These are the trade offs to consider at the spacecraft level.

#### Factors

The factors influencing overall architecture could be:
- Operating altitude
- Density of micrometeoroids/orbital debris
- Angle between the Earth-Sun line and the orbit plane
- Sun-tracking method for range of angles to sun (if applicable)
- Number of wings
- 1.5% eccentricity in the Earth’s orbit around the sun

#### Power system level trades

These are the trade offs being considered at the high power system level.

#### Factors

Primary selection factors could be:
- Payload power level
- Operating orbit parameter
- Mission life
- Number of satellite in the program procurement

#### Choices

Here selection of [[1.1, 1.2 Power systems Overview|power source type]] and general [[spacecraft power system architectures|power system architecture]] is made. Example configurations:
- For large high-power satellite: Fully regulated high-voltage bus
- For a short mission operating over wide orbit parameter: Peak power tracking architecture
- For an interplanetary or deep space mission: Nuclear power source


[[selection of system voltage|Spacecraft bus voltage]] level and the power generation and energy storage technologies must be jointly selected to optimise the total power.
 
### Cell level trades

#### Factors
- Generates required electrical power for the entire mission duration (considers [[end of life|EOL]])
- Degradation ([[effect of radiation on solar panel output|degredation and solar efficiency]])
	- Charged particles from mission profile
	- Off-gassing from spacecraft
	- Gases from attitude control/propulsion

![[Pasted image 20231017201015.png]]

For a LEO satellite, 10 years of degradation is about 50% output loss for silicon cells and 30% for GaAs/Ge cells... can you guess which one costs more?

#### Choices
It's a choice of cell chemistry.

### Solar array level trades

#### Factors
- Array size effects maximum power output
- Significant weight implications
- Significant impacts on propulsion and attitude control design ([[Attitude control overview|recall attitude control]])
- Significant effect on shape, casting shadows and potentially [[space drag]]

#### Choices
- Size
- Rotation mechanism

Examples:
- Large array: Increases the drag and momentum on the satellite
- Mission requiring a narrow orbit control
- Mission requiring a precision attitude control

### Battery level trades

#### Factors
- Eclipse time
- Intensity variation with orbit (more applicable to solar orbits)
- Variation of peak load
- Charge/discharge cycle count and rate
- Thermal control system (batteries tend to require tight thermal regulation)

##### Chemistry
-  Cycle life, stability of capacity and voltage
-  Round trip energy efficiency
-  Mass and volume constraints
-  Temperature effects on the performance
-  Ampere-hour capacity ratings available
-  Ease and speed of recharging
-  Self-discharging rate
-  Safety issues

#### Choices
Examples:
- GEO: high launch cost and requires fewer battery charge/discharge cycles
- LEO: low launch cost, high ionised radiation, and a much grater number of battery charge/discharge cycles

### Bus voltage trades

Mf this is all there is for this one:
![[Pasted image 20231017202432.png]]

Look back at [[selection of system voltage]] for context.

