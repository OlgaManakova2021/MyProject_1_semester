# У Вас в некотором банке имеется счет, с которым Вы можете
# совершать операции пополнения и снятия денег.
# Необходимо реализовать класс Account,
# который обеспечивает реализацию затребованной
# операции и после ее выполнения и информирует
# Вас о балансе счета.

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self.history.append([amount, 'Приход'])

    def withdraw(self, amount):
        if self.balance >= amount:
            print(f'Вы потратили со счета {amount} рублей')
            self.balance -= amount
            self.show_balance()
            self.history.append([-amount, 'Расход'])
        else:
            print('\033[31m На Вашем счете недостаточно средств \033[0m')

    def show_balance(self):
        print(f'Баланс Вашего счета {self.balance}')

    def show_history(self):
        print('\nИстория операций')
        for amount, type_transaction in self.history:
            if amount > 0:
                print(f'{type_transaction}:  \033[32m {amount} \033[0m')
            else:
                print(f'{type_transaction}:  \033[31m {amount} \033[0m')


p = Account('Olga', 0)
# p.deposit(500)
# p.withdraw(100)
# p.deposit(1500)
# p.show_history()
p1 = Account('Ivan', 200)
p1.deposit(2500)
p1.withdraw(100)
p1.deposit(13500)
p1.withdraw(6000)
p1.show_history()