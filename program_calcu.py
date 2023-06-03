from oop_simplecalcu import Calculator
from simple_calcu_inherit import SimpleCalcuInherit

calcu = Calculator()
calcu.select_operation
inherit = SimpleCalcuInherit()

import pyfiglet
import time
import colorama
from colorama import Fore
colorama.init()
print(Fore.LIGHTCYAN_EX+pyfiglet.figlet_format("CALCULATOR",font="stop"))
time.sleep(1)
border = "✪" * 75
border_2 = " 𓇼 " * 25
print(border)
print(Fore.LIGHTMAGENTA_EX+' THIS PROGRAM WILL HELP YOU ADD, SUBTRACT, MULTIPLY or DIVIDE TWO NUMBERS... ')
print(border)
time.sleep(2)


try:
    print ( " You may choose your desired Operation!\n A. Addition\n S. Subtraction\n M. Multiplication\n D. Division ")

    operation = { "A": calcu.addition, "S": calcu.subtraction, "M": calcu.multiplication, "D": calcu.division} 

    while True:
        user_choice = calcu.select_operation()
        if calcu.checking_choice(user_choice):
            num_1, num_2 = calcu.input_number()

            print(Fore.LIGHTYELLOW_EX+pyfiglet.figlet_format("Computing...",font="wavy"))
            time.sleep(4)
            the_result = operation[user_choice](num_1, num_2)
            print(Fore.LIGHTBLUE_EX+ " The RESULT is >>> ", the_result)

            if calcu.try_again():
                continue
        else:
            exit()

except ValueError: 
    print (" ERROR: Make sure you input a number instead of words. ")
except TypeError:
    print (" ERROR: Make sure your input is correct. ")
except ZeroDivisionError:
    print (" ERROR: You cannot divide by 0. ")    
finally:
    print (" Hey, don't forget to smile ; ) ")

    