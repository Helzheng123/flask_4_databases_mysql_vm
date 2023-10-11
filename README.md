# flask_4_databases_mysql_vm

## Guide to this assignment:
#### 1. MySQL Setup on Azure/GCP VM:
 - On your Azure account, create a new virtual machine. Create a new resource group and set the region to **US EAST**. Change the security type to **Standard**. Change the Size to **B1ms**.
 - Set up a username and password under the authentication type. Make sure the price per hour is 0.0207 USD. Once everything is set up, press **create**.
 - Log into your Google Shell and in the terminal, type in ```ssh```.
 - Type in ```ssh [username that you created in azure will be replaced here]@[ip address of your virtual machine]```. There will be a **Are you sure you want to continue connecting (yes/no/[fingerprint])? Type in yes. Then type in your password. This will link you to Ubuntu 20.04.6.
 - Type in ```sudo apt-get update```. It will ask you if you would want to continue. Type in Y.
 - Type in ```sudo mysql``` to enter the MySQL connection.
 - Create a user by typing in ```create user '<user>'@'%' IDENTIFIED BY '<password>';``` You can set the <user> and <password> to your liking.
 - type in ```select user from mysql.user;```. This will show the user you created in the list of users.
 - Now grant privileges to the user you created by typing in ```grant all privileges on *.* to '<user>'@'%' with grant option;```
 - Go back to your virtual machine in Azure and go to **networking**. Click on **Add inbound security rule** and change the Service to MySQL so the Destination Port Ranges will be **3306**.
 - Go back to Google Shell and in the terminal type in ```\quit``` to get out of the mysql connection. Then type in ```sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf``` to enter the nano terminal. Find **bind address** and change it to ```0.0.0.0```. Then Ctrl + O to save, enter, and Ctrl + X to exit.
 - Type in ```/etc/init.d/mysql restart```. Then type in your password for your virtual machine.
 - Open your MySQL Workbench and create a new connection. Input a new connection name and use your virtual machine's **IP address as the Hostname** and **change the user name to the <user> you input before**. Enter your **password from <password> as well**. Test the connection and if successful, click **Ok**. 
