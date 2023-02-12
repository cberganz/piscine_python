import time

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
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        if not isinstance(new_account, Account):
            raise TypeError("Error: Bank: add(): Invalid new_account type.")
        if not hasattr(new_account, 'name'):
            raise Exception("Error: Bank: add(): No attribute name found.")
        for account in self.accounts:
            if account.name == new_account.name:
                raise Exception("Error: Bank: add(): Account name already exist.")
        print(new_account.name + ' successfully added.')
        self.accounts.append(new_account)

    def is_corrupted(self, account):
        if len(dir(account)) % 2 == 0:
            print("Error: Bank: is_corrupted(): Even number of attr.")
            return True
        if not hasattr(account, 'name')\
        or not hasattr(account, 'id')\
        or not hasattr(account, 'value'):
            print("Error: Bank: is_corrupted(): name, id, or value not found.")
            return True
        if not isinstance(account.name, str)\
        or not isinstance(account.id, int)\
        or not isinstance(account.value, (float, int)):
            print("Error: Bank: is_corrupted(): Invalid attr type.")
            return True
        check = {'zip': False, 'addr': False}
        for attr in dir(account):
            if attr.startswith('zip'):
                check['zip'] = True
            if attr.startswith('addr'):
                check['addr'] = True
            if attr.startswith('b'):
                print("Error: Bank: is_corrupted(): attr starting with 'b'.")
                return True
        if not check['zip']:
            print("Error: Bank: is_corrupted(): 'zip' not found.")
            return True
        if not check['addr']:
            print("Error: Bank: is_corrupted(): 'addr' not found.")
            return True
        return False

    def transfer(self, origin, dest, amount):
        origin = [x for x in self.accounts if hasattr(x, 'name') and x.name == origin]
        dest = [x for x in self.accounts if hasattr(x, 'name') and x.name == dest]
        if len(origin) == 0 or len(dest) == 0:
            print("Error: Bank: transfer(): Account not found.")
            return False
        if self.is_corrupted(origin[0]) or self.is_corrupted(dest[0]):
            print("Error: Bank: transfer(): Account corrupted.")
            return False
        if amount < 0 or amount > origin[0].value:
            print("Error: Bank: transfer(): Invalid amount.")
            return False
        origin[0].transfer(-amount)
        dest[0].transfer(amount)
        print(origin[0].name + ' has sent ' + str(amount) + '$ to ' + dest[0].name)
        return True

    def fix_account(self, name):
        if not isinstance(name, str):
            print("Error: Bank: fix_account(): name is not a str.")
            return False
        account = [x for x in self.accounts if hasattr(x, 'name') and x.name == name]
        if len(account) == 0:
            print("Error: Bank: fix_account(): Account not found.")
            return False
        account = account[0]
        if not hasattr(account, 'id'):
            account.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if not hasattr(account, 'name'):
            account.name = 'Account_' + str(account.id) + '_recovery'
        if not hasattr(account, 'value'):
            account.value = 0
        check = {'zip': False, 'addr': False}
        for attr in dir(account):
            if attr.startswith('zip'):
                check['zip'] = True
            if attr.startswith('addr'):
                check['addr'] = True
            if attr.startswith('b'):
                delattr(account, attr)
        if not check['zip']:
            account.zip = ''
        if not check['addr']:
            account.addr = ''
        if len(dir(account)) % 2 == 0:
            account.__dict__['fix_even_attr_' + str(int(time.time()))] = 'attr balanced'
        return False if self.is_corrupted(account) else True

