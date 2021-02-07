
""" A hierarchical design is useful in software development, as common functionality can be grouped at the most general level, thereby promoting reuse of code,
while differentiated behaviors can be viewed as extensions of the general case, In
object-oriented programming, the mechanism for a modular and hierarchical organization is a technique known as inheritance. This allows a new class to be defined
based upon an existing class as the starting point. In object-oriented terminology,
the existing class is typically described as the base class, parent class, or superclass, while the newly defined class is known as the subclass or child class.
There are two ways in which a subclass can differentiate itself from its superclass. A subclass may specialize an existing behavior by providing a new implementation that overrides an existing method. A subclass may also extend its
superclass by providing brand new methods."""


class CreditCard:
    """This class will be describing a credit card.
     Credit Card will have BANK NAME, ACCOUNT NUMBER, CARD NUMBER , ACCOUNT HOLDER"""

    def __init__(self, bank_name, card_number, credit_limit, account_holder, account_number):
        self._bank_name = bank_name
        self._card_number = card_number
        self._credit_limit = credit_limit
        self._account_holder = account_holder
        self._account_number = account_number
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

    def get_account_holder(self, name):
        return self._account_holder

    def get_account_number(self):
        return self._account_number

    def get_limit(self):
        return self._credit_limit

    def get_balance(self):
        return self._balance

    def charge(self, new_value):
        """ It charges money from the user based on the new given amount of money"""
        if (new_value + self._balance) > self._credit_limit:
            return False
        else:
            self._credit_limit += new_value
            return True

    def make_payment(self, payment):
        self._balance = self._balance - payment
        return f"CASH OUT: {payment}"

    def __str__(self):
        return f"""BANK NAME: {self._bank_name}
                   ACCOUNT NUMBER: {self._account_number}
                   CARD NUMBER: {self._card_number}
                   ACCOUNT HOLDER: {self._account_holder}
                   CREDIT LIMIT : {self._credit_limit}
                   CURRENT BALANCE: {self._balance}"""


class PredatoryCreditCard(CreditCard):
    """Extension of the credit card instance"""
    def __init__(self, bank_name, card_number, credit_limit, account_holder, account_number, percent_rate):
        """Creating a new predatory credit card instance
        Initial balance is zero

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        account the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        annual percentage rate (e.g., 0.0825 for 8.25% APR)"""
        super().__init__(bank_name, card_number, credit_limit, account_holder, account_number)
        self.percent_rate =  percent_rate

    def charge(self, new_value):
        """ Charge given price to the card, assuming sufficient credit limit
        Return True if charge was processed
        Return False and assess $5 fee if charge is denied"""
        success = super().charge(new_value) #call inherited method from base class
        if not success:
            self._balance += 5      #Access penalty
        else:
            return success          #return success


    def process_month(self):
        """Asses monthly interest on outstanding balance"""
        if self._balance > 0:
            #if positive balance, convert APR to monthly multiplicative factor
            monthly_factor =  pow(1 + self.percent_rate, 1/12)
            self._balance *= monthly_factor





credit =  PredatoryCreditCard("Deutsche Bank",1242414124, 20000,"Orik",24515,2)

