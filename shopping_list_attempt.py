import time
items = []

def add_item(items):
    if "Empty" in items:
        items.remove("Empty")
    add = input("\n"+"Add item: ")
    items.append(add)
    return items        

def remove_item(items):
    remove = input("\n"+"Remove item: ")
    items.remove(remove)
    return items

def display_item(items):
      if items == []:
          items.append("Empty")   
      for item in items:        
              print(item)
      return item
      
def options():     
     while True:                 
          print("Options:"+"\n"+"1.Add Item"+"\n"+"2. Remove Item"+"\n"+"3.Display List"+"\n"+"4.Quit(Q)")
          opt = input("\n"+"Whats would you like to do: ").lower().replace(" ","")                    
                                  
          if opt.isdigit() or opt.isalpha():
                            
              if opt in ["4","quit","q"]:
                  print("\n"+"Quiting"+"."*10)
                  time.sleep(3)
                  print("Bye!")
                  break
             
              if opt in ["1","additem","add"]:
                  add_item(items)
                  proceed = input("Proceed? (Y/N): ").lower().replace(" ","")
                  if proceed.isalpha():                      
                      
                      if proceed == "y":
                          add_item(items)
                          print("\n")
                      if proceed == "n":
                          break
                  else:
                      print("\n"+"Bye!")
                      quit()                  
                    
              if opt in ["2","remove","removeitem"]:
                  remove_item(items)
                  proceed = input("Proceed? (Y/N): ").lower().replace(" ","")
                  if proceed.isalpha():                      
                      
                      if proceed == "y":
                          remove_item(items)
                      if proceed == "n":
                          break
                  else:
                      print("Bye!")
                      quit()                  
             
              if opt in ["3","display","displayitem"]:   
                  print("-"*10+"\n")
                  display_item(items)
                  print("\n"+"-"*10)
                  proceed = input("Proceed? (Y/N): ").lower().replace(" ","")
                  if proceed.isalpha():                      
                      
                      if proceed == "y":
                          print("\n")
                          continue
                      if proceed == "n":
                          break
                  else:
                      print("Bye!")
                      quit()
          
          else:
              print("Not a Valid Option") 
              continue
          
options()

