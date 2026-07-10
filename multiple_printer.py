multiple = input("What number would you like to be multiplied: ")

while True:
    
    if multiple.isdigit():
        multiple = int(multiple) 
        break
    elif multiple >= 100:
        print("I dont like numbers 100 or bigger")
    else:
       multiple = (input("Number invalid, Add new: "))
       continue
  

                            
for i in range(1,11):
    result = multiple*i
    print(multiple,"×",i,"=",result)
