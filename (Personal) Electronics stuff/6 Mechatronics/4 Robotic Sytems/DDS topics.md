---
aliases: [""]
tags: []
---

## DDS topics

DDS ([[Data Distribution Service]]) Topics are the primary means of communication in DDS-based systems, enabling a publish-subscribe communication model. A DDS topic represents a named channel that publishers use to send data and subscribers use to receive data. Topics define the data type and name, but not the actual content, which allows for scalable, efficient, and flexible communication.

Key aspects of DDS topics:
1) Publish-Subscribe Model: Publishers send data to a topic without knowing who the subscribers are. Subscribers receive data from topics they are interested in, without needing to know the publishers.
2) Data Types: Each topic is associated with a specific data type (e.g., sensor readings, commands), ensuring that only compatible data is exchanged.
3) Quality of Service (QoS): DDS topics allow fine-grained control over communication with settings for reliability, durability, latency, and more, ensuring the system meets specific real-time or fault-tolerance requirements.
4) Decoupling: Topics decouple publishers and subscribers in terms of timing, location, and number, allowing for flexible and scalable systems.

In DDS, topics are crucial for ensuring efficient data exchange in [[distributed applications|distributed]], real-time systems, and their design influences systems like [[Robot Operating System 2|ROS2]] that rely on DDS for communication

