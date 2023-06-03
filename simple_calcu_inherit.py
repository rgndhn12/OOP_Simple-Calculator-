from oop_simplecalcu import Calculator

class SimpleCalcuInherit(Calculator):
    def user_name(self):
        name_user = input(" What is your name? ")
        print(" Hi,", name_user)
    