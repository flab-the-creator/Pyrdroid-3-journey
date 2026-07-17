import time

Class = []

def add_student(Class):
    print("Name must not contain special characters and must be under 20 letters"+"\n")
    new_stdt = input("Enter a name: ").strip().title()
    test = new_stdt.replace(" ","") 
    length = len(test)   
    if test.isalpha() and length <= 20:
        Class.append(new_stdt)
        print(f"{new_stdt} was add to the Class")
    else:
        print("Name invalid, Try again")
        return Class
    
def remove_student(Class):
        remove =  input("Who would you like to remove: ").strip().title()
        if remove in Class:
            Class.remove(remove)
            print(f"{remove} has been removed from the Class")
        else:
            print("\n"+"Student not found , No action was taken..."+"\n"+"Make sure of correct spelling.")
            return Class
            
def view_students(Class):
        
        for student in Class:               
               print(Class.index(student) + 1,".",student)
        return Class       
    
def search_students(Class):
     search = input("Who're you looking for: ").strip().title()
     if search in Class:
         print("\n"+f"{search} is in the class")
     else:
         print(search,"was not found in Class"+"\n"+"maybe try viewing students to confirm.") 
     return search
     
def student_count(Class):
    count = 0
    for student in Class:
        count += 1
               
    if count >= 2:         
        print("There are",count,"students in Class")
         
    if count == 1:
        print("There is only",count,"student")
         
    if count <= 0:
        print("There are No students in Class")
    return count

def Exit():
    print("Quiting"+"."*10)
    time.sleep(1)
    print("Done!!")
    quit()
    
def choices():
    print("Choice by number only"+"\n")
    print("1.Add Student"+"\n"+"2.Remove Student"+"\n"+"3.View Student(s)"+"\n"+"4.Search"+"\n"+"5.Student Count"+"\n"+"6.Exit")
    while True:
            choice = input("\n"+"Choose: ") 
            if choice.isdigit():                 
               ch = int(choice) 
            else :
                print("Numbers only")
                continue   
    
            if ch <= 6:
      
                if ch == 1:
                    print("\n"+"-"*10)
                    add_student(Class)
                    continue         
        
                if ch == 2:
                     remove_student(Class)
                     print("\n"+"-"*10)
                     continue
        
                if ch == 3:
                    view_students(Class)
                    print("\n"+"-"*10)
                    continue
        
                if ch == 4:
                    search_students(Class)
                    print("\n"+"-"*10)
                    continue                                                                            
                if ch == 5:
                     student_count(Class)
                     print("\n"+"-"*10)
                     continue                                                                              
                if ch == 6:
                    Exit()
   
            else:       
                 print("Choice is invalid")  
                 continue                                                 

choices()
