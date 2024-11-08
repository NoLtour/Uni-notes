---
aliases:
  - publish subscribe pattern
tags:
---

## Publish subscribe architecture

#### What it is
The Pub/Sub (Publisher/Subscriber) model is a messaging pattern used in software architecture to facilitate [[asynchronous and synchronous communication|asynchronous communication]] between different components or systems. In this model, publishers produce messages that are then consumed by subscribers. Key points of the Pub/Sub model include:
- Publishers: Entities that generate and send messages.
- Subscribers: Entities that receive and consume messages, in this model they subscribe to the topic rather than the publisher directly.
- Topics: Channels or categories to which messages are published.
- Message Brokers: Intermediaries that manage the routing of messages between publishers and subscribers.

Subscriptions can have different configurations, such as message delivery guarantees (e.g., [[rules for message sends|at-most-once delivery]], [[rules for message sends|at-least-once delivery]]) and acknowledgment mechanisms.

![[What-is-Pub-Sub-Architecture.webp|600]]
#### Why it was introduced
Consider a scenario of synchronous message passing. You have two components in your system that communicate with each other. Let’s call the sender and receiver. The receiver asks for a service from the sender and the sender serves the request and waits for an acknowledgment from the receiver.
- There is another receiver that requests a service from the sender. The sender is blocked since it hasn’t yet received any acknowledgment from the first receiver.
- The sender isn’t able to serve the second receiver which can create problems. To solve this drawback, the Pub-Sub model was introduced.
