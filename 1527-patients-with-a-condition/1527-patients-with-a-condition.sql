# Write your MySQL query statement below
# SELECT patient_id, patient_name, conditions
# FROM Patients WHERE INSTR(CONCAT(' ',conditions), ' DIAB1') > 0
SELECT patient_id, patient_name, conditions
FROM Patients WHERE (conditions LIKE 'DIAB1%'
OR conditions LIKE '% DIAB1%') AND conditions NOT LIKE '_DIAB1%'