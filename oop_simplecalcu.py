#Dahan, Regine Fae M.    BSCPE 1-5

#introducing the operations
class Calculator():    
    def select_operation(self):
        user_choice = input(" Enter:  A \ S \ M \ D >>>  ").upper()
        return user_choice

#each operation's calculation
    def addition(self, num_1, num_2):
            return num_1 + num_2

    def subtraction(self, num_1, num_2):
            return num_1 - num_2

    def multiplication(self, num_1, num_2):
            return num_1 * num_2

    def division(self, num_1, num_2):
            return num_1 / num_2
    
#user choosing the operation
    def checking_choice(self, user_choice):
        if user_choice in ["A", "S", "M", "D"]:
              return True
        else:
              return False  
    
    #if addition
        #print sum

    #if subtraction
        #print difference

    #if multiplication
        #print product

    #if division
        #print quotient

#tryagain?