if __name__ == "__main__":

    acc_valid_1 = Account('Sherlock Holmes',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=1000.0)
    acc_valid_2 = Account('James Watson',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=25000.0)
    invalid_even = Account("invalid_even",
                           zip='42',
                           do='',
                           addr='boulevard bessieres',
                           value=42)
    invalid_b = Account("invalid_b",
                        zip='1',
                        addr='Mexico',
                        value=42,
                        do='',
                        battr=42)
    invalid_nozip = Account("invalid_nozip",
                            addr='Somewhere in the Milky Way',
                            do='',
                            value=42)
    invalid_noaddr = Account("invalid_noaddr",
                             zip='2',
                             do='',
                             value=42)
    invalid_novalue = Account("invalid_novalue",
                              value=42,
                              zip='1',
                              do='',
                              addr='Mexico')
    invalid_noid = Account("invalid_id",
                           value=42,
                           do='',
                           zip='1',
                           addr='Mexico')
    invalid_noname = Account("invalid_noname",
                             value=42,
                             do='',
                             zip='1',
                             addr='Mexico')

    # add()
    print("\n1. Adding accounts to bank")
    bank = Bank()

    print("\n1.1 Valid cases")
    bank.add(acc_valid_1)
    bank.add(acc_valid_2)
    bank.add(invalid_even)
    bank.add(invalid_b)
    bank.add(invalid_nozip)
    bank.add(invalid_noaddr)
    bank.add(invalid_novalue)
    bank.add(invalid_noname)
    bank.add(invalid_noid)
    delattr(invalid_noname, 'name')
    delattr(invalid_novalue, 'value')
    delattr(invalid_noid, 'id')
    for account in bank.accounts:
        print(account.__dict__)

    print("\n1.2 invalid cases")
    try:
        bank.add(42.0)
        print("Input accepted: fail.")
    except Exception as e:
        print("Error catched: success: " + str(e))
    try:
        bank.add(acc_valid_1)
        print("Input accepted: fail.")
    except Exception as e:
        print("Error catched: success: " + str(e))


    # transfer()
    print("\n2. Tranfer()")

    print("\n2.1 origin or dest not an account")
    if bank.transfer('Sherlock Holmes', 'BLA', 500.0) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")
    if bank.transfer('BLA', 'Sherlock Holmes', 500.0) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")

    print("\n2.2 Negative amount")
    if bank.transfer('James Watson', 'Sherlock Holmes', -42) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")

    print("\n2.3 Bank account too low")
    if bank.transfer('James Watson', 'Sherlock Holmes', 42000) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")

    print("\n2.4 Invalid: even number of attr")
    if bank.transfer('invalid_even', 'Sherlock Holmes', 1) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")

    print("\n2.5 Invalid attr starting with 'b'")
    if bank.transfer('invalid_b', 'Sherlock Holmes', 1) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")

    print("\n2.6 No zip")
    if bank.transfer('invalid_nozip', 'Sherlock Holmes', 1) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")

    print("\n2.7 No addr")
    if bank.transfer('invalid_noaddr', 'Sherlock Holmes', 1) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")

    print("\n2.8 No value")
    if bank.transfer('invalid_novalue', 'Sherlock Holmes', 1) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")

    print("\n2.9 No name")
    if bank.transfer('invalid_noname', 'Sherlock Holmes', 1) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")

    print("\n2.10 No id")
    if bank.transfer('invalid_id', 'Sherlock Holmes', 1) is False:
        print("Error catched: success.")
    else:
        print("Input accepted: fail.")

    print("\n2.11 Valid transfer")
    for account in bank.accounts:
        if hasattr(account, 'name'):
            if account.name == 'Sherlock Holmes' or account.name == 'James Watson':
                print(account.__dict__)
    bank.transfer('Sherlock Holmes', 'James Watson', 500.0)
    for account in bank.accounts:
        if hasattr(account, 'name'):
            if account.name == 'Sherlock Holmes' or account.name == 'James Watson':
                print(account.__dict__)

    print()


    # fix_account()
    print("\n3. fix_account()")

    print("\n3.1 fix invalid_even account")
    if bank.fix_account('invalid_even') is True:
        print("Account fixed: success.")
    else:
        print("Account not fixed: fail.")

    print("\n3.2 fix invalid_b account")
    if bank.fix_account('invalid_b') is True:
        print("Account fixed: success.")
    else:
        print("Account not fixed: fail.")

    print("\n3.3 fix invalid_nozip account")
    if bank.fix_account('invalid_nozip') is True:
        print("Account fixed: success.")
    else:
        print("Account not fixed: fail.")

    print("\n3.4 fix invalid_noaddr account")
    if bank.fix_account('invalid_noaddr') is True:
        print("Account fixed: success.")
    else:
        print("Account not fixed: fail.")

    print("\n3.5 fix invalid_novalue account")
    if bank.fix_account('invalid_novalue') is True:
        print("Account fixed: success.")
    else:
        print("Account not fixed: fail.")

    print("\n3.6 fix invalid_noid account")
    if bank.fix_account('invalid_id') is True:
        print("Account fixed: success.")
    else:
        print("Account not fixed: fail.")

    print("\n3.7 Invalid parameter name: does not exist")
    if bank.fix_account('no') is False:
        print("Account not found: success.")
    else:
        print("Account found: fail.")

    print("\n3.7 Invalid parameter name: not a str")
    if bank.fix_account(42.0) is False:
        print("Error returned: success.")
    else:
        print("No error returned: fail.")

    print()


    # transfert() after fix_account()
    print("\n4. transfert() after fix_account()")

    print("\n4.1 Invalid: even number of attr")
    if bank.transfer('invalid_even', 'Sherlock Holmes', 1) is False:
        print("Error catched: fail.")
    else:
        print("Input accepted: success.")

    print("\n4.2 Invalid attr starting with 'b'")
    if bank.transfer('invalid_b', 'Sherlock Holmes', 1) is False:
        print("Error catched: fail.")
    else:
        print("Input accepted: success.")

    print("\n4.3 No zip")
    if bank.transfer('invalid_nozip', 'Sherlock Holmes', 1) is False:
        print("Error catched: fail.")
    else:
        print("Input accepted: success.")

    print("\n4.4 No addr")
    if bank.transfer('invalid_noaddr', 'Sherlock Holmes', 1) is False:
        print("Error catched: fail.")
    else:
        print("Input accepted: success.")

    print("\n4.5 No value")
    if bank.transfer('Sherlock Holmes', 'invalid_novalue', 1) is False:
        print("Error catched: fail.")
    else:
        print("Input accepted: success.")

    print("\n4.6 No id")
    if bank.transfer('invalid_id', 'Sherlock Holmes', 1) is False:
        print("Error catched: fail.")
    else:
        print("Input accepted: success.")

    print()

    # Tests from subject
    print("\n4. Tests from subject")
    print("\n4.1 First test main")
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

    print("\n4.2 Second test main")
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
