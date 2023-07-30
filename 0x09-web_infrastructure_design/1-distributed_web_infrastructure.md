# Distributed Web Infrastructure

![Image of a distributed web infrastructure](1-distributed_web_infrastructure.jpg)

## Description

This web infrastructure follows a distributed approach to minimize the load on the primary server. It achieves this by offloading a portion of the traffic to a replica server, which is facilitated by a load balancer responsible for distributing the load between the two servers (primary and replica).

## Specifics About This Infrastructure

 + Load Balancer Algorithm: The HAProxy load balancer is configured with the Round Robin distribution algorithm. This algorithm evenly distributes incoming traffic among the servers in a cyclic manner based on their weights. It ensures a fair distribution of workload, and the server processing time remains balanced. Additionally, the Round Robin algorithm is dynamic, allowing server weights to be adjusted on-the-fly.

 + Load Balancer Setup: The HAProxy load balancer facilitates an Active-Passive setup rather than an Active-Active setup. In an Active-Active setup, the load balancer distributes workloads across all available nodes to prevent any single node from becoming overloaded. This results in improved throughput and response times. Conversely, in an Active-Passive setup, not all nodes are actively receiving workloads at all times. For example, if there are two nodes, one node will be active and processing requests while the other remains passive or on standby. The passive node becomes active only if the preceding active node becomes inactive.

 + Database Primary-Replica Cluster: In a Primary-Replica (Master-Slave) cluster setup, one server acts as the Primary server, and the other server acts as a Replica of the Primary. The Primary server can handle both read and write requests, while the Replica server is limited to processing read requests. Data synchronization occurs between the Primary and Replica servers whenever a write operation is performed on the Primary server.

 + Role of Primary and Replica Nodes: The Primary node is responsible for handling all write operations required by the website. On the other hand, the Replica node primarily deals with read operations, reducing the read traffic directed to the Primary node and helping to distribute the load effectively.

## Issues With This Infrastructure

 + Single Points of Failure (SPOF): The infrastructure contains multiple single points of failure. For instance, if the Primary MySQL database server experiences downtime, the entire site would be affected, and tasks such as user management would be unavailable. Additionally, the server hosting the load balancer and the application server connected to the primary database are also single points of failure.

 + Security Vulnerabilities: Security concerns arise from the lack of SSL encryption for data transmitted over the network, potentially exposing it to interception by hackers. Furthermore, the absence of a firewall on any server makes it impossible to block unauthorized IPs, increasing the risk of unauthorized access.

 + Absence of Monitoring: Currently, there is no monitoring system in place to track the status of each server. As a result, there is no way to proactively identify issues or potential failures, leading to a lack of visibility and control over the infrastructure's health.
