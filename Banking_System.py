# #Simple Bank System Built With pyOOP.


class operation:
  def __init__(self):
        self.balance = 0
  
  
  def deposit(self): 
    amount= int(input("enter the amount you want to deposit :"))
    self.balance+= amount
    print(f"Deposit has been made :{amount} \nand your balance is :{self.balance}")

  
  def withdraw(self):
    amount= int(input("enter the amount you want to withdraw :"))
    if amount <= self.balance:
        self.balance-= amount
        print(f"Withdrawn: {amount}\nYour balance is now: {self.balance}")
    else:
            print("Insufficient funds.")



class SignUpAndLogIn(operation) :
  
  def sign_up(self):
    self.name = input("weclome! \nto use this bank enter this information : \nenter your name : ")
    self.phone = input("enter your phone : ")
    self.email= input("enter your email : ")
    self.password =input("enter your password : ")


  def log_in(self):
    name= input("To sign in \nenter your name : ")
    password =input("enter your password : ")

    if self.name == name and self.password == password :
      log_in = input("enter 1- deposit 2- withdraw : ")
      if log_in == "1":
        self.deposit()
        new_login = input("did you want to do another operation :( y / n ) ")
        if new_login=="y":
           self.log_in()
        elif new_login=="n":
           print("thanks for use our bank")
        else:
         print("Invalid input.") 


      elif log_in == "2":
        self.withdraw()
        new_login = input("did you want to do another operation :( y / n ) ")
        if new_login=="y":
           self.log_in()
        elif new_login=="n":
           print("thanks for use our bank")
        else:
         print("Invalid input.")
      
      else:
         print("Invalid input.")


    else : 
       print("Name or Password error. try agin ")
       self.log_in() 
    
  def display(self):
    while True:

        display = input("enter 1 - To log In  , 2 - To quit :")
        if display == "1":
           self.log_in()
        
        elif display == "2":
            print("Thanks for using our bank.")
            break
        else:
            print("Invalid input.")


sign = SignUpAndLogIn()
sign.sign_up()
sign.display()
