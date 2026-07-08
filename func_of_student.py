def welcome_screen():
    print("!Welcome To Student Manager!")
       
def info():
    name = input("Insert Name: ").title()
    age = input("Insert age: ").replace(" ","")
    grade = input("Insert grade(1-12): ").replace(" ","")
    return name,age,grade
   
def validation(name,age,grade):
    while not name.replace(" ","").isalpha():
        print("name must be letters")
        name = input("Insert an appropriate name!!: ") 
        continue
    
    while not age.isdigit() or int(age) >= 100 or int(age) <= 0:
        print("Age Invalid!")
        age = input("Insert valide age: ")
        continue
    
    while not grade.isdigit() or int(grade) >= 13 or int(grade) <= 0:
        print("Grade Invalid")
        grade = input("Insert valid grade!: ")
        continue
   
    return name,age,grade

def get_mark():
    mark = input("Insert student mark: ")
    return mark
