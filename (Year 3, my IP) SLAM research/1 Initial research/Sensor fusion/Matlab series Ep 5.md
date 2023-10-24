On: https://youtu.be/IIt1LHIHYc4?si=-VDhWyLzj1xDJ7Vr

To avoid mapping sensor data onto the wrong tracked object counter measures obviously need to be taken:
- For sparse objects it's quite simple, associate data with the nearest object/within a certain rage of a known object. This obviously an issue when the uncertainty is large enough to cover multiple objects (either through imprecise location knowledge or clustered objects) (data association problem)
- Rules need to be created for creation/deletion of objects 
	- Eg creation of new tracked object when sensors detect something exists in what is expected to be empty space or deletion when predicted object doesn't exist
	- The issue arises when considering false positives/negatives (The track maintenance problem)

Video contains lots of really cool info, which is not really relevant to the IP so yeah...