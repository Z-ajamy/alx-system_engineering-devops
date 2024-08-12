<!-- 
Online HTML, CSS and JavaScript editor to run code online.
-->
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" href="style.css" />
  <title>Browser</title>
</head>

<body>
  <h1>
    Postmortem: Nginx Configuration Outage.
  </h1>
  <p>
    Our HTML editor updates the webview automatically in real-time as you write code.
  </p>
  <script src="script.js"></script>
</body>

</html><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Postmortem: Nginx Service Outage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
            background-color: #f4f4f9;
            color: #333;
        }

        header {
            background-color: #4a90e2;
            color: #fff;
            padding: 10px;
            text-align: center;
        }

        h1, h2, h3 {
            color: #4a90e2;
        }

        h1 {
            margin-top: 0;
        }

        section {
            margin-bottom: 20px;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
        }

        ul {
            list-style-type: disc;
            padding-left: 20px;
        }

        .timeline {
            list-style-type: none;
            padding-left: 0;
        }

        .timeline li {
            margin-bottom: 10px;
        }

        .images {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }

        .images img {
            max-width: 100%;
            height: auto;
            margin: 0 10px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>

<body>

    <header>
        <h1>Postmortem: Nginx Service Outage</h1>
    </header>

    <section>
      <img src="https://tech.sadaalomma.com/wp-content/uploads/2024/02/f35e5770b916a231a93f14b8c3156c87.png">
        <h2>Issue Summary</h2>
        <p><strong>Duration of Outage:</strong><br>
            <strong>Start Time:</strong> 2024-08-10, 14:00 UTC<br>
            <strong>End Time:</strong> 2024-08-10, 15:30 UTC
        </p>
        <p><strong>Impact:</strong><br>
            During the outage, the primary web service was unavailable to approximately 60% of our users. This resulted
            in a 40% decrease in page views and affected customer transactions, as users experienced either timeouts or
            error messages when accessing the site.
        </p>
        <p><strong>Root Cause:</strong><br>
            The root cause was identified as an incorrect user configuration in the Nginx setup, where the web server
            was running as the <code>root</code> user instead of the <code>nginx</code> user, leading to a permissions
            conflict and service failure when certain scripts attempted to execute.
        </p>
    </section>

    <section>
        <h2>Timeline</h2>
        <ul class="timeline">
            <li><strong>14:00 UTC:</strong> Issue detected by automated monitoring alert indicating a high rate of HTTP
                502 errors.</li>
            <li><strong>14:05 UTC:</strong> On-call engineer received the alert and began investigation.</li>
            <li><strong>14:10 UTC:</strong> Initial assumption was a network connectivity issue due to similar past
                incidents.</li>
            <li><strong>14:20 UTC:</strong> Investigated server logs indicating a permission-denied error related to the
                Nginx process.</li>
            <li><strong>14:30 UTC:</strong> Misleading path taken by checking network configurations and firewall
                settings.</li>
            <li><strong>14:40 UTC:</strong> Incident escalated to the DevOps team for deeper analysis.</li>
            <li><strong>15:00 UTC:</strong> Identified the Nginx process running as the <code>root</code> user.</li>
            <li><strong>15:10 UTC:</strong> Reconfigured Nginx to run as the <code>nginx</code> user and restarted the
                service.</li>
            <li><strong>15:20 UTC:</strong> Verified the resolution and confirmed normal operations were restored.</li>
            <li><strong>15:30 UTC:</strong> Incident closed after confirming stability and full service restoration.</li>
        </ul>
    </section>

    <section>
        <h2>Root Cause and Resolution</h2>
        <p><strong>Root Cause:</strong><br>
            The root cause was the incorrect configuration of the Nginx process running under the <code>root</code> user
            account. This configuration inadvertently caused a permissions conflict with application scripts requiring
            lower privilege execution.
        </p>
        <p><strong>Resolution:</strong><br>
            The resolution involved updating the Nginx configuration file to run the service under the <code>nginx</code>
            user account. The following steps were performed:
        </p>
        <ul>
            <li><strong>Configuration Update:</strong> Modified the <code>/etc/nginx/nginx.conf</code> file to change the
                user from <code>root</code> to <code>nginx</code>:
                <pre><code>sed -i "s/#user www-data/user nginx/" /etc/nginx/nginx.conf</code></pre>
            </li>
            <li><strong>Permission Check:</strong> Ensured that file permissions for all necessary directories and files
                were compatible with the <code>nginx</code> user.</li>
            <li><strong>Service Restart:</strong> Restarted the Nginx service to apply changes:
                <pre><code>sudo -u nginx service nginx restart</code></pre>
            </li>
            <li><strong>Verification:</strong> Conducted comprehensive testing to ensure all web functionalities were
                operational.</li>
        </ul>
    </section>

    <section>
        <h2>Corrective and Preventative Measures</h2>
        <p><strong>Improvements and Fixes:</strong></p>
        <ul>
            <li><strong>User Configuration Audit:</strong> Conduct an audit of all server configurations to ensure proper
                user permissions are set.</li>
            <li><strong>Enhanced Monitoring:</strong> Implement additional monitoring to detect permission issues
                promptly.</li>
            <li><strong>Training:</strong> Provide team training on user privilege best practices to avoid similar issues
                in the future.</li>
        </ul>
        <p><strong>Task List:</strong></p>
        <ul>
            <li>Patch the Nginx server configuration to use the <code>nginx</code> user.</li>
            <li>Set up automated alerts for permission-related errors in logs.</li>
            <li>Review and document current server configurations.</li>
            <li>Schedule a training session on security and permissions management for the engineering team.</li>
        </ul>
    </section>

    <section>
        <h2>Conclusion</h2>
        <p>This incident highlights the importance of proper user privilege management in preventing outages and ensuring
            system security. Through the lessons learned and corrective actions taken, we aim to prevent similar
            incidents in the future and enhance our overall system reliability.
        </p>
    </section>

    <section class="images">
        <h2>Diagrams and Visuals</h2>
        <p>Include relevant diagrams and visuals here to help illustrate the incident and solution:</p>
        <img src="path/to/diagram1.png" alt="Diagram 1">
        <img src="path/to/diagram2.png" alt="Diagram 2">
    </section>

</body>

</html>
