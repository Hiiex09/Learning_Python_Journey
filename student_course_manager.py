# Student Course Manager

students = [
    (1,'Park Von Jae'),
    (2,'Park Nel Son'),
    (3,'Kim Cho Yin')
]

courses = {'Math','Science','English','Cooking'}

enrollments = {1: ['Math','Science'], 2:['English','Science'],3:['Math']}

courses.add('Art')
enrollments[3].append('Art')


invalid_course = 'Cooking'

if invalid_course in courses:
    enrollments[2].append(invalid_course)
else:
    print(f"Course '{invalid_course}' is not available and cannot be added to student 2.")


for student in students:
    student_id, name = student
    student_courses = enrollments.get(student_id, [])
    
    if student_courses:
        course_list = ', '.join(student_courses)
        print(f"{name} is enrolled in: {course_list}")
    else:
        print(f"{name} is not enrolled in any courses.")
