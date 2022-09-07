from bank import Bank 
from bank_account_manager import Bank_Account_Manangement_System
from bank_account_owner import Bank_Account_Owner
from bank_account import Bank_Account

import os
import time
import random
import string


# This is a helper function to clean the terminal command
def clear_screen(sec):
    # clear screen after sec second
    print("Screen cleaning in " + str(sec) +" seconds. ")
    time.sleep(sec)
        
        
    # clean the screen. 
    os.system('cls' if os.name == 'nt' else 'clear')
    



#############################################
#####   Customer User Interface #############
#############################################
def customer_interface(account):
    
    print("Enter one of the commands. ")
    print("   1. Withdraw Amount")
    print("   2. Deposit Amount")
    print("   3. Account Balance")
    
    command = input("Enter your selection:")
    
    if(command == "1"):
        
        amount = input("Enter the amount that you want to withdraw:")
        account.withdraw(float(amount))
        print(account)
        clear_screen(4)

    
    elif(command == "2"):
        
        amount = input("Enter the amount that you want to deposit:")
        account.deposit(float(amount))
        print(account)
        clear_screen(4)
    
    elif(command == "3"):
        
        print(account)
        clear_screen(4)
        
    else:
        print("Unknown Command!")
        clear_screen(4)
        


####################################################
#####   Bank Administration Interface ##############
####################################################  
    
def admin_interface(example_bank_management_sys):
    
    print("Enter one of the commands. ")
    print("   1. Create an Account")
    print("   2. Delete an Account")
    print("   3. Change password of an Account")
    print("   4. Search an Account by Owner's Name")
    
    command = input("Enter your selection:")
    
    
    if(command == "1"):
            
        name = input("Enter Owner's Name: ")
        
        # printing lowercase
        letters = string.ascii_lowercase
        owner_id = ( ''.join(random.choice(letters) for i in range(10)) )
        driver_license = input("Enter Owner's Driver License Number:")
      
        
        bank_account_owner = Bank_Account_Owner(name = name, id=owner_id, driver_license = driver_license )
        print("Owner Created ... ")
        print(bank_account_owner)
        
        # account_id = random.randint(10000, 99999)
        account_id = input("Enter an account ID:")
        print("Generated an account ID " ,account_id )
        
        
        m_account = Bank_Account(account_id)
        password = input("Enter a password for this account:")
    
        m_account.owner = bank_account_owner 
        m_account.password = password
        m_account.balance = 0
    
        example_bank_management_sys.add_account(m_account)
        print(m_account)
        print("Account Added!")


        clear_screen(6)

    
    elif(command == "2"):
        
        account_id = input("Enter the account id you want to delete:")
        
        if(account_id in example_bank_management_sys.accounts.keys()):
            account = example_bank_management_sys.accounts.get(account_id)
            print("Deleting the account ", account)
            example_bank_management_sys.accounts.pop(account_id)
        else:
            print("Account does not exist.")
        

        clear_screen(4)
    
    elif(command == "3"):
        account_id = input("Enter the account id you want to change the password:")
        
        if(account_id in example_bank_management_sys.accounts.keys()):
            account = example_bank_management_sys.accounts.get(account_id)
            print("Changing Password of Account ", account)
            password = input("Enter the new password:")
            account.password = password

            # Set back the account
            example_bank_management_sys.accounts[account.account_id] = account
        
        else:
            print("Account does not exist.")
        

        clear_screen(4)
    
    elif(command == "4"):
            
        name = input("Enter the owner's name: ")
        ac = example_bank_management_sys.get_account_by_name(name)
        if(ac!=None):
            print(ac)
        else:
            print("Account Not found!")    
        clear_screen(6)
        
    else:
        print("Unknown Command!")
        clear_screen(4)
        


#############################
####### Main Function #######
#############################

def main():
    
    example_bank = Bank("Chase", 11100001123123)
    
    example_bank_management_sys = Bank_Account_Manangement_System()
    
    # set the bank management system 
    example_bank.set_bank_manager(example_bank_management_sys)
    

        
         
    
    #########################################
    # Create an axample account
    matt_s_account = Bank_Account("1111")
    matt = Bank_Account_Owner(name = "Matt Doe", id="Owner-1111", driver_license = "xdege23451" )
    
    matt_s_account.owner = matt 
    matt_s_account.password = "1111"
    matt_s_account.balance = 100
    
    example_bank_management_sys.add_account(matt_s_account)
    
    
    matt_s_account.deposit(50)
    matt_s_account.withdraw(25.23)
    #####################################################


    
    flag = True
    
    while(flag):
        print("Welcome to Example Bank!")
        id = input("Enter your Bank ID: ")
        
        if(id.lower() == "admin"):
            password = input("Enter the Administration Password: ")
            if(password.lower() == "admin"):
                # admin functionalities
                print("Welcome to Bank Administration Console!")
                admin_interface(example_bank_management_sys)
                
        elif(id.lower() == "quit"):
            flag = False
            break        
        
        elif(id in example_bank_management_sys.accounts.keys()):
 
            customer_account = example_bank_management_sys.accounts.get(id)
            
            # Now ask the password here!
            input_password = input("Enter the account password:")
            
            if(input_password == customer_account.password):
                # Entering the Customer ATM system
                print("Loading Account Data ...  ")
                # simulate that we are loading the data from an external database system ... 
                time.sleep(1)
                print()
                print("--------------")
                print("Welcome " + customer_account.owner.name)
                customer_interface(customer_account)
            else:
                print("Account Password does not match!")
        
        else:
            print("We do not have an Account with this ID.")
    
    
    
    
    



if __name__ == "__main__":
    main()


