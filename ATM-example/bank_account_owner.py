class Person:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
    
    def __str__(self) -> str:
        return("ID: "+ self.id + " -- Name: " + self.name)


class Bank_Account_Owner(Person):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.driver_license = kwargs.get('driver_license')
    
        
    def __str__(self) -> str:
        return(super().__str__() + " -- Driver License: " +  self.driver_license)


# TODO!
# Extend this to have Corporate Owners and Corporate bank accounts 

    