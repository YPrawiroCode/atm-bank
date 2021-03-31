from credit_card import CREDITCard

class Customer:
    def __init__(self, id, custPin = 112233, custBalance = 10000):
        self.id = id
        self.pin = custPin
        self.balance = custBalance
        
    
    def checkId(self):
        return self.id

    def checkPin(self):
        return self.pin
    
    def checkBalance(self):
        return self.balance  
    
    def withdrawBalance(self, nominal):
        self.balance -= nominal

    def depositBalance(self, nominal):
        self.balance += nominal
    
  
