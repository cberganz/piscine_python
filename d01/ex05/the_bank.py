class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            raise TypeError("Error: Bank: add(): Invalid new_account type.")
        for account in self.accounts:
            if account.name == new_account.name:
                raise Exception("Error: Bank: add(): Account name already exist.")
        self.accounts.append(new_account)

    def is_corrupted(self, account):
        if len(account.__dict__) % 2 == 0:
            return True
        if not hasattr(account, 'name')\
        or not hasattr(account, 'id')\
        or not hasattr(account, 'value'):
            return True
        if not isinstance(account.name, str)\
        or not isinstance(account.id, int)\
        or not isinstance(account.value, (float, int)):
            return True
        check = {'zip': False, 'addr': False}
        for key in account.__dict__.keys():
            if key.startswith('zip'):
                check['zip'] = True
            if key.startswith('addr'):
                check['addr'] = True
            if key.startswith('b'):
                return True
        if not check['zip']:
            return True
        if not check['addr']:
            return True
        return False

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        origin = [x for x in self.accounts if x.name == origin][0]
        dest = [x for x in self.accounts if x.name == dest][0]
        if not origin or not dest:
            return False
        if amount < 0 or amount > origin.value:
            return False
        if self.is_corrupted(origin) or self.is_corrupted(dest):
            return False
        origin.transfer(-amount)
        dest.transfer(amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account = [x for x in self.accounts if x.name == name][0]
        if not account:
            return False
        if not hasattr(account, 'name'):
            account.__dict__['name'] = 'Account_' + str(account.id)
        if not hasattr(account, 'id'):
            account.__dict__['id'] = Account.ID_COUNT
            Account.ID_COUNT += 1
        if not hasattr(account, 'value'):
            account.__dict__['value'] = 0
        check = {'zip': False, 'addr': False}
        for key in list(account.__dict__.keys()):
            if key.startswith('zip'):
                check['zip'] = True
            if key.startswith('addr'):
                check['addr'] = True
            if key.startswith('b'):
                account.__dict__.pop(key)
        if not check['zip']:
            account.__dict__['zip'] = '75017'
        if not check['addr']:
            account.__dict__['addr'] = '96 Boulevard Bessieres'
        lst = ['name', 'id', 'value']
        if len(account.__dict__) % 2 == 0:
            for key in account.__dict__.keys():
                if key not in lst and not key.startswith('zip') and not key.startswith('addr'):
                    account.__dict__.pop(key)
                    break
        return False if self.is_corrupted(account) else True

if __name__ == "__main__":

    print("\n1. First test main")
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation'
    ))
    if bank.transfer('William John', 'Smith Jane', 545.0) is False:
        print('Failed')
    else:
        print('Success')
    print()


    print("\n2. Second test main")
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    ))
    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
        bank.fix_account('William John')
        bank.fix_account('Smith Jane')
    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
    else:
        print('Success')
    print()
