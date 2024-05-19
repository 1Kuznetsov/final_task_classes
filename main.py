import re


class Load:
    """
    Class representing loading data from files
    """

    hospital_patients = []
    ambulatory_patients = []
    nurses = []
    doctors = []
    current_id = 1

    @staticmethod
    def is_int(obj):
        """
        Method that checks that the obj has int type
        :param obj:
        :return: integer obj if type is int and None otherwise
        """

        try:
            return int(obj)
        except ValueError:
            return None

    @staticmethod
    def is_bool(obj):
        """
        Method that checks that the obj has bool type
        :param obj:
        :return: boolean obj if type is bool and None otherwise
        """

        if obj == 'True':
            return True
        elif obj == 'False':
            return False
        return None

    @staticmethod
    def is_str(obj):
        """
        Method that checks that the obj has string type
        :param obj:
        :return:
        """

        if isinstance(obj, str):
            return obj
        return None

    @staticmethod
    def load_hospital_patients(filename):
        """
        Method of loading data about hospital patients
        :param filename:
        :return:
        """

        with open(filename, 'r', encoding='utf8') as f_hospital:
            for ptr in f_hospital:
                Load.hospital_patients.append(HospitalPatient(Load.current_id, *ptr.split(';')[:-1]))
                Load.current_id += 1

    @staticmethod
    def load_ambulatory_patients(filename):
        """
        Method of loading data about ambulatory patients
        :param filename:
        :return:
        """

        with open(filename, 'r', encoding='utf8') as f_ambulatory:
            for ptr in f_ambulatory:
                Load.ambulatory_patients.append(AmbulatoryPatient(Load.current_id, *ptr.split(';')[:-1]))
                Load.current_id += 1

    @staticmethod
    def load_nurses(filename):
        """
        Method of loading data about nurses
        :param filename:
        :return:
        """

        with open(filename, 'r', encoding='utf8') as f_nurses:
            for ptr in f_nurses:
                Load.nurses.append(Nurse(Load.current_id, *ptr.split(';')[:-1]))
                Load.current_id += 1

    @staticmethod
    def load_doctors(filename):
        """
        Method of loading data about doctors
        :param filename:
        :return:
        """

        with open(filename, 'r', encoding='utf8') as f_doctors:
            for ptr in f_doctors:
                Load.doctors.append(Doctor(Load.current_id, *ptr.split(';')[:-1]))
                Load.current_id += 1

    @staticmethod
    def print_without_none(output):
        """
        Method of printing output without strings with None
        :param output:
        :return:
        """

        lst_out = output.split('\n')
        for i in range(len(lst_out)-1, -1, -1):
            if 'None' in lst_out[i]:
                lst_out.pop(i)
        return '\n'.join(lst_out)


