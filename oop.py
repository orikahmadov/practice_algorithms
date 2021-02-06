class CreditCard:
    """This class will be describing a credit card.
     Credit Card will have BANK NAME, ACCOUNT NUMBER, CARD NUMBER , ACCOUNT HOLDER"""
    def __init__(self,bank_name, card_number,credit_limit, account_holder, account_number):
        self._bank_name =  bank_name
        self._card_number = card_number
        self._credit_limit =  credit_limit
        self._account_holder = account_holder
        self._account_number  =  account_number
        self._balance = 0
    """ 
        john =  CreditCard 
        Bank Name:  John Smith
        Account Number :  120927409812749
        Card Number :  12093241414
    """
    def get_bank_name(self):
        return self._bank_name

    def get_card_number(self):
        return self._card_number

    def get_account_holder(self,name):
        return self._account_holder

    def get_account_number(self):
        return self._account_number

    def get_limit(self):
        return self._credit_limit

    def get_balance(self):
        return self._balance

    def charge(self, new_value):
        """ It charges money from the user based on the new given amount of money"""
        if( new_value + self._balance) > self._credit_limit:
            return False
        else:
            self._credit_limit += new_value
            return True

    def make_payment(self, payment):
        self._balance = self._balance - payment
        return f"CASH OUT: {payment}"


    def __str__(self):
        return     f"""BANK NAME: {self._bank_name}
                   ACCOUNT NUMBER: {self._account_number}
                   CARD NUMBER: {self._card_number}
                   ACCOUNT HOLDER: {self._account_holder}
                   CREDIT LIMIT : {self._credit_limit}
                   CURRENT BALANCE: {self._balance}"""



person1 =  CreditCard("Deutsche Bank", 12421649172, 2000, "Orkhan Ahmadov", 2937612472),
person2 =  CreditCard("Deutsche Bank", 12421649172, 3000, "John Hopkins", 2937612472),
person3 =  CreditCard("CITI BANK", 218371928746, 1000, "John Smith", 2937612472),
person4 =  CreditCard("ACB BANK", 12421649172, 2000, "Lee Adams", 2937612472),
person5 =  CreditCard("Commerz Bank", 12421649172, 1000, "Orkhan Ahmadov", 2937612472),
wallet  =[]
wallet.append(person1)
wallet.append(person2)
wallet.append(person3)
wallet.append(person4)
wallet.append(person5)



    
def find_person(person_name):
    found =  False
    people = []
    person = {}
    while not found:
        found =  False
        for object in wallet:
            for property in object:
                if property._account_holder == person_name:
                    person["Name"] =  property.get_account_holder(person_name)
                    person["Bank Name"] =  property.get_bank_name()
                    person["Balance"] =  property.get_balance()
                    people.append(person)
                    found =  True
                
    else:
        return people



def find_by_bank(bank_name):
    banks = []
    bank = {}
    for object in wallet:
        for property in object:
            if property._bank_name.lower() == bank_name.lower():
                    bank["Bank Name"]  = property.get_bank_name()
                    banks.append(bank)
            else:
                continue
    else:
        return banks

print(find_by_bank("Deutsche Bank"))
                
        
        
