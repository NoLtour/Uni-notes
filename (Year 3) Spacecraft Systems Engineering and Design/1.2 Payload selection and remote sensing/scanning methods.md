---
aliases: ["pushbroom","pushbroom scanner","line scanner","whiskbroom","whiskbroom scanner"]
tags: []
---

## Scanning methods

![[Pasted image 20231016142904.png]]


### Pushbroom scanner

#### Description

![[Push_broom_scanner_visualization.gif]]

Pushbroom scanners capture images using an array of detectors arranged along a line. The sensor scans the Earth's surface as it moves along its flight path, creating a continuous image strip. Pushbroom scanners offer high spatial and spectral resolution, making them ideal for detailed Earth observation. They are commonly used in satellites and drones for tasks like land mapping and environmental monitoring.

Since they eliminate the need for being rotated they are more reliable.

#### Quantification

![[Pasted image 20231016143013.png]]

> ### $$\begin{align*} V_{gd}  &= V_{orb} \frac{R_{E}}{r_{orb}}  \end{align*}$$
> ### $$\begin{align*} d &= t_{s} V_{gd}  \end{align*}$$
>> where:
>> $V_{gd}=$ velocity of ground relative to satellite 
>> $V_{orb}=$ velocity of satellite in orbit
>> $R_{E}/r_{orb}=$ radius of earth divided by orbital radius (assuming both circular)
>> $d=$ [[remote sensing (aerospace)|Spatial]] sample rate
>> $t_{s}=$ array sample rate

It's not so hard to apply the above to the other two methods as well, just account for the panning motion.

### Line scanner
![[Whiskbroom_visualization.gif]]

A line scanner captures images one line at a time by recording reflected or emitted radiation from the Earth's surface. The sensor typically moves perpendicular to the scan lines, creating a series of adjacent lines to form an image. Line scanners are used in applications where high spatial resolution is crucial, such as aerial photography and satellite imaging. They offer excellent image quality but may have slower data acquisition rates compared to pushbroom scanners.

### Whiskbroom scanner
(imagine this but with more pixels being scanned)
![[Whiskbroom_visualization.gif]]

A whiskbroom scanner captures images by using a moving mirror or prism to sweep across the field of view. As the mirror moves, it directs light to a detector, creating individual pixels. Whiskbroom scanners are commonly used in satellite instruments and airborne sensors. They provide high spectral and moderate spatial resolution, making them suitable for various remote sensing applications.