class Person:
    """
    Class representing a person
    """

    allowed_level_education = ['высшее', 'ср.спец', 'среднее']

    def __init__(self, id, full_name, gender, birthday, place_birth,
                 married, passport, residence_address, level_education,
                 phone_number):
        """
        Sets all the necessary attributes for the class Person
        :param id:
        :param full_name:
        :param gender:
        :param birthday:
        :param place_birth:
        :param married:
        :param passport:
        :param residence_address:
        :param level_education:
        :param phone_number:
        """

        self.__id = Load.is_int(id)
        self.__full_name = Load.is_str(full_name)[:25]

        if gender == 'муж.' or gender == 'жен.':
            self.__gender = gender
        else:
            self.__gender = None

        if re.fullmatch('\d{2}.\d{2}.\d{4}', birthday):
            self.__birthday = birthday
        else:
            self.__birthday = None

        self.place_birth = Load.is_str(place_birth)
        self.married = Load.is_bool(married)

        if re.fullmatch('\d{4} \d{6} \d{2}.\d{2}.\d{4}', passport):
            self.__passport = passport
        else:
            self.__passport = None

        self.residence_address = Load.is_str(residence_address)
        if level_education in Person.allowed_level_education:
            self.__level_education = level_education
        else:
            self.__level_education = None

        if re.fullmatch('\+\d\(\d{3}\)\d{3}-\d{2}-\d{2}', phone_number):
            self.__phone_number = phone_number
        else:
            self.__phone_number = None

    @property
    def id(self):
        return self.__id

    @property
    def full_name(self):
        return self.__full_name

    @property
    def gender(self):
        return self.__gender

    @property
    def birthday(self):
        return self.__birthday

    @property
    def passport(self):
        return self.__passport

    @property
    def level_education(self):
        return self.__level_education

    @property
    def phone_number(self):
        return self.__phone_number

    def __str__(self):
        """
        Method of presenting data for printing data of class Person
        :return: data in appropriate format of class Person
        """

        output = f'''
Номер: {self.id}
ФИО: {self.full_name}
Пол: {self.gender}
Дата рождения: {self.birthday}
Место рождения: {self.place_birth}
В браке: {'да' if self.married == True else 'нет' if self.married == False
        else None }
Паспорт: {self.passport}
Адрес регистрации: {self.residence_address}
Уровень образования: {self.level_education}
Телефон: {self.phone_number}'''

        return Load.print_without_none(output)

    def __repr__(self):
        """
        Method of representing data of class Person
        :return: class data
        """

        return f'{self.id}. {self.full_name}'


class Employee(Person):
    """
    Class representing an employee
    """

    professions_allowed = ['врач', 'медицинская сестра']

    def __init__(self, id, full_name, gender, birthday, place_birth, married,
                 passport, residence_address, level_education, phone_number,
                 know_foreign_language, education_document, year_graduation,
                 qualification, specialty, profession, work_experience):
        """
        Sets all the necessary attributes for the class Employee
        :param id:
        :param full_name:
        :param gender:
        :param birthday:
        :param place_birth:
        :param married:
        :param passport:
        :param residence_address:
        :param level_education:
        :param phone_number:
        :param know_foreign_language:
        :param education_document:
        :param year_graduation:
        :param qualification:
        :param specialty:
        :param profession:
        :param work_experience:
        """

        super().__init__(id, full_name, gender, birthday, place_birth,
                         married, passport, residence_address,
                         level_education, phone_number)

        self.know_foreign_language = Load.is_bool(know_foreign_language)
        self.education_document = Load.is_str(education_document)

        if '1950' <= year_graduation <= '2030':
            self.__year_graduation = int(year_graduation)
        else:
            self.__year_graduation = None

        self.qualification = Load.is_str(qualification)
        self.specialty = Load.is_str(specialty)

        if profession in Employee.professions_allowed:
            self.__profession = profession
        else:
            self.__profession = None

        if 0 <= int(work_experience) <= 60:
            self.__work_experience = int(work_experience)
        else:
            self.__work_experience = None

    @property
    def year_graduation(self):
        return self.__year_graduation

    @property
    def profession(self):
        return self.__profession

    @property
    def work_experience(self):
        return self.__work_experience

    def __str__(self):
        """
        Method of presenting data for printing data of class Employee
        :return: data in appropriate format of class Employee
        """

        output = f'''
Знание иностранного языка: {'да' if self.know_foreign_language else 'нет'}
Документ об образовании: {self.education_document}
Год окончания: {self.year_graduation}
Квалификация: {self.qualification}
Специализация: {self.specialty}
Профессия: {self.profession}
Стаж: {self.work_experience}'''

        return Load.print_without_none(output)

    def __repr__(self):
        """
        Method of representing data of class Employee
        :return: class data
        """

        return f'{self.id}. {self.full_name}'


