#Dahan, Regine Fae M.    BSCPE 1-5

#introducing the operations

class Calculator():    
    def select_operation(self):
        user_choice = input(" Enter:  A \ S \ M \ D >>>  ").upper()
        return user_choice

#each operation's calculation
    
    #if addition
    def addition(self, num_1, num_2):
            return num_1 + num_2
    
    #if subtraction
    def subtraction(self, num_1, num_2):
            return num_1 - num_2

    #if multiplication
    def multiplication(self, num_1, num_2):
            return num_1 * num_2
    
    #if division
    def division(self, num_1, num_2):
            return num_1 / num_2
    
#user choosing the operation
    def checking_choice(self, user_choice):
        if user_choice in ["A", "S", "M", "D"]:
              return True
        else:
              return False

#user inputting the two numbers    
    def input_number(self):
          num_1 = float(input( " Enter your first number>>> " ))
          num_2 = float(input( " Enter your second number>>> " ))
          return num_1, num_2

#tryagain?
    def try_again(self):
          try_again = input( "PRESS 1 if you want to try again. PRESS 2 if otherwise. ")
          if (try_again == "1"):
            return Calculator
          elif (try_again == "2"):
            print( " THANK YOU FOR USING MY PROGRAM : ) ")
            exit()
          else:
            print( "INVALID." )