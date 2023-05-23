from oop_simplecalcu import Calculator

calcu = Calculator()
calcu.select_operation

print ( " You may choose your desired Operation!\n A. Addition\n S. Subtraction\n M. Multiplication\n D. Division ")

operation = { "A": calcu.addition, "S": calcu.subtraction, "M": calcu.multiplication, "D": calcu.division} 

while True:
    user_choice = calcu.select_operation()
    if calcu.checking_choice(user_choice):
        num_1, num_2 = calcu.input_number()

        the_result = operation[user_choice](num_1, num_2)
        print( " The result is>>> ", the_result)

        if calcu.try_again():
            continue
    else:
        exit()