class Doctor(Employee):
    """
    Class representing a doctor
    """

    category_allowed = ['высшая', 'первая', 'вторая']

    def __init__(self, id, full_name, gender, birthday, place_birth, married,
                 passport, residence_address, level_education, phone_number,
                 know_foreign_language, education_document, year_graduation,
                 qualification, specialty, profession, work_experience,
                 academic_degree, academic_rank, category, trainings,
                 medical_errors, diagnosis_patients, treatment_patients,
                 rehabilitation_patients):
        """
        Sets all the necessary attributes for the class Doctor
        :param id:
        :param full_name:
        :param gender:
        :param birthday:
        :param place_birth:
        :param married:
        :param passport:
        :param residence_address:
        :param level_education:
        :param phone_number:
        :param know_foreign_language:
        :param education_document:
        :param year_graduation:
        :param qualification:
        :param specialty:
        :param profession:
        :param work_experience:
        :param academic_degree:
        :param academic_rank:
        :param category:
        :param trainings:
        :param medical_errors:
        :param diagnosis_patients:
        :param treatment_patients:
        :param rehabilitation_patients:
        """

        super().__init__(id, full_name, gender, birthday, place_birth,
                         married, passport, residence_address,
                         level_education, phone_number, know_foreign_language,
                         education_document, year_graduation, qualification,
                         specialty, profession, work_experience)

        self.academic_degree = Load.is_bool(academic_degree)
        self.academic_rank = Load.is_bool(academic_rank)

        if category in Doctor.category_allowed:
            self.__category = category
        else:
            self.__category = None

        self.trainings = Load.is_bool(trainings)
        self.medical_errors = Load.is_str(medical_errors)
        self.diagnosis_patients = Load.is_bool(diagnosis_patients)
        self.treatment_patients = Load.is_bool(treatment_patients)
        self.rehabilitation_patients = Load.is_bool(rehabilitation_patients)

    @property
    def category(self):
        return self.__category

    def __str__(self):
        """
        Method of presenting data for printing data of class Doctor
        :return: data in appropriate format of class Doctor
        """

        print(Person.__str__(self), end='')
        print(Employee.__str__(self), end='')

        output = f'''
Ученая степень: {'да' if self.academic_degree else 'нет' if
        self.academic_degree == False else None}
Ученое звание: {'да' if self.academic_rank else 'нет' if 
        self.academic_rank == False else None}
Категория: {self.category}
Повышение квалификации: {'да' if self.trainings else 'нет' if 
        self.trainings == False else None}
Врачебные ошибки: {self.medical_errors}
Выполнение диагностики заболеваний: {'да' if self.diagnosis_patients else
        'нет' if self.diagnosis_patients == False else None}
Лечебная практика: {'да' if self.treatment_patients else 'нет' if 
        self.treatment_patients == False else None}
Реабилитация больных: {'да' if self.rehabilitation_patients else 'нет' if
        self.rehabilitation_patients == False else None}'''

        return Load.print_without_none(output)

    def __repr__(self):
        """
        Method of representing data of class Doctor
        :return: class data
        """

        return f'{self.id}. {self.full_name}'


class Nurse(Employee):
    """
    Class representing a nurse
    """

    def __init__(self, id, full_name, gender, birthday, place_birth, married,
                 passport, residence_address, level_education, phone_number,
                 know_foreign_language, education_document, year_graduation,
                 qualification, specialty, profession, work_experience,
                 sanitary_service, patient_care, medical_procedures):
        """
        Sets all the necessary attributes for the class Nurse
        :param id:
        :param full_name:
        :param gender:
        :param birthday:
        :param place_birth:
        :param married:
        :param passport:
        :param residence_address:
        :param level_education:
        :param phone_number:
        :param know_foreign_language:
        :param education_document:
        :param year_graduation:
        :param qualification:
        :param specialty:
        :param profession:
        :param work_experience:
        :param sanitary_service:
        :param patient_care:
        :param medical_procedures:
        """

        super().__init__(id, full_name, gender, birthday, place_birth,
                         married, passport, residence_address,
                         level_education, phone_number, know_foreign_language,
                         education_document, year_graduation, qualification,
                         specialty, profession, work_experience)

        self.sanitary_service = Load.is_bool(sanitary_service)
        self.patient_care = Load.is_bool(patient_care)
        self.medical_procedures = Load.is_bool(medical_procedures)

    def __str__(self):
        """
        Method of presenting data for printing data of class Nurse
        :return: data in appropriate format of class Nurse
        """

        print(Person.__str__(self), end='')
        print(Employee.__str__(self), end='')

        output = f'''
Санитарная обработка помещений: {'да' if self.sanitary_service else 'нет' if 
        self.sanitary_service == False else None}
Уход за больными: {'да' if self.patient_care else 'нет' if 
        self.patient_care == False else None}
Выполнение медицинских процедур: {'да' if self.medical_procedures else 'нет'
        if self.medical_procedures == False else None}'''

        return Load.print_without_none(output)

    def __repr__(self):
        """
        Method of representing data of class Nurse
        :return: class data
        """

        return f'{self.id}. {self.full_name}'


