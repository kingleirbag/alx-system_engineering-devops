# Secured and Monitored Web Infrastructure

![Image of a secured and monitored infrastructure](2-secured_and_monitored_web_infrastructure.jpg)

## Description

This web infrastructure consists of three servers, and it has been designed with security, monitoring, and encryption to ensure robust and reliable performance.


## Specifics About This Infrastructure

 + Load Balancer (HAProxy): The first server in the infrastructure is the load balancer, which efficiently distributes incoming traffic across multiple servers. This setup not only prevents overloading of any single server but also provides high availability by ensuring that if one server fails, the others can still handle incoming requests.

 + Web Server (Nginx): The second server serves as the web server and is responsible for handling HTTP and HTTPS requests. It has been configured to serve encrypted traffic using SSL certificates (HTTPS). This ensures that all data transmitted between the clients and the server is encrypted, safeguarding it from unauthorized access and eavesdropping.

 + Application Server: The third server hosts the application and handles the business logic and data processing. It interacts with the web server to deliver dynamic content to the clients while maintaining a secure and isolated environment.

 #### Security measures:

 + SSL Certificates: The use of SSL certificates on the web server ensures that communication between clients and the server is encrypted, protecting sensitive data from being intercepted.
 + Firewalls: Each server is equipped with firewalls that help prevent unauthorized access and ensure that only legitimate traffic is allowed.
 + Regular Updates: The servers are kept up to date with the latest security patches and software updates to mitigate potential vulnerabilities.

 #### Monitoring:

 + Monitoring System: The infrastructure is monitored using a dedicated monitoring system that constantly checks the health and performance of each server. This enables proactive identification of issues and quick resolution of any potential problems.
 + Alerts and Notifications: The monitoring system is configured to send alerts and notifications to the system administrators if any anomalies or critical events are detected. This ensures timely actions to maintain the infrastructure's stability.
 + With these security, monitoring, and encryption measures in place, the 3-server web infrastructure provides a reliable and secure platform for hosting websites and serving encrypted traffic to clients.

## Issues With This Infrastructure
 + If SSL termination is performed at the load balancer, the communication between the load balancer and the web servers would be left unencrypted.
 + Utilizing a single MySQL server poses scalability challenges and creates a potential single point of failure within the web infrastructure.
 + Employing servers with identical components can result in resource contention, including CPU, Memory, I/O, etc. This contention may lead to suboptimal performance and difficulties in identifying the root cause of issues. Such a configuration lacks easy scalability.
