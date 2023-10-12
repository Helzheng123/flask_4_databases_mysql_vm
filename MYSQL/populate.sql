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