class Patient(Person):
    """
    Class representing a patient
    """

    status_allowed = ['рабочий', 'служащий', 'обучающийся']

    def __init__(self, id, full_name, gender, birthday, place_birth, married,
                 passport, residence_address, level_education, phone_number,
                 medical_policy, status, place_work_study, blood_type,
                 rhesus_affiliation, allergic_reactions):
        """
        Sets all the necessary attributes for the class Patient
        :param id:
        :param full_name:
        :param gender:
        :param birthday:
        :param place_birth:
        :param married:
        :param passport:
        :param residence_address:
        :param level_education:
        :param phone_number:
        :param medical_policy:
        :param status:
        :param place_work_study:
        :param blood_type:
        :param rhesus_affiliation:
        :param allergic_reactions:
        """

        super().__init__(id, full_name, gender, birthday, place_birth,
                         married, passport, residence_address,
                         level_education, phone_number)

        self.medical_policy = Load.is_str(medical_policy)

        if status in Patient.status_allowed:
            self.__status = status
        else:
            self.__status = None

        self.place_work_study = Load.is_str(place_work_study)

        if '1' <= blood_type <= '4':
            self.__blood_type = int(blood_type)
        else:
            self.__blood_type = None

        if rhesus_affiliation in '+-':
            self.__rhesus_affiliation = rhesus_affiliation
        else:
            self.__rhesus_affiliation = None

        self.allergic_reactions = Load.is_str(allergic_reactions)

    @property
    def status(self):
        return self.__status

    @property
    def blood_type(self):
        return self.__blood_type

    @property
    def rhesus_affiliation(self):
        return self.__rhesus_affiliation

    def __str__(self):
        """
        Method of presenting data for printing data of class Patient
        :return: data in appropriate format of class Patient
        """

        output = f'''
Медицинский полис: {self.medical_policy}
Статус: {self.status}
Место работы (учебы): {self.place_work_study}
Группа крови: {self.blood_type}({self.rhesus_affiliation})
Аллергические реакции: {None if self.allergic_reactions == 'Не выявлено' else
        self.allergic_reactions}'''

        return Load.print_without_none(output)

    def __repr__(self):
        """
        Method of representing data of class Patient
        :return: class data
        """

        return f'{self.id}. {self.full_name}'


