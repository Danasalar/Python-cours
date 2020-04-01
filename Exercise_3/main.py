
from classroom import Student
from classroom import Teacher



me = Student('Dana', 'Salar', 'Automation and robotics')
print('')

print('Student :')
print('')
print('First name  Last name  Subject area')
me.print_name_sub()

print('')

teacher = Teacher('Filipe','Maia','Python programming')
print('Teacher :')
print('')
print('First name  Last name  course')
teacher.print_name_course()
