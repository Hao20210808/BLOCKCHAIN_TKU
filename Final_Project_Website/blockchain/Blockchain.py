class BlockChain:
    def __init__(self):
        self.adjust_difficulty_blocks = 10
        self.difficulty = 1
        self.block_time = 30
        self.mining_rewards = 10
        self.block_limitation = 32
        self.chain = []
        self.pending_transactions = []

# adjust_difficulty_blocks: 
#   adjust the difficulty every how many blocks

# Difficulty: 
#   It is hoped that the output time of each block should be as consistent as possible. 
#   Therefore, as the number and performance of nonce mining machines change, the mining difficulty must also be adjusted accordingly to maintain the output time in a dynamic balance. 
#   This field represents The current difficulty of the blockchain

# block_time: 
#   ideally how long it takes to produce a block. 
#   When the actual block time is less than the set ideal value, it means that the computing performance is better than the actual need, 
#   so the difficulty must be increased accordingly, and vice versa. Details will be given later There will be further explanations in the teaching.

# miner_rewards: 
#   The amount of rewards for miners. 
#   Miners who dig out new blocks can get rewards, so as to encourage miners to participate in blockchain operations

# block_limitation: 
#   The upper limit of transactions that can be accommodated in each block. 
#   The upper limit exists because when a miner digs out a new nonce, he needs to broadcast all accepted transactions and block data to others, 
#   so if the capacity is too large Conferences cause propagation to be too slow or increase the network speed required by miners to the point where it is not economical.

# chain: 
#   all blocks currently stored in the blockchain

# pending_pranscations: 
#   When a user sends a transaction, because the transaction volume that the blockchain can handle is limited, the transaction will be in the pending state first. 
#   When the transaction volume is too large, the miners will first choose the transaction with high handling fee to process first.
