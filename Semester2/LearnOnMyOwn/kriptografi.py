import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = str(self.index) + self.previous_hash + str(self.transactions) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, max_supply):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []
        self.mining_reward = 5
        self.total_supply = 0
        self.max_supply = max_supply

    def create_genesis_block(self):
        return Block(0, "0", [], time.time())

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address):
        if self.total_supply + self.mining_reward > self.max_supply:
            print("Max supply reached. Mining halted.")
            return

        new_block = Block(len(self.chain), self.get_latest_block().hash, self.pending_transactions, time.time())
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

        self.pending_transactions = [
            {"from": "Bitcoin", "to": mining_reward_address, "amount": self.mining_reward}
        ]
        self.total_supply += self.mining_reward

    def create_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Simulasi penggunaan Blockchain dengan koin terbatas
max_supply = 100
my_coin = Blockchain(max_supply)

# Tambahkan beberapa transaksi
my_coin.create_transaction({"from": "Alice", "to": "Bob", "amount": 10})
my_coin.create_transaction({"from": "Bob", "to": "Charlie", "amount": 5})

# Mine blok dan reward miner
while True:
    input()
    # my_coin.mine_pending_transactions("Miner1")

    # Cek status blockchain
    print(f"Total Supply: {my_coin.total_supply}")
    print(f"Blockchain valid: {my_coin.is_chain_valid()}")

    my_coin.mine_pending_transactions("Miner1")

    for block in my_coin.chain:
        print(f"Block {block.index} [Hash: {block.hash}]")
        print(f"Transactions: {block.transactions}\n")
