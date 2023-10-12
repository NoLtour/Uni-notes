Done on: https://youtu.be/6qV3YjFppuc?si=Jm327E4zo5cILYrv

Fundementally sensor fusion is combining the data from multiple sources to generate a better understanding of the environment.


Sensor noise reduction:
- Averaging, can reduce non-correlated noise between similar sensors:
 ![[Pasted image 20231010140149.png]]

- Corrilated noise can invalidate the usefulness of averaging, (all sensors of a given catagory get noise from the same source so averaging doesn't help) eg:
![[Pasted image 20231010140332.png]]

- In the example of a phones magnatomiter, multiple doesn't help since they have the same noise sources from environmental local mag fields, but using a acceleromiter we can determine if changes are caused by rotation OR just noise (Look into Kalman Filters, MATLab has a vid on it):
![[Pasted image 20231010140534.png]]

Sensor invalidation:
- In the event of a single sensor failure, having 3 which take the same measurements allows for one sensors data to be disgarded if it's reading significantly deviates from the other 2 readings