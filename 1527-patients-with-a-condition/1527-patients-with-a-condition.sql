# Write your MySQL query statement below
# SELECT patient_id, patient_name, conditions
# FROM Patients WHERE INSTR(CONCAT(' ',conditions), ' DIAB1') > 0
SELECT patient_id, patient_name, conditions
FROM Patients WHERE conditions like '%DIAB1%'
AND conditions NOT LIKE '__DIAB1%'
