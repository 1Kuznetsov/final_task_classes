from main import Load as Loader

load = Loader()

load.load_hospital_patients('hospital.txt')
for item in range(3):
    print(load.hospital_patients[item])
print(load.hospital_patients)

load.load_ambulatory_patients('ambulatory.txt')
for item in range(3):
    print(load.ambulatory_patients[item])
print(load.ambulatory_patients)

load.load_nurses('nurses.txt')
for item in range(3):
    print(load.nurses[item])
print(load.nurses)

load.load_doctors('doctors.txt')
for item in range(3):
    print(load.doctors[item])
print(load.doctors)
