# Not sure how to create a system for checking citezenship, id and registration, Will fill in example answers.
import time
age = int(input("Age: "))
    
citezenship = True

id = True

registered = True




def voting(age,citezenship,registered,id):

       if age < 18:
         print("VOTING INELLEGIBLE")
         time.sleep(1)
         print("MEET REQUIREMENTS BEFORE RETURN")
         return False
    
       if not citezenship:
                 return False
    
       if not registered:
                 return False
    
       if not id:
                 return False
    
       return True
    
if voting(age,citezenship,registered,id):
    print("Eligable for vote")
