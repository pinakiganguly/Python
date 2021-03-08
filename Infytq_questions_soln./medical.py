def max_patients(patient_list,medical_speciality):
    l=[]
    for i in range(0,len(patient_list),2):
        l.append(patient_list[i])
    max_patient=patient_list.index(max(l))
    for k,v in medical_speciality.items():
        if k==patient_list[max_patient+1]:
            speciality=v
    return speciality
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
patient_list=[101,"P",102,"O",302,"P",305,"P"]
print(max_patients(patient_list,medical_speciality))