---
aliases: [""]
tags: []
---

## ROS2 service definition

In [[Robot Operating System 2|ROS2]], service definitions are used to define request-response interactions between nodes. A service allows one [[ROS2 architecture|nodes]] to request a specific action or data from another node, with a clear request and response structure.

A service definition consists of two main components:
- Request: The data that is sent to the service server when a client makes a request. This is typically a set of parameters or arguments needed to execute the service's action.
- Response: The data returned by the service server after it processes the request. This can include the result of the requested action or any feedback that the client node needs.

A service is defined in a .srv file, which includes the request and response message types. For example, a simple service definition could look like this:
```
# Request part
int32 x
int32 y

---
# Response part
int32 sum
```

In this case, the service takes two integers (x and y) as input and returns their sum as the response.

Services are typically used for tasks that require a single, blocking [[ROS2 architecture|service invocation]] between nodes, such as querying data or triggering specific actions that don’t require continuous communication (unlike [[ROS2 architecture|topics]], which are for ongoing data streams).