import random,time
rnd_range = 100
rnd_num = random.randint(1,rnd_range)
score = 0
strike = 0
quit_button = str("Quit").lower().replace(" ","")

def greet(quit_button):
    
    print("Welcome to my guessing game,"+" \n "+"My name is The Provider")
    print("-"*50)
    time.sleep(1)
    
    name = input("Whats is your name?: ")
    
    if name.isalpha():            
        name = name.capitalize()
        print("-"*50)        
        print("Well hey!,",name)
    else:
        print("-"*50)
        print("Shucks I can't really say that")   
    time.sleep(1)
    print("-"*50) 
    print("Type (",quit_button,") at any moment to quit")
    print("-"*50)

def guess(rnd_num,score,rnd_range,strike,quit_button):
    while True:
        score += 1
        guess = input("Guess a number: ").replace(" ","")
        if guess.isalpha():
            end = guess.lower().replace(" ","")
            if end == quit_button:
                quit()
        
        if guess.isdigit():
            num = int(guess)
            if num > rnd_range:
                strike += 1
                print("We only count up till",rnd_range,".That is strike",strike)
                
                if strike >= 5:
                    print("-"*50)
                    print("Good bye :)")
                    quit()
                
                continue
            if num > rnd_num:
                print("-"*5)
                print("Lower than",num)
                print("-"*5)
                continue
            if num < rnd_num:
                print("-"*5)
                print(" Higher than",num)
                print("-"*5)
                continue      
            if num == rnd_num:
                print("-"*50)
                print("Wow correct the number was",rnd_num)
                break
        else:
            print("-"*50)             
            print("Enter a real number")               
            print("-"*50)            
            continue  
    time.sleep(1)
    print("-"*50)       
    print("You Guessed in",score,"!!")
    print("-"*50)
    if strike >= 1:        
        print("With",strike,"Strikes")
        print("-"*50)

greet(quit_button) 
                                                                            
guess(rnd_num,score,rnd_range,strike,quit_button)
