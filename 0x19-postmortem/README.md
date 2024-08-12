# Postmortem: Nginx Service Outage

## Issue Summary

- **Duration of Outage:**
  - **Start Time:** 2024-08-10, 14:00 UTC
  - **End Time:** 2024-08-10, 15:30 UTC

- **Impact:**
  - During the outage, the primary web service was unavailable to approximately 60% of our users. This resulted in a 40% decrease in page views and affected customer transactions, as users experienced either timeouts or error messages when accessing the site.

- **Root Cause:**
  - The root cause was identified as an incorrect user configuration in the Nginx setup, where the web server was running as the `root` user instead of the `nginx` user, leading to a permissions conflict and service failure when certain scripts attempted to execute.

## Timeline

- **14:00 UTC:** Issue detected by automated monitoring alert indicating a high rate of HTTP 502 errors.
- **14:05 UTC:** On-call engineer received the alert and began investigation.
- **14:10 UTC:** Initial assumption was a network connectivity issue due to similar past incidents.
- **14:20 UTC:** Investigated server logs indicating a permission-denied error related to the Nginx process.
- **14:30 UTC:** Misleading path taken by checking network configurations and firewall settings.
- **14:40 UTC:** Incident escalated to the DevOps team for deeper analysis.
- **15:00 UTC:** Identified the Nginx process running as the `root` user.
- **15:10 UTC:** Reconfigured Nginx to run as the `nginx` user and restarted the service.
- **15:20 UTC:** Verified the resolution and confirmed normal operations were restored.
- **15:30 UTC:** Incident closed after confirming stability and full service restoration.

## Root Cause and Resolution

- **Root Cause:**
  - The root cause was the incorrect configuration of the Nginx process running under the `root` user account. This configuration inadvertently caused a permissions conflict with application scripts requiring lower privilege execution.

- **Resolution:**
  - The resolution involved updating the Nginx configuration file to run the service under the `nginx` user account. The following steps were performed:
    - **Configuration Update:** Modified the `/etc/nginx/nginx.conf` file to change the user from `root` to `nginx`:
      ```bash
      sed -i "s/#user www-data/user nginx/" /etc/nginx/nginx.conf
      ```
    - **Permission Check:** Ensured that file permissions for all necessary directories and files were compatible with the `nginx` user.
    - **Service Restart:** Restarted the Nginx service to apply changes:
      ```bash
      sudo -u nginx service nginx restart
      ```
    - **Verification:** Conducted comprehensive testing to ensure all web functionalities were operational.

## Corrective and Preventative Measures

- **Improvements and Fixes:**
  - **User Configuration Audit:** Conduct an audit of all server configurations to ensure proper user permissions are set.
  - **Enhanced Monitoring:** Implement additional monitoring to detect permission issues promptly.
  - **Training:** Provide team training on user privilege best practices to avoid similar issues in the future.

- **Task List:**
  - Patch the Nginx server configuration to use the `nginx` user.
  - Set up automated alerts for permission-related errors in logs.
  - Review and document current server configurations.
  - Schedule a training session on security and permissions management for the engineering team.

## Conclusion

This incident highlights the importance of proper user privilege management in preventing outages and ensuring system security. Through the lessons learned and corrective actions taken, we aim to prevent similar incidents in the future and enhance our overall system reliability.

## Diagrams and Visuals

Include relevant diagrams and visuals here to help illustrate the incident and solution:

![Diagram 1](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwC7BBlGgMcgm4PCY5b0Y-TPYa0rD6pjoAnA&s)
