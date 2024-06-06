import random


class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def receive_coins(self, amount):
        self.balance += amount

    def send_coins(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return 0


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def execute(self):
        sent_amount = self.sender.send_coins(self.amount)
        if sent_amount > 0:
            self.receiver.receive_coins(sent_amount)
            return True
        else:
            return False


class CoinSimulation:
    def __init__(self, initial_coins, users):
        self.total_coins = initial_coins
        self.users = users

    def distribute_initial_coins(self):
        for user in self.users:
            user.receive_coins(self.total_coins // len(self.users))

        # Handle any remaining coins
        remaining_coins = self.total_coins % len(self.users)
        for i in range(remaining_coins):
            self.users[i].receive_coins(1)

    def simulate_transaction(self):
        sender = random.choice(self.users)
        receiver = random.choice(self.users)
        while receiver == sender:
            receiver = random.choice(self.users)

        amount = round(random.uniform(0.0, sender.balance), 2)
        transaction = Transaction(sender, receiver, amount)
        success = transaction.execute()
        return success

    def print_balances(self):
        for user in self.users:
            print(f"{user.name}: {user.balance} Bitcoin or {user.balance * 1000}")


# Initialize simulation
users = [User(f"User_{i}") for i in range(10)]
simulation = CoinSimulation(100, users)
simulation.distribute_initial_coins()

# Simulate transactions
for _ in range(1000):
    simulation.simulate_transaction()

# Print final balances
simulation.print_balances()
