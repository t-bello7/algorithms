import datetime

userTime = datetime.datetime.now()
print(userTime)

name = input("What is your name?")
allowedUsers = ['Seyi','Mike','Love']
allowedPasswords = ['passwordSeyi', 'passwordMike', 'passwordLove']


#the code below runs if the name is in the list then if the password is in the list 
# if(name in allowedUsers):
#     password = input("Your password? \n ")

#     if(password == allowedPasswords):
#         print("Welcome %s" %name)
#     else:
#         print("Password Incorrect, Please try again")

# else: 
#     print("Name not found, Please try again")


#the code below runs if the name is in the list and the password is also matching the index of the list 
while(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPasswords[userId]):
        print ('Welcome to %s'% name)
        print ('These are the available options')
        print ('1. Withdrawal')
        print ('2. Cash Deposit')
        print ('3. Complaint')

        selectedOption = int(input("Please select an option:"))

        Withdrawal = 0.0
        bankBalance = 0.0
        exit
        if(selectedOption == 2):
            print ('Your selected option is Cash deposit')
            Deposit = float(input('How much do you want to deposit'))
            bankBalance += Deposit
            print('Your current balance is %s ' %bankBalance)

        elif(selectedOption == 1):
            print ( 'Your selected option is Withdrawl')
            Withdrawal = float(input('How much do you want to withdraw'))
            print('Take out your cash')
     
        elif(selectedOption == 3):
            print ('What issue will you like to report ?')
        else:
            print("Invalid Option selected, please try again")
        
     

    else:
        print("Password Incorrect, please try again")

else:
    print('Name not found, Please Try Again')
    addName = input('Please add your name: ')
    addPassword = input('Please add your password: ')
    allowedUsers.append(addName)
    allowedPasswords.append(addPassword)

