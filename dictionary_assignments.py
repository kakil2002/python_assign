"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""
student={'student_name':'Akil','age':22,'roll_no':102,'class':'Btech','section':'ECE','percentage':77,'college_name':'ysr college'}
print('percentage is:',student['percentage'])

"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys and values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""
students_data = {'students_names': ['Akil','Prasad','Pavan'],'ages':[22,23,24],
                 'roll_nos':(102,64,72),'classes':['Btech','Mtech','Degree'],
                 'sections': ['ECE','EEE','MCA'],'percentages':[77,80,85]}
print('student_3 class is:',students_data['classes'][2])

"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
employees_data={'employee_1':{'employee_name':'Akil','salary':25000,'designation':'Associative 1'},
                'employee_2':{'employee_name':'Prasad','salary':26000,'designation':'Associative 2'},
                'employee_3':{'employee_name':'Pavan','salary':27000,'designation':'Associative 3'},
                'employee_4':{'employee_name':'Vishnu','salary':28000,'designation':'Associative 4'}}
print('3rd employee designation is:',employees_data['employee_3']['designation'])
