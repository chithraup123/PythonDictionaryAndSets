from prescription_data import *

# if paracetamol[-1] == 'Painkiller':
#     print(paracetamol[0])

patients_uses_painkiller = []
for patient, prescription in patients.items():
    if paracetamol in prescription:
        patients_uses_painkiller.append(patient)
print('The patients who are taking pain killer are: ', ','.join(patient for patient in patients_uses_painkiller))


