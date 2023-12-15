---
aliases:
  - highly eccentric orbit
  - HEO
  - Molniya orbit
  - Tundra orbit
tags:
---

## Highly eccentric orbit (year 3)

### Common features

[[highly eccentric orbit (year 3)|HEO]]s are characterised by their extremely high elevations. Which allows access to regions of the earth that cannot be covered by [[geostationary coverage|GEO coverage]].

A specific subset of HEO make use of periods that are 12 hour ([[highly eccentric orbit (year 3)|Molniya orbit]]) and 24 hour ([[highly eccentric orbit (year 3)|Tundra orbit]]) which allows them to target specific regions on the earths surface for significant lengths of their orbit. Which is especially useful for military and communications.

Other common advanteges of HEO is:
- Short eclipses, which don't occur near apogee (often the main operating period for comms)
- The flexibility allows for targeting specific latitudes, though additional consideration regarding stability is required

There are many disadvantages that must also be considered:
- Ground stations do still require active tracking, unlike [[geostationary coverage|GEO]]
- The ground stations must actively account for the [[doppler effect]] since the relative velocity of the satellite is changing in a complex mannor
- The intensity of the signal also varies as distance varies
- Latency varies with distance
- For [[highly eccentric orbit (year 3)|HEO]] that are not synced with Earths rotation, they can have constant change in ground coverage, this can be an advantage for some use cases
- Orbital perturbations ([[space drag]]) with potential for significant interference from the moon due to high [[ellipse|eccentricity]]
- Passes through [[Van Allen radiation belts]], which can cause significant problems for the [[spacecraft maintenance problem]]

The following visualises typical orbital drift for [[highly eccentric orbit (year 3)|HEO]]:
![[Pasted image 20231215114350.png]]

### Molniya orbit

#### Description

Highly elliptical 12 hour orbit (strictly, half a [[sidereal day]] 11 h 58 m), inclined at 63.4° or 116.6° to the equator.

This type of orbit is particularly useful for communication satellites serving polar and high-latitude regions, where geostationary satellites may have limitations due to their positioning relative to the equator. Molniya orbits allow for longer dwell times over high-latitude areas, improving communication services in these regions

![[Pasted image 20231215105018.png]]

#### Coverage

The critical inclination combined with high eccentricity means coverage is good for high latitude ground stations, as about 99% of the orbital period is spent between $90\degree\leq f\leq 270\degree$, which is the useful section of the orbit.

![[Pasted image 20231215105558.png]]
![[Pasted image 20231215105623.png]]

By syncing the period with half the rotation of the earth a [[highly eccentric orbit (year 3)|Molniya orbit]] satellite can spend the majority of it's time over a specific area of the planet, as seen above. The problem being that this useful period is half spent over your target region as well as every other cycle being spent on the opposite side of the earth. 
This would be an issue if the USSR wanted a purely communication satellite, but would you look at that. It coincidently spends that other cycle over the US! Wow! You might even pick up some fun radio signals while over the US or something, purely an accident since this is a "communications" satellite!

To achieve 24 hour coverage of the target region, 3 satellites spaced 120 degrees apart are needed.

### Tundra orbit 

#### Description

This is a Highly elliptical 24 hour (strictly, 23 h 56 m) orbit, inclined at 63.4°to the equator (a = RGEO = 42,164 km).

![[Pasted image 20231215110724.png]]


#### Coverage
Unlike [[highly eccentric orbit (year 3)|Molniya orbit]]s, these have a period that syncs up with the earth, so they only spend there useful time over one spot. Of course this requires boosting to a pretty high [[perigee and apogee|apogee]]:


![[N0H7Q.gif]]

Similarly to [[highly eccentric orbit (year 3)|Molniya orbit]]s, [[highly eccentric orbit (year 3)|Tundra orbit]]s need 3 satellites to maintain 24h coverage of their target region