class Block:
    def __init__(self,previous_hash,difficulty,miner,miner_rewards):
        self.previous_hash = previous_hash
        self.hash = ''
        self.difficulty = difficulty
        self.nonce = 0
        self.timestamp = int(time.time())
        self.transactions = []
        self.miner = miner
        self.miner_rewards = miner_rewards
        
# previous_hash: 
#   For encryption, we will use the hash value of the previous block to ensure the security of data on the blockchain

# hash: 
#   the hash value calculated by the current block

# nonce: 
#   The miner found the key that can unlock the previous block lock

# difficulty: 
#   The difficulty used when digging out this block

# timestamp: 
#   It records when the block was generated, and it will be used when adjusting the difficulty of mining

# transactions: 
#   records all transaction records in this block

# miner: 
#   records who mined this block

# miner_rewards: 
#   Records the rewards given to miners when this block is produced
