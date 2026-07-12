import time

def get_number():
    while True:
        num = input("What is your number: ")

        if num.isdigit():
            time = int(num)

            if time >= 101:
                print("Number Too Big")
                continue

            if time <= 0:
                print("Number Too Small")
                continue

            break
        else:
            print("Error!")
            continue

    return num

num = int(get_number())

for i in range(num,0,-1):
    print(i)
    time.sleep(1)

print("Hooray!!")
