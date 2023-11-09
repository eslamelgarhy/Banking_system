# #Simple Bank System Built With pyOOP.


class operation:
  def __init__(self):
        self.balance = 0
  
  
  def deposit(self): 
    amount= int(input("Enter The Amount You Want To Deposit :"))
    self.balance+= amount
    print(f"Deposit Has Been Made :{amount} \nAnd Your Balance Is :{self.balance}")

  
  def withdraw(self):
    amount= int(input("Enter The Amount You Want To Withdraw :"))
    if amount <= self.balance:
        self.balance-= amount
        print(f"Withdrawn: {amount}\nYour Balance Now: {self.balance}")
    else:
            print(f"Insufficient Funds. Available Balance :",self.balance)



class SignUpAndLogIn(operation) :
  
  def sign_up(self):
    self.name = input("Weclome! \nTo Use This Bank Enter This Information : \nEnter Your Name : ")
    self.phone = input("Enter Your Phone : ")
    self.email= input("Enter Your Email : ")
    self.password =input("Enter Your Password : ")


  def log_in(self):
    self.lname= input("To Login \nEnter Your Name : ")
    self.lpassword =input("Enter Your Password : ")
  def continue_operation(self):
        new_ope = input("Did You Want To Do Another Operation :( y / n ) ")
        if new_ope=="Y" or new_ope=="y" :
           self.check_login()
        elif new_ope=="N" or new_ope=="n":
           print("Thanks For Using Our Bank.")
        else:
         print("Invalid Input.")
         self.continue_operation() 
  def check_login(self):
    
    if self.name == self.lname and self.password == self.lpassword :
      ope= input("\nEnter\n\n   1-> Deposit   2-> Withdraw   3-> Show Balance: ")
      if ope == "1":
        self.deposit()
        self.continue_operation()


      elif ope == "2":
        self.withdraw()
        self.continue_operation()

      elif ope =="3":
         print("Available Balance In Your Account Is: ",self.balance)
         self.continue_operation()
      else:
         print("Invalid Input.")
         self.continue_operation()


    else : 
       print("Name Or Password Error. Try Again ")
       
class display(SignUpAndLogIn) :  
  
  def action(self):
    while True:

        display = input("\nEnter\n\n   1-> To log In     2-> To Quit :")
        if display == "1":
           self.log_in()
           self.check_login()
        elif display=="2":
            print("Thanks For Using Our Bank.")
            break
        else:
            print("Invalid Input.")


sign = display()
sign.sign_up()
sign.action()
