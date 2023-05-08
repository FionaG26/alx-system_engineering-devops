Issue Summary:
If you're a fan of detective stories, you're in for a treat! Join us on a thrilling ride as we uncover the root cause of a recent outage that affected our e-commerce website's login service.

Between 10:00 AM and 11:30 AM EAT on May 6, 2023, the login service of our e-commerce website was down, affecting 50% of our users. Users attempting to log in were met with an error message and unable to access their accounts or complete purchases. 

Luckily, the issue was resolved by rolling back the configuration change and restarting the database. But we're not stopping there! We're taking a series of corrective and preventative measures, including improving monitoring, configuration management, and system redundancy, to ensure this doesn't happen again. So, if you're a fan of thrilling detective stories, or just want to know how we resolved a recent outage, come along for the ride!

Timeline:

    10:00 AM EAT: The issue was detected when our monitoring system reported a sudden spike in error rates for the login service.
    10:02 AM EAT: The engineering team was alerted and began investigating the issue.
    10:05 AM EAT: The team discovered that the login service was not responding to requests, and attempted to restart the service.
    10:10 AM EAT: Restarting the service did not resolve the issue, and the team began investigating further, suspecting a possible database issue.
    10:15 AM EAT: The team discovered that the database server was experiencing high CPU usage and suspected that it might be the root cause of the issue.
    10:20 AM EAT: The team attempted to optimize the database queries and indexes to reduce CPU usage but did not see any significant improvements.
    10:30 AM EAT: The incident was escalated to the senior engineering team and the database administrators.
    10:35 AM EAT: The database administrators discovered that a recent configuration change had caused a deadlock in the database, preventing the login service from accessing it.
    10:40 AM EAT: The configuration change was rolled back, and the database was restarted.
    11:00 AM EAT: The login service was restored, and users were able to log in and complete purchases.
    11:30 AM EAT: The incident was declared resolved.

Root cause and resolution:
The root cause of the issue was a configuration change that caused a deadlock in the database, preventing the login service from accessing it. The deadlock occurred because of a misconfigured database index, which caused queries to be blocked and resulted in high CPU usage. The issue was resolved by rolling back the configuration change and restarting the database.

Corrective and preventative measures:
To prevent similar incidents from happening in the future, the following corrective and preventative measures will be taken:

    Improve monitoring of database performance metrics to detect issues earlier.
    Review and test database configuration changes before deploying them to production.
    Improve documentation and training for database administrators to ensure proper configuration management.
    Add more redundancy and failover mechanisms to the login service to reduce the impact of similar incidents.
    Review the database schema and query patterns to identify and address any potential performance bottlenecks.

In conclusion, the outage of our e-commerce website's login service was caused by a misconfigured database index that resulted in a deadlock and high CPU usage. The incident was resolved by rolling back the configuration change and restarting the database. We will take corrective and preventative measures to improve monitoring, configuration management, and system redundancy to prevent similar incidents in the future.
