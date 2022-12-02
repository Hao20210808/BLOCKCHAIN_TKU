def create_first_block(self):
    print("Create genesis block...")
    new_block = Block('FirstBlock', self.difficulty, 'lkm543', self.miner_rewards)
    new_block.hash = self.get_hash(new_block, 0)
    self.chain.append(new_block)
    
# Since this is our first blockchain, we set the difficulty and mining rewards in the previous_hash field as the default value of the blockchain.
# The miners directly fill in our name here, and directly add the first block to the chain after generating the block.
