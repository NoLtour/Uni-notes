---
aliases: ["EBE","extended bernouli equation"]
tags: ["Question","QFormat3"]
---

#### What is the
## Steady mechanical energy equation
### The equation
Basically this is the same as the [[steady flow energy equation]] but it has some extra terms slapped on to account for mechanical losses.

> ### $$ - \frac{\dot{W}}{\dot{m}}= \left(\frac{p}{\rho} + gz + \frac{1}{2}\alpha \bar{U}^{2} \right)_{out} - \left(\frac{p}{\rho} + gz + \frac{1}{2}\alpha \bar{U}^{2} \right)_{in} + f \frac{L}{2d} \bar{U}^{2} + \sum\limits_{n} k_{n} \left(\frac{1}{2} \bar{U}^{2}\right) $$
>> where:
>> $W=$ work done, ’non-fluid’ energy transfer. For example electrical work increasing the fluid pressure in a pump. (positive is work out, negative is work in)
>>  $p=$ pressure
>>  $\rho=$ fluid density
>>  $g=$ acceleration due to gravity
>>  $z=$ height of centre of cross sectional area
>>  $\alpha=$ [[kinetic energy correction factor]]
>>  $d=$ pipe diameter
>>  $L=$ pipe length
>>  $f=$ emperical coefficient relating to friction
>>  $k_{n}=$ the coefficient relating to that specific energy loss
>>  $\bar{U}=$ [[bulk velocity]]

^50e06c

A more simple form of the equation can be written as the following:
> ### $$ \dot{W}_{pump} - \dot{W}_{turbine} = \dot{m}\left( \left( \frac{p_{out}}{\rho} + \alpha_{out} \frac{V_{out}^{2}}{2} + gz_{out} \right) - \left( \frac{p_{in}}{\rho} + \alpha_{in} \frac{V_{in}^{2}}{2} + gz_{in} \right) \right) + \dot{E}_{mech\:loss} $$
>> where:
>> ${W}_{turbine}=$ Work done by the water on the turbine
>> ${W}_{pump}=$ Work done by the pump on the water
>>  $p=$ pressure
>>  $\rho=$ fluid density
>>  $g=$ acceleration due to gravity
>>  $z=$ height of centre of cross sectional area
>>  $\alpha=$ [[kinetic energy correction factor]]
>>  $E_{mech\:loss}=$ Energy loss as heat due to mechanical friction
>>  $V=$ velocity 


This equation only assumes [[steady flow]] and there are 2 ports, so it is widely applicable.

### Equation parts
The equation has lots of bits each with it's own meaning, so I'll break it down to be more understandable. Also note that all of these are per unit mass (divided by $\dot{m}$)

#### Energy stored in the fluid

$$ \left(\frac{p}{\rho} + gz + \frac{1}{2}\alpha \bar{U}^{2} \right)_{out} - \left(\frac{p}{\rho} + gz + \frac{1}{2}\alpha \bar{U}^{2} \right)_{in} $$
Represents the change in energy stored in the fluid (excluding heat), so pressure, kinetic and gpe are represented here.

#### Pipe frictional losses
$$ f \frac{L}{2d} \bar{U}^{2} $$

This uses a coefficient that is specific to the pipe $f$ to adjust for losses due to friction in the strait sections of pipe.

#### Fitting/joint losses
$$ \sum\limits_{n} k_{n} \left(\frac{1}{2} \bar{U}^{2}\right) $$
This represents all the losses due to the fluid moving around bends through valves ect, the coefficient $k_{n}$ is specific to the component that's being adjusted for, and since it's a sum function it can account for as many joints as need to be considered.

#### [[steady mechanical energy equation#Frictional losses|Pipe friction]] and [[steady mechanical energy equation#Fitting joint losses|fitting losses]]
$$ f \frac{L}{2d} \bar{U}^{2} + \sum\limits_{n} k_{n} \left(\frac{1}{2} \bar{U}^{2}\right) = C_{V}(T_{out} - T_{in} ) - \frac{\dot{Q}}{m} $$
Basically what this is saying is that the fitting and pipe friction is directly linked to heat change equations ([[define friction retard|I wonder why]]), I should probably write this as a proper equation definition... eh effort...
> ### $$ f \frac{L}{2d} \bar{U}^{2} + \sum\limits_{n} k_{n} \left(\frac{1}{2} \bar{U}^{2}\right) = C_{V}(T_{out} - T_{in} ) - \frac{\dot{Q}}{m} $$ 
>> where:
>>  $d=$ pipe diameter
>>  $L=$ pipe length
>>  $f=$ emperical coefficient relating to friction
>>  $k_{n}=$ the coefficient relating to that specific energy loss
>>  $\bar{U}=$ [[bulk velocity]]
>>  ${Q}=$ heat into the sytem
>>  $T=$ temp of fluid
>>  $C_V=$ [[constant volume specific heat]]
>>  $m=$ mass

#### Net work out
$$ - \frac{\dot{W}}{\dot{m}} $$
Here positive values of $W$ represent work being extracted from the system while negative values indicate work being put into the system hence:
> ### $$ \dot{W} = \dot{W}_{turbine} - \dot{W}_{pump} $$ 
>> where:
>> $\dot{W}=$ The variable used in [[steady mechanical energy equation#^50e06c|the steady mechanical energy equation]]
>> $\dot{W}_{turbine}=$ Work done by the water on the turbine
>> $\dot{W}_{pump}=$ Work done by the pump on the water