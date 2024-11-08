---
aliases: [""]
tags: []
---

## Remote method invocation

Invoking a method on a remote object is known as remote method invocation (RMI) or remote invocation, and is the object-oriented programming analog of a [[remote procedure call]].

The widely used approach on how to implement the communication channel is realized by using stubs and skeletons. They are generated objects whose structure and behavior depends on chosen communication protocol, but in general provide additional functionality that ensures reliable communication over the network. 

![[Distributed_object_communication.png]]

When a caller wants to perform remote call on the called object, it delegates requests to its stub which initiates communication with the remote skeleton. Consequently, the stub passes caller arguments over the network to the server skeleton. The skeleton then passes received data to the called object, waits for a response and returns the result to the client stub. Note that there is no direct communication between the caller and the called object.