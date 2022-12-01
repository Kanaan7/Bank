


def flt(test):
  while True:
   try:
    answer=float(input(test))
    if answer<=0:
      print("insert number greater than 0")
    else:
     return answer
   except:
    print("insert number")
    pass
def int(test):
  while True:
   try:
    answer=int(input(test))
    if answer<=0:
      print("insert number greater than 0")
    else:
     return answer
   except:
    print("insert number")
    pass
class program:
  def showMainMenu():
    choice=input("Select an option Do you want  to choose:\n1.Select Account\n2.Exit\n")
    while   choice!='1' and choice!='2':
     print("Please input one of the given options")
     choice=input("Select an option Do you want  to choose:\n\n1.Select Account\n2.Exit\n")
    return choice
  def showAccountMenu():
     choice2=input("Select an option Do you want  to choose:\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit Account\n")
     while choice2!='1' and choice2!='2' and choice2!='3' and choice2!='4':
        choice2=input("Select an option Do you want  to choose:\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit Account\n")
     return choice2
class bank:
  def __init__(self,ChequeBalance,Name,AccountName,SavingBalance):
   self.ChequeBalance=ChequeBalance
   self.Name=Name
   self.AccountName=AccountName
   self.SavingBalance=SavingBalance
class accounts(bank):

  def searchaccount():
   accNumber=int("What is your account number? (1-5)\n")
   return accNumber

  def getCurrentBalance(self):
   bal=input("")
  
  def deposit(AccountBalance):
    AccountBalance+=flt(" deposit\n")
    print("Youre new balance is", AccountBalance)
    return AccountBalance
  def widthdraw(AccountBalance):
   if AccountChoice=='1':
    widthdrawamount=(flt("insert amount you want to widthdraw\n"))
    while int(AccountBalance)-widthdrawamount<=5000:
     print("Your savings account requires a minimum balance of $5000\nIf you would like to cancel the widthdraw, type 'exit', otherwise,please try again")
     widthdrawamount=(flt("insert amount you want to widthdraw\n"))
    else:
     AccountBalance-=widthdrawamount
     print("Your savings balance is", AccountBalance)
     return int(AccountBalance)
   if AccountChoice=="2":
    widthdrawamount=flt("insert amount you want to withdraw\n")
    while widthdrawamount>AccountBalance+5000:
      widthdrawamount= flt("You may widthdraw up to $5000 over your current chequing balance\nIf you would like to cancel the widthdraw, type 'exit', otherwise,please try again\n")
    else:
     AccountBalance-=widthdrawamount
    print("Your chequing balance is", AccountBalance)
    return int(AccountBalance)
    



acc1=(20000,'Jack',1,10000)
acc2=(30000,'Harry',2,15000)
acc3=(40000,'Zak',3,20000)
acc4=(50000,'Jake',4,25000)
acc5=(60000,'Kanaan',5,45000)
banklist=[0,acc1,acc2,acc3,acc4,acc5]

while True:
 match program.showMainMenu():
  case '2':
    quit()
  case '1':
   BankAccount= int((accounts.searchaccount()))
   while BankAccount>len(banklist)-1:
    print("This account does not exist within our system please try again")
    BankAccount= int((accounts.searchaccount()))
   accdetails=banklist[BankAccount]
#    for details in accdetails:
   m=accounts(accdetails[0],accdetails[1],accdetails[2],accdetails[3])
   while True:
    match program.showAccountMenu():
     case '1':
       print("Your chequing balance is:",m.ChequeBalance,"\nYour savings balance is:" ,m.SavingBalance,"\nYour total balance is:",m.ChequeBalance+m.SavingBalance)
     case '2':
      AccountChoice=input("Do you want  to deposit to your savings account or your chequings accounts?\nType 1 for savings and 2 for chequing\n")
      while AccountChoice!= '1' and AccountChoice!='2':
        print("Please input one of the given options")
        AccountChoice=input("Do you want  to deposit to your savings account or your chequings accounts?\nType 1 for savings and 2 for chequing\n")
      if AccountChoice=='1':
         m.ChequeBalance=accounts.deposit(m.ChequeBalance)
      if AccountChoice=='2':
         m.SavingBalance=accounts.deposit(m.SavingBalance)
     
     case'3':
      AccountChoice=input("Do you want  to widthdraw your savings account or your chequings accounts?\nType 1 for savings and 2 for chequing\n")
      while AccountChoice!= '1' and AccountChoice!='2':
       print("Please input one of the given options")
       AccountChoice=input("Do you want  to widthdraw your savings account or your chequings accounts?\nType 1 for savings and 2 for chequing\n")
      if AccountChoice=='1':
         m.ChequeBalance=accounts.widthdraw(m.ChequeBalance)
      if AccountChoice=='2':
         m.SavingBalance=accounts.widthdraw(m.SavingBalance)
      
     case '4':
      accdetails=list(accdetails)
      accdetails[0]=m.ChequeBalance
      accdetails[3]=m.SavingBalance
      accdetails=tuple(accdetails)
      banklist[BankAccount]=(accdetails[0],accdetails[1],accdetails[2],accdetails[3])

      break

  case '3':
    exit()

  





