from prescription_data import adverse_interactions
from prescription_data import patients

# Prints Patient details where the patient is taking the drug of 'adverse intercation'
########################################################################################
patients_with_drugs_risk = set()
for adverse_drug in adverse_interactions:
    for key, value in patients.items():
        if adverse_drug.issubset(value):
            #print(f"Patient {key} uses adverse drug {adverse_drug}")
            patients_with_drugs_risk.add(key)

print(sorted(patients_with_drugs_risk))