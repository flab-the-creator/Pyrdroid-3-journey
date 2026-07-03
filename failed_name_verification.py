def user_input():
        a = str(input("What is your name?: ")).replace(" ","").capitalize()
        return a
        
def verification(a):
    while not a != a.isalpha():
        print("characters are invalid")
        return user_input()
   
     
    if  len(a) >= 10:
       print("Name too long!")
       return user_input()

a = user_input()

verification(a)      

print(a)
