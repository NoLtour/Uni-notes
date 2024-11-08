---
aliases:
  - node
  - topic
  - service invocation
  - actions
  - ROS messages
tags:
---

## ROS2 Architecture

### Introduction

The brains of the robot, which we actually write sits in the [[ROS2 layers|application layer]] of [[Robot Operating System 2|ROS2]]. Rather than one monolithic program, it can be thought of as lots of smaller self contained programs each communicating with each other, like computers on a network. 

This is where ROS shines, this format encourages more modular programming which makes code reuse and library integration convenient! Let's more formally define how it works, using proper terms now.

#### Nodes
![[0_n7FfmKCTMjXgD7_V.gif|600]]
These are our [[distributed applications]], how they work can be seen in the diagram, they are processes which receive, transmit and process messages sent across the system. 

Nice thing is that the nodes can all be running on one computer or distributed across a network, allowing us to do anything from a simple robot to a swarm acting as one!

#### Node communication

You can see in the diagram there are a bunch of ways nodes can talk to each other, here we'll describe them. Nodes communicate with each other via Topic, Service Invocation and Actions.

- Topic - The topic based communication has [[publish subscribe architecture]] where the data produced and published by a node is subscribed by more than one node and similarly, one topic data can be produced to more than one node. An important note is that [[publish subscribe architecture||topics]] defined in ROS2 **exactly** match [[DDS topics]].
- Service invocation - Service calls use a [[remote method invocation]] approach from an application developer perspective.
- Actions - Actions are an approach used for long service calls. The client requests an action with goal, the action server starts the long-running process, publishes intermediate results, and reports the final result when the goal is achieved. (These service and actions are also implemented using topics over the DDS middleware.)

Note that an action may "never" terminate, it could be "switch to X mode" which is an action that will continue unless interrupted. 

The decentralized architecture of Topic structure creates advantage in terms of both performance and fault tolerance. In addition, rich quality of service features provided by the DDS middleware have also been a factor that raised the ROS 2 architecture to higher levels.

#### Messages

The data types used in topic communication are called message (Message). These Message data structures basically match the [[DDS topics|DDS]] data types (Type). A sample camera message is given below:
```
sensor_msgs/CameraInfo
Header header
  uint32 seq
  time stamp
  string frame_id
uint32 height
uint32 width
RegionOfInterest roi
  uint32 x_offset
  uint32 y_offset
  uint32 height
  uint32 width
float64[5] D
float64[9] K
float64[9] R
float64[12] P
```

The messages defined in ROS 2 are actually of great importance for interoperability; eg, cameras developed by different companies can be quickly integrated into the system by communicating with standard messages regardless of the model camera. Here, the Node component developed for the relevant camera will convert the camera’s special communication protocol messages into standard DDS data. Preliminary studies can be performed using the camera simulator in the [[Gebazo simulation]].

ROS 2 also effectively uses the [[DDS quality of services|quality of services]] (QOS) defined in the [[ROS2 layers|DDS middleware]]. For example, while continuously updated sensor data is sent unreliably, a command sent to the robot to do a job can be sent reliably. Matching the rich quality of service features in DDS with the topics is an important design decision. Ready-made service quality profiles that can be used according to the type of data are defined and the service quality related to newly defined topics is determined by selecting one of these profiles.

The QOS profiles defined in ROS 2 are known by service, sensor data, parameters and default. For example, the parameters use the reliable service quality value while the sensor data uses the best effort QOS value.