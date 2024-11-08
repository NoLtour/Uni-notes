---
aliases: 
tags:
  - NotesPage
---

# ROS Fundamentals Overview

#### Aims
- **Learn the purpose of ROS and ROS2**
  - Understand what ROS (Robot Operating System) is, why it is essential for robotics, and the key differences between ROS and ROS2.
  - Understand why ROS2 was developed, its improvements over ROS, and how it addresses shortcomings in ROS (e.g., real-time, multi-platform support, and DDS communication).

- **The architecture underpinning ROS2**
  - Learn the high-level architecture of ROS2 and what makes it effective for building robotic systems.
    - **Communication**: How ROS2 handles communication using DDS (Data Distribution Service) for more reliable, real-time, and scalable messaging.
    - **Platforms**: What platforms ROS2 can run on (e.g., Linux, Windows, macOS, and embedded systems via micro-ROS).
    - **Safety and real-time requirements**: Why ROS2 is more suitable for real-time and safety-critical applications, with enhanced real-time capabilities.

- **What are packages, nodes, and workspaces in ROS2**
  - Learn the basic components of ROS2:
    - **Packages**: What they are and how they organize ROS2 software.
    - **Nodes**: The smallest unit of execution within ROS2, responsible for specific tasks (e.g., sensor data processing).
    - **Workspaces**: How they manage and compile packages in ROS2.

- **What are topics, services, and actions in ROS2**
  - Understand the communication mechanisms in ROS2:
    - **Topics**: Publish/subscribe communication model for continuous data exchange between nodes.
    - **Services**: Request/response communication for synchronous tasks in ROS2.
    - **Actions**: Long-running tasks with feedback, useful for more complex operations like movement or navigation.

#### Intro and contents
What they are:
- [[Robot Operating System]]
- [[Robot Operating System 2]]

There are lots of similarities between [[Robot Operating System|ROS]] and [[Robot Operating System 2|ROS2]], but we don't really care much about [[Robot Operating System|ROS]] so we focus on [[Robot Operating System 2|ROS2]]'s architecture:
- [[ROS2 layers]]
- [[ROS2 architecture]]
- 


## Expanded articles
