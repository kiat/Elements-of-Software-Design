
from bank_account import Bank_Account 

class Bank_Account_Manangement_System:
    
    def __init__(self):
        self.accounts = dict()
        
    def add_account(self, account):
        self.accounts[account.account_id] = account
    
    def del_account(self, account):
        self.accounts.remove(account.account_id)
    
    def get_account_by_id(self, account_id) -> Bank_Account:
        return self.accounts.get(account_id)
    
    
    def get_account_by_name(self, name) -> Bank_Account:
        '''We do a linear search to find the account in our database 
        because we have no other indexing'''
        
        for ac in self.accounts.values():
            if (name == ac.owner.name):
                print("Account found!")
                return ac
                        
        print("Account NOT found!")
        return None
        
        
    
    