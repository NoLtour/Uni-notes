---
aliases:
  - application layer
  - middleware layer
  - OS layer
  - DDS middleware
tags:
---

## ROS2 layers
![[ROS2_arch.png]]

ROS2 is a modular framework designed for building robotic systems, providing a clear separation between different layers of the system:
- Application Layer: This is where users interact with [[Robot Operating System 2|ROS2]]. It includes nodes, topics, services, actions, and custom components that define the behaviour of the robot. Developers write the robot’s logic here, using tools, libraries, and packages to create applications. (This is the part we do most interaction with!)
- Middleware Layer: The core of ROS2's communication infrastructure, this layer uses DDS (Data Distribution Service) to handle data exchange between nodes. DDS ensures reliable, scalable, and real-time communication, making ROS2 more flexible and adaptable to different use cases, including multi-robot systems and real-time applications.
- OS Layer: This layer consists of the underlying operating system (e.g., Linux, Windows, or macOS), providing the basic system resources, such as memory management, process scheduling, and hardware abstraction. ROS2 operates on top of the OS layer, leveraging its capabilities for execution and communication.

Together, these layers form a flexible, distributed system where the application layer handles the robot’s behaviour, the middleware layer ensures communication, and the OS layer provides the foundational system services.


From an architecture perspective, ROS2 is designed into multiple layers, which is visualized above. Compared with ROS1, the main differences are shown as below:
- ROS1 mainly supports Linux-based operating system. ROS2 provides more portability of deployment on underlying operating systems, such as Linux, Windows, Mac, and RTOS.
- ROS data transport protocol uses TCPROS/UDPROS, and communication is highly dependent on the operation of Master node. Communication in ROS2 is based on [[Data Distribution Service|DDS]] (Data Distribution Service) standard, enhancing fault tolerance capabilities.
- Intra-process in ROS2 provides more optimized transmission mechanism.

