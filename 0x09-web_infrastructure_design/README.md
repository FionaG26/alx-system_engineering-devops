Author  : Fiona Githaiga

Task 0:Simple web stack

What is a server?
A server is a hardware(computer), software (program) or a device that sends, stores and receives data. It responds to clients over HTTP requests.

What is the role of the domain name?
A domain name is the address of a speccific website. It helps to locate website addresses using internet protocol.
Domain names are simpler to remember compared to a string of number that make up IP addresses

What type of DNS record www is in www.foobar.com
A record . An A record maps a domain to the physical IP address of the computer hosting that domain. Internet traffic uses the A record to find the computer hosting your domain's DNS settings
What is the role of the web server
A web server is a computer that stores, processes, and delivers website files to web browsers.

What is the role of the application server
Application Server is a type of server designed to install, operate, and host applications.

What is the role of the database
The database is used to store all the information that the user needs to store

What is the server using to communicate with the computer of the user requesting the website
Web browsers and servers communicate using TCP/IP. Hypertext Transfer Protocol is the standard application protocol on top of TCP/IP supporting web browser requests and server responses.

SPOF - A single point of failure (SPOF) is a potential risk posed by a flaw.-  If a part of a system fails, it will stop the entire system from working
Downtime when maintenance needed (like deploying new code web server needs to be restarted) - Since there is only one server, the system has to be shutdown for maintenance
Cannot scale if too much incoming traffic -No possibility to scale the service with additional servers as backup. Leading to a possible breakdown of the web page and client requests, as traffic surpasess servers capacity.

Task 1 :Distributed web infrastructure
For every additional element, why you are adding it

The new configuration is composed of two master-servers and one slave-servers. As the master-servers are going to be working based on a Active-Active set up, their configuration must be identical, therefore we need to add every additional element as the simple web infrastructure we had in the previous point. The load is going to be managed through a load-balancer, which distributes the queries according to a Robin-Round algorithm. Finally an additional server will be needed to serve a replica or slave server, helping to unload the masters servers reading queries.


What distribution algorithm your load balancer is configured with and how it works

My load-balancer is using a Round Robin algorithm distribution. Meaning the queries requested are distributed to every server sequentially one after another. And after sending the request to the last server, the algorithm starts from the first server. This will bring on average and approximately, to a server load distribution of 50% on each of the two servers configuration.

Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both

My load balancer is enabling an Active-Active set up. The Active-Active cluster is typically made up of at least two nodes, both activaley running the same type of services at the same time. Their purpose is to achieve load balancing by distributing tasks to different servers in order to prevent overload. As there are more than one servers (nodes) available to severe, the service time and process throughput can have improvements.

On the other hand the Active-Passive setup, also made up of at least two nodes (servers), however not all nodes are going to be active simultaneously. In this configuration, while one node is active, the other nodes (failover servers) are passively waiting to be active as backup in case the primary server (the one being in use actively) is disconnected or unable to serve.

How a database Primary-Replica (Master-Slave) cluster works

A database Primary-Replica (Master-Replica) is a mechanism which enables data of one database server (the master) to be replicated or to be copied to one or more computers or database servers (the slaves), in order all users share the same level of information. This process leads to a distributed database in which users can quickly access data without interfering with each other.

The database replication process can either be synchronous or asynchronous. In the first one, the replication process is done from the client server to the model server and then replicated to all the replica servers before the client is notified about the data replication. This method of replication may take longer to verify, however all data was copied before proceeding.

As in the asynchronous replication process, replication is done by sending data from the client to the model server, followed by a confirmation order to the client, who finally gives permission of copying to the replicas at an unspecified or monitored pace.


What is the difference between the Primary node and the Replica node in regard to the application
The primary node serves as the keeper of information, here the “real” data is kept, then writing only happens here. On the other hand, reading only occurs in the replica or slave node. This architecture purpose is due to safeguard site reliability. In case a site receives a lot of traffic, a replica node prevents overloading of the master node with reading and writing requests.

