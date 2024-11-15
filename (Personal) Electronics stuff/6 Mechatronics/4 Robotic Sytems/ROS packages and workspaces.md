---
aliases:
  - ROS package
  - ROS workspace
tags:
---

## ROS packages and workspaces

#### Overview

These are how we organise the code responsible for constructing our ROS based program:
- Workspaces - These are the top level directories where [[Robot Operating System 2|ROS2]] packages are developed and built. They can hold many packages, generally the "src" sub-folder is where packages are stored
- Packages - These are the fundamental building blocks in [[Robot Operating System 2|ROS2]] which can hold multiple [[ROS2 architecture|nodes]]. Similar concepts exist in JavaScript and python, these are effectively libraries.
- [[ROS2 architecture|node]]s - These are the self contained executable processes which are initiated from the package code.

#### Package architecture
Packages are the main unit for organizing software in ROS. A package may contain ROS runtime processes (nodes), a ROS-dependent library, datasets, configuration files, or anything else that is usefully organized together. Packages are the most atomic build item and release item in ROS. Meaning that the most granular thing you can build and release is a package. 

```lua
my_package/
├── package.xml
├── CMakeLists.txt
├── src/
│   └── my_node.cpp
├── include/
│   └── my_package/
│       └── my_header.h
├── launch/
│   └── my_launch_file.launch.py
├── config/
│   └── my_config.yaml
├── msg/
│   └── MyMessage.msg
└── srv/
    └── MyService.srv
```

The structure of a ROS2 package is something like that. Going into more detail on the purpose of each of these core parts:
- package.xml - Acts as the [[manifest file]] describing the package. It includes metadata such as the package name, version, description, author, and dependencies. The XML structure defines which other packages are required to build and run this package, enabling ROS2’s build system (colcon) to manage dependencies automatically.
- CMakeLists.txt - This file provides instructions to [[CMake]] (the build system) on how to compile and link the code in the package. It specifies the location of source files, any libraries needed, and the target executables or libraries to be created. The CMakeLists.txt file also lists dependencies, ensuring they are linked correctly during compilation.
- src/ - this is where you actually put your code, whether that's python or C++ code.
- include/ - this contains [[header file]] for packages. By convention each package stores it's stuff in "include/{package name}"
- config/ - this includes configuration files, usually [[YAML file]]s. Parameters might include sensor thresholds, PID tuning values, or other customizable settings. These configuration files allow the behavior of nodes to be modified without changing the code, though usually the user defines settings during runtime by passing parameters. 

There are also folders for message definitions:
- msg/ - this contains custom [[ROS2 architecture|message]] definitions. Which specifies the format and datatypes of the content of custom message types.
- srv/ - this contains [[ROS2 service definition]]s. Which are used for request-response interactions between [[ROS2 architecture|nodes]] (see [[ROS2 architecture|service invocation]]).
- action/ - this contains custom [[ROS2 architecture|actions]], which are long running tasks.

Some other bits are:
- tests/ - This is a directory that contains integration tests, far from mandatory but useful for making validation simpler.
- README.md - Very common, generally contains everything the author of the package thinks needs to be communicated to the user for introduction to it's use
- LICENSE - Also very common, defines the terms of the packages use


