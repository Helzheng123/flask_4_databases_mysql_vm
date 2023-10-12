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