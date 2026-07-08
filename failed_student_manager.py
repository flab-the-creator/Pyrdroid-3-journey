from func_of_student import welcome_screen,info,validation,get_mark
import time

welcome_screen()     
time.sleep(0.5)

a = list(info())
name = a[0]
age = a[1]
grade = a[2]

validation(name,age,grade)      

func_of_student.get_mark