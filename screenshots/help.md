# Setup Guide with Screenshots

This guide will walk you through setting up a Windows Task Scheduler event that triggers when a failed login attempt (Event ID 4625) occurs, and then executes the script to capture logs/screenshots.  

---

## Step 1 – Open Task Scheduler  
![Step 1](./screenshots/step1.png)  
Open **Task Scheduler** by searching for it in the Windows search bar. Click **Open** to launch it.  

---

## Step 2 – Task Scheduler Dashboard  
![Step 2](./screenshots/step2.png)  
This is the **Task Scheduler** dashboard. From here, click **Create Task…** to begin creating a new scheduled task.  

---

## Step 3 – Adding a New Trigger  
![Step 3](./screenshots/step3.png)  
In the **Triggers** tab, click **New** to add a new trigger for the event.  

---

## Step 4 – Configuring the Trigger  
![Step 4](./screenshots/step4.png)  
- Select **Begin the task: On an event**  
- Under **Log**, choose **Security**  
- Enter **4625** as the Event ID (Failed login attempt)  

Make sure **Enabled** is checked.  

---

## Step 5 – Event Log Selection  
![Step 5](./screenshots/step5.png)  
From the dropdown, select **Security** as the log source to capture failed login events.  

---

👉 Once you finish setting the trigger, you will later configure the **Actions** tab to run your PowerShell script, which in turn executes the Python script.  
