from prescription_data import *

trial_patients = ['Denise', 'Eddie', 'Frank', 'Georgia', 'Kenny']

for t_patient in trial_patients:
    prescription = patients[t_patient]
    # print(f"{t_patient} : {prescription}")
    try:
        prescription.remove(warfarin)  # gets exception if prescription of the patient doesn't contain 'warfarin'
        prescription.add(edoxaban)
    except KeyError:
        print(f"The patient {t_patient} doesn't use the drug {warfarin}")
    print(f"{t_patient} : {prescription}")