class AmbulatoryPatient(Patient):
    """
    Class representing an ambulatory patient
    """

    health_group_allowed = ['I', 'II', 'III']

    def __init__(self, id, full_name, gender, birthday, place_birth, married,
                 passport, residence_address, level_education, phone_number,
                 medical_policy, status, place_work_study, blood_type,
                 rhesus_affiliation, allergic_reactions, territorial_number,
                 disability, health_group, chronic_diagnosis):
        """
        Sets all the necessary attributes for the class AmbulatoryPatient
        :param id:
        :param full_name:
        :param gender:
        :param birthday:
        :param place_birth:
        :param married:
        :param passport:
        :param residence_address:
        :param level_education:
        :param phone_number:
        :param medical_policy:
        :param status:
        :param place_work_study:
        :param blood_type:
        :param rhesus_affiliation:
        :param allergic_reactions:
        :param territorial_number:
        :param disability:
        :param health_group:
        :param chronic_diagnosis:
        """

        super().__init__(id, full_name, gender, birthday, place_birth,
                         married, passport, residence_address,
                         level_education, phone_number, medical_policy,
                         status, place_work_study, blood_type,
                         rhesus_affiliation, allergic_reactions,
                         )
        try:
            territorial_number = int(territorial_number)

            if 1 <= territorial_number <= 20:
                self.__territorial_number = territorial_number
            else:
                self.__territorial_number = None

        except ValueError:
            self.__territorial_number = None

        if '0' <= disability <= '3':
            self.__disability = int(disability)
        else:
            self.__disability = None

        if health_group in AmbulatoryPatient.health_group_allowed:
            self.__health_group = health_group
        else:
            self.__health_group = None

        self.chronic_diagnosis = Load.is_str(chronic_diagnosis)

    @property
    def territorial_number(self):
        return self.__territorial_number

    @property
    def disability(self):
        return self.__disability

    @property
    def health_group(self):
        return self.__health_group

    def __str__(self):
        """
        Method of presenting data for printing data of class AmbulatoryPatient
        :return: data in appropriate format of class AmbulatoryPatient
        """

        print(Person.__str__(self), end='')
        print(Patient.__str__(self), end='')

        output = f'''
Участок: {self.territorial_number}
Группа инвалидности: {None if self.disability == 0 else self.disability}
Группа здоровья: {self.health_group}
Хронический диагноз: {None if self.chronic_diagnosis == 'Не выявлено' else
        self.chronic_diagnosis}'''

        return Load.print_without_none(output)

    def __repr__(self):
        """
        Method of representing data of class AmbulatoryPatient
        :return: class data
        """

        return f'{self.id}. {self.full_name}'


class HospitalPatient(Patient):
    """
    Class representing a hospital patient
    """

    hospital_patients = []

    def __init__(self, id, full_name, gender, birthday, place_birth, married,
                 passport, residence_address, level_education, phone_number,
                 medical_policy, status, place_work_study, blood_type,
                 rhesus_affiliation, allergic_reactions, medical_department,
                 room_number, clinic_diagnosis):
        """
        Sets all the necessary attributes for the class HospitalPatient
        :param id:
        :param full_name:
        :param gender:
        :param birthday:
        :param place_birth:
        :param married:
        :param passport:
        :param residence_address:
        :param level_education:
        :param phone_number:
        :param medical_policy:
        :param status:
        :param place_work_study:
        :param blood_type:
        :param rhesus_affiliation:
        :param allergic_reactions:
        :param medical_department:
        :param room_number:
        :param clinic_diagnosis:
        """

        super().__init__(id, full_name, gender, birthday, place_birth, married,
                         passport, residence_address, level_education,
                         phone_number, medical_policy, status,
                         place_work_study, blood_type, rhesus_affiliation,
                         allergic_reactions)

        self.medical_department = Load.is_str(medical_department)
        self.room_number = Load.is_int(room_number)
        self.clinic_diagnosis = Load.is_str(clinic_diagnosis)
        HospitalPatient.hospital_patients.append(f'{self.id}. {self.full_name} ')

    def __str__(self):
        """
        Method of presenting data for printing data of class HospitalPatient
        :return: data in appropriate format of class HospitalPatient
        """

        print(Person.__str__(self), end='')
        print(Patient.__str__(self), end='')

        output = f'''
Отделение: {self.medical_department}
Палата: {self.room_number}
Клинический диагноз: {None if self.clinic_diagnosis == 'Не выявлено'
        else self.clinic_diagnosis}'''

        return Load.print_without_none(output)

    def __repr__(self):
        """
        Method of representing data of class AmbulatoryPatient
        :return: class data
        """

        return f'{self.id}. {self.full_name}'
