# Здесь интерфейс

def get_value():
    print("Hello! Welcome to our caculator.")


    while True:
        kind_operation = input("For complex numbers input 1, for usual numbers input 2: ")
        if kind_operation == "1" or kind_operation == "2":
            break
        print("Your input is incorrect. Try again, please.")
    while True:
        inp = input("Input you operation. Please separate numbers from the sign of operation with space \nFor complex numbers input (1.12,1 + 23.2,12), for usual numbers input (12 + 3) \n: ")


        data = inp.split()

        if len(data) == 3:
            if data[1] == "+" or data[1] == "-" or data[1] == "*" or data[1] == "/":
                print("Thank you!")
                break

        print("Your input is incorrect. Try again, please.")

    return inp, kind_operation

def output(result):
    try:
        if result.is_integer():
            print(f"Your result is:", int(result))
        elif isinstance(result, float):
            print(f"Your result is:", result)
        else:
            print(result)
    except:
        print(result)