class BlockChain:
    def __init__(self):
        self.adjust_difficulty_blocks = 10
        self.difficulty = 1
        self.block_time = 30
        self.mining_rewards = 10
        self.block_limitation = 32
        self.chain = []
        self.pending_transactions = []