2. Secured and monitored web infrastructure

For every additional element, why you are adding it

3 Firewalls: The first Firewall checks the rules after receiving the requests and could deny following requests. The second firewall is working in the server to prevent someone hacking depending of the requests, and the third firewall acts as a circuit-level firewalls, inspect the transaction of the information.

SSL certificate: 1 SSL certificate: is added to secure https protocols and encrypt communication. Then, the ‘plain text’ won’t be easy accessed or viewed by a third person, making the protocol communication and data transfer form the browser and web server more secure.

Why is the traffic served over HTTPS

HTTPS stands for HyperText Transfer Protocol Secure, and the traffic is served in order to bring protection by using the secure port 443, which encrypts outgoing information. Then it is more difficult to spy or get access to the site’s information.

What monitoring is used for

Monitoring is practice used for quality control. monitoring not only helps to make sure to maintain high quality levels, keeping the established standards and consistency, but also to help in the continuous improvement of the resources performance.

The way data monitoring is performed, relies on checking new data against predefined rules and metrics. If data quality anomalies are detected, an alert is sent in order to give information about the metrics and rules violation, so data can be checked.
How the monitoring tool is collecting data

IT monitoring is composed of three parts: 1) Fundation; 2) Software, and 3) Interpretation in order to function.

Foundation: Are related to the infrastructure at its lowest layer of the software stack. This includes physical and virtual devices, such as servers, CPUs and VMs.
Software: The software is the monitoring section which analyzes what is happening in the devices (physical or virtual machines) in terms of CPU usage, load, memory, and running count.
Interpretation: Here is where collected data is turned into metrics and are presented through graphs or data charts (mostly on GUI dashboard). This is often integrated with tools of data visualization to help better understand and do data analytics of performance (Gillis, 2020).

Explain what to do if you want to monitor your web server QPS
Determine the Most Critical KPIs
The first step in server monitoring is determining exactly what data you want to track on each server. Your options here are determined by the functionality that the server provides for your company. You can determine that availability and responsiveness are the most important KPIs for an application server. The most critical factors for a web server are capacity and speed. Latency, data throughput, and data loss may be more important for a data storage server.

Set Baseline KPI Values
After you've identified which KPIs are the most critical, you'll need to assess each server's performance against each KPI metric and establish an acceptable range of values for each KPI. This initial measurement will serve as a baseline against which future server performance will be measured.

Configure Data Collection and Analysis
To pull data from the servers installed in your cloud environment, a server monitoring tool must be properly configured. Server monitoring tools track server activity by streaming event logs, also known as log files, which the server generates automatically. On the server, log files provide information about issues, user activity, and security events. Server monitoring tools track server operating system KPIs such as CPU and memory availability, network connectivity, and disk performance in addition to log files.

Set up Comprehensive and Specific Alerts
After you've set up your data collection and aggregation, you'll need to create an alert system that will notify you and your team when a KPI is breached and your chosen metrics fall below threshold values.

Get Ready to Respond
Finally, you'll need to define your alert response policy and method. Who is in charge of looking into security alerts? Trying to solve operational challenges? What types of alerts require action, and how urgent should that action be? All of these questions must be addressed as you choose how your company will handle various types of event notifications.

Queries per second is a measure of the rate of traffic going in a particular server serving a Web domain. It is an important metric to monitor, because it can help you decide whether to scale the server in order to cope with the demand of usage, and resource requirement so the web page won’t collapse in the future with overload server request.

What Are Website KPIs? display and highlight data related to customer behavior habits, SEO and e-commerce website health.

Issues within the secured and monitored web infrastructure
Why terminating SSL at the load balancer level is an issue
Data that is passing across the network from the load balancer to the App Server are now unencrypted, and that will leave applications vulnerable to Man-in-the-Middle Attack 

Why having only one MySQL server capable of accepting writes is an issue
Automatic failover in case of failure of the master node.

Why having servers with all the same components (database, web server and application server) might be a problem

If the stack combination fails this means the website will be down because the servers have the same stack combination





