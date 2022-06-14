# Write your MySQL query statement below
SELECT patient_id, patient_name, conditions
FROM Patients WHERE INSTR(CONCAT(' ',conditions), ' DIAB1') > 0
# OR INSTR(conditions, ' DIAB1') > 0