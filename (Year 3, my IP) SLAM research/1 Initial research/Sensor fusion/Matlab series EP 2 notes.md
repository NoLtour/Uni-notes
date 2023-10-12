On: https://youtu.be/0rlvvYgmTvI?si=tP_1TwESQCKnOXyB

Look into filter types:
- Complementary
- Kalman
- Madgwick
- Mahony

Combining filters:
![[Pasted image 20231010142632.png]]
- Essentially, we determine the value of what we are looking for by combining multiple inputs by weight averaging according to how much we currently "trust" their output
- This trust allows us to play to the strengths of each input and get a clearer picture of the vehicles current location

