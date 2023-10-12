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

#### 2. Creating a Database with Tables:
 - In MySQL Workbench, type in the [following](https://github.com/Helzheng123/flask_4_databases_mysql_vm/blob/main/MYSQL/hospital.sql):
```
CREATE DATABASE hospital;

USE hospital;

CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    doctor_name VARCHAR(50) NOT NULL,
    specialty VARCHAR(50) DEFAULT 'General Practice'
);

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    primary_doctor_id INT,
    FOREIGN KEY (primary_doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE laboratorytests (
    test_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    test_name VARCHAR(50),
    test_date DATE,
    test_results TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);
```
These tables were created from my [previous repository](https://github.com/Helzheng123/mysql_cloudmanaged_databases).  
 - To insert fake data, type in the [following](https://github.com/Helzheng123/flask_4_databases_mysql_vm/blob/main/MYSQL/populate.sql):
```
INSERT INTO doctors (doctor_name, specialty) VALUES 
('Dr. Olivia Mitchell', 'Cardiology'),
('Dr. Will Davis', 'Dermatology'),
('Dr. Michael Anderson', 'Orthopedics');

INSERT INTO patients (first_name, last_name, date_of_birth, primary_doctor_id) VALUES
('John', 'Doe', '1990-05-15', 1), 
('Jane', 'Hill', '1985-11-22', 2), 
('Michael', 'White', '1978-03-08', 3); 

INSERT INTO laboratorytests (patient_id, doctor_id, test_name, test_date, test_results) VALUES
(1, 1, 'Blood Test', '2023-10-doctorsdoctors10', 'Normal results'),
(2, 2, 'Skin Biopsy', '2023-10-11', 'No abnormalities detected'),
(3, 3, 'X-ray', '2023-10-09', 'No abnormalities detected');
```
 - Go to **Database**--> **Reverse Engineer** to create the ERD diagram.
![image](https://github.com/Helzheng123/flask_4_databases_mysql_vm/assets/123939070/dddfcd88-f1b0-4719-b195-756339d405b4)

#### 3. Integrate with Flask:
 - I used my previous flask deployment templates as an example html file. 

