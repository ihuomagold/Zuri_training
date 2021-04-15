class Budget:

    def __init__(self, **categories):
        self.categories = categories
        print(self.categories)

    def deposit(self, amount, category):
        self.categories[category] = self.categories[category] + amount
        print('You have deposited', str(amount), 'naira to ', category)

    def withdraw(self, amount, category):
        if amount <= self.categories[category]:
            self.categories[category] = self.categories[category] - amount
            print(str(amount), "Naira has been withdrawn for", category)
        else:
            print('Insufficient Funds')

    def transfer(self, amount, debit, credit):
        if amount <= self.categories[debit]:
            self.categories[debit] = self.categories[debit] - amount
            self.categories[credit] = self.categories[credit] + amount
            print('You have transferred', str(amount), 'Naira from', debit, 'to', credit)
        else:
            print("Insufficient Funds!")

    def get_balance(self, category):
        print("Your", category, "balance is", str(self.categories[category]))


budget = Budget(food=30000, clothing=8540, entertainment=15000, rent=150000)
budget.deposit(14100, "food")
budget.withdraw(145200, "rent")
budget.transfer(4560, "entertainment", "clothing")
budget.get_balance("entertainment")
