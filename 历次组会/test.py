class BankAccount:
    def __init__(self, card_number, holder_name, password, balance):
        self.card_number = card_number
        self.holder_name = holder_name
        self.password = password
        self.balance = balance
        self.locked = False
        self.failed_attempts = 0

    def set_holder_name(self, name):
        self.holder_name = name

    def set_password(self, password):
        self.password = password

    def modify_password(self, old_password, new_password):
        if self.password == old_password:
            self.password = new_password
            return True
        return False

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def query_balance(self):
        return self.balance

    def transfer(self, source_account,target_account, amount):
        if self.source_account >= amount:
            self.balance -= amount
            target_account.deposit(amount)
            return True
        return 3

    def lock_account(self):
        self.locked = True

    def unlock_account(self):
        self.locked = False
        self.failed_attempts = 0

    def failed_attempt(self):
        self.failed_attempts += 1
        if self.failed_attempts >= 3:
            self.lock_account()

class BankManagementSystem:
    def __init__(self):
        self.bank_accounts = []
        self.admin_password = "admin123"

    def create_account(self, card_number, holder_name, password, balance):
        account = BankAccount(card_number, holder_name, password, balance)
        self.bank_accounts.append(account)

    def set_holder_name(self, card_number, holder_name):
        account = self.find_account(card_number)
        if account:
            account.set_holder_name(holder_name)
            return True
        return False

    def query_balance(self,card_number):##xxx
        account = self.find_account(card_number)
        if account:
            account.query_balance()
            return True
        return False

    def set_password(self, card_number, password):
        account = self.find_account(card_number)
        if account:
            account.set_password(password)
            return True
        return False

    def modify_password(self, card_number, old_password, new_password):
        account = self.find_account(card_number)
        if account:
            return account.modify_password(old_password, new_password)
        return False

    def deposit(self, card_number, amount):
        account = self.find_account(card_number)
        if account:
            if account.locked == True:
                return 0
            else:
                account.deposit(amount)
                return 1
        return 2

    def withdraw(self, card_number, amount):
        account = self.find_account(card_number)
        if account:
            if account.locked == True:
                return 0
            else:
                if account.withdraw(amount):
                    return 1
                else:
                    return 3
        return 2

    def transfer(self, source_card_number, target_card_number, amount):
        source_account = self.find_account(source_card_number)
        target_account = self.find_account(target_card_number)
       # if source_account.locked == True or target_account.locked == True:
        #    return 0
        #elif source_account and target_account:
        #    return source_account.transfer(source_account,target_account, amount)
        #return 2
        if source_account == None or target_account == None:
            return 0
        if source_account.locked == True or target_account.locked == True:
            return 0
        if source_account.transfer(source_account,target_account, amount) == 3:
            return 0
        return 1
        

    def lock_account(self, card_number):
        account = self.find_account(card_number)
        if account:
            account.lock_account()
            return True
        return False

    def unlock_account(self, card_number):
        account = self.find_account(card_number)
        if account:
            account.unlock_account()
            return True
        return False

    def failed_attempt(self, card_number):
        account = self.find_account(card_number)
        if account:
            account.failed_attempt()
            return True
        return False

    def admin_unlock_account(self, card_number):
        account = self.find_account(card_number)
        if account and account.locked:
            account.unlock_account()
            return True
        return False

    def find_account(self, card_number):
        for account in self.bank_accounts:
            if account.card_number == card_number:
                return account
        return None

    def admin_query_all_accounts(self):
        account_info = []
        for account in self.bank_accounts:
            account_info.append(f"持卡人姓名：{account.holder_name}，余额：{account.balance}")
        return account_info

def main_menu():
    bank_management_system = BankManagementSystem()

    while True:
        print("欢迎使用银行管理系统")
        print("1. 创建账户")
        print("2. 设置持卡人姓名")
        print("3. 设置密码")
        print("4. 修改密码")
        print("5. 存款")
        print("6. 取款")
        print("7. 查询余额")
        print("8. 转账")
        print("9. 锁定账户")
        print("10. 解锁账户")
        print("11. 管理员解锁账户")
        print("12. 管理员查询所有账户")
        print("0. 退出系统")

        choice = input("请输入您的选择：")

        if choice == "1":
            card_number = input("请输入卡号：")
            holder_name = input("请输入持卡人姓名：")
            password = input("请输入密码：")
            balance = float(input("请输入初始余额："))
            bank_management_system.create_account(card_number, holder_name, password, balance)
            print("账户创建成功！")

        elif choice == "2":
            card_number = input("请输入卡号：")
            holder_name = input("请输入新的持卡人姓名：")
            if bank_management_system.set_holder_name(card_number, holder_name):
                print("持卡人姓名设置成功！")
            else:
                print("卡号不存在！")

        elif choice == "3":
            card_number = input("请输入卡号：")
            password = input("请输入新的密码：")
            if bank_management_system.set_password(card_number, password):
                print("密码设置成功！")
            else:
                print("卡号不存在！")

        elif choice == "4":
            card_number = input("请输入卡号：")
            old_password = input("请输入原密码：")
            new_password = input("请输入新的密码：")
            if bank_management_system.modify_password(card_number, old_password, new_password):
                print("密码修改成功！")
            else:
                print("卡号或密码错误！")

        elif choice == "5":
            card_number = input("请输入卡号：")
            amount = float(input("请输入存款金额："))
            signal = bank_management_system.deposit(card_number, amount)
            if signal == 1:
                print("存款成功！")
            elif signal == 0:
                print("卡号锁定！")
            else:
                print("卡号不存在！")

        elif choice == "6":
            card_number = input("请输入卡号：")
            amount = float(input("请输入取款金额："))
            signal = bank_management_system.withdraw(card_number, amount)
            if signal == 1:
                print("取款成功！")
            elif signal == 0:
                print("卡号锁定！")
            elif signal == 2:
                print("卡号不存在！")                        
            else:
                print("余额不足！")

        elif choice == "7":
            card_number = input("请输入卡号：")
            balance = bank_management_system.query_balance(card_number)
            if balance is not None:
                print(f"当前余额为：{balance}")
            else:
                print("卡号不存在！")

        elif choice == "8":
            source_card_number = input("请输入转出账号的卡号：")
            target_card_number = input("请输入转入账号的卡号：")
            amount = float(input("请输入转账金额："))
            if bank_management_system.transfer(source_card_number, target_card_number, amount):
                print("转账成功！")
            else:
                print("转出账号或转入账号不存在或余额不足！")

        elif choice == "9":
            card_number = input("请输入卡号：")
            if bank_management_system.lock_account(card_number):
                print("账户已锁定！")
            else:
                print("卡号不存在！")

        elif choice == "10":
            card_number = input("请输入卡号：")
            if bank_management_system.unlock_account(card_number):
                print("账户已解锁！")
            else:
                print("卡号不存在！")

        elif choice == "11":
            admin_password = input("请输入管理员密码：")
            if admin_password == bank_management_system.admin_password:
                card_number = input("请输入要解锁的账号的卡号：")
                if bank_management_system.admin_unlock_account(card_number):
                    print("账户已解锁！")
                else:
                    print("卡号不存在或未被锁定！")
            else:
                print("管理员密码错误！")

        elif choice == "12":
            admin_password = input("请输入管理员密码：")
            if admin_password == bank_management_system.admin_password:
                bank_management_system.admin_query_all_accounts()
            else:
                print("管理员密码错误！")

        elif choice == "0":
            print("谢谢使用，再见！")
            break

        else:
            print("无效的选择，请重新输入！")

if __name__ == "__main__":
    main_menu()

