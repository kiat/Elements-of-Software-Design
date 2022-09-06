from bank_account_owner import Bank_Account_Owner

# Extend this implementation to have Personal Bank Accounts and Corporate Bank Accounts


class Bank_Account:
    
    def __init__(self, account_id):
        self.account_id = account_id
        
    
    def deposit(self, amount) -> None:
        self.__balance = self.__balance + amount
    
    
        
    def withdraw(self, amount) -> None:
        
        if(amount <= self.__balance):
            self.__balance = self.__balance - amount
        else:
            print("Not enough Funds on this account!")
            
    
    @property
    def password(self):
        return self.__password
    
    
    # This is a highly simplified example ... 
    # For example this can only be set by admin or customer after checking the existing password. 
    @password.setter
    def password(self, password) -> None:
       
        self.__password = password
        
        
    @property
    def balance(self) -> float:
        return self.__balance
    
    @balance.setter
    def balance(self, amount) -> None:
        if(amount >= 0):
            self.__balance = amount
        else:
            print("[Error] - Amount should be a postive number.")
    
    @property
    def owner(self) -> Bank_Account_Owner:
        return self.__owner
    
    @owner.setter
    def owner(self, owner) -> None:
        if(owner.driver_license != None):
            self.__owner = owner 
        else:
            print("[Error] - We need to have a driver's license copy of each bank accoount owner.")
            
    
    def __str__(self) -> str:
        return "Owner is: "+ str(self.owner) + "\n" + "Account Balance is: " + str(self.balance)




###########################################################
### This is a simulation run for testing of this class. ###
###########################################################


def main():
    
    matt_s_account = Bank_Account()
    matt = Bank_Account_Owner(name = "Matt", id="m12345", driver_license = "xdege23451" )
    print(matt)
    
    matt_s_account.owner = matt 
    matt_s_account.balance = 100
    print(matt_s_account)
    
    matt_s_account.deposit(50)
    
    print(matt_s_account)
    matt_s_account.withdraw(25.23)
    
    print(matt_s_account)
    
    
    
    
    




if __name__ == "__main__":
    main()
