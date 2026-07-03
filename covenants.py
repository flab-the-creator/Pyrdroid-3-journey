#coded in pydroid 03/07/2026 (had to learn eval command for logic)
def calculator_processing(a):
     result = a
     return result

print("This is a basic calculator. " + " Input your calculation in the following notation.(number,operation,number." + " Operations include:+, -, *, **,/,//,%.")  

a = input()

result = calculator_processing(a)
print(eval(result))