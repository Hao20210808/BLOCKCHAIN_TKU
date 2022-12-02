def mine_block(self, miner):
    start = time.process_time()

    last_block = self.chain[-1]
    new_block = Block(last_block.hash, self.difficulty, miner, self.miner_rewards)

    self.add_transaction_to_block(new_block)
    new_block.previous_hash = last_block.hash
    new_block.difficulty = self.difficulty
    new_block.hash = self.get_hash(new_block, new_block.nonce)
    new_block.nonce = random.getrandbits(32)

    while new_block.hash[0: self.difficulty] != '0' * self.difficulty:
        new_block.nonce += 1
        new_block.hash = self.get_hash(new_block, new_block.nonce)
        if self.receive_verified_block:
            print(f"[**] Verified received block. Mine next!")
            self.receive_verified_block = False
            return False

    self.broadcast_block(new_block)

    time_consumed = round(time.process_time() - start, 5)
    print(f"Hash: {new_block.hash} @ diff {self.difficulty}; {time_consumed}s")
    self.chain.append(new_block)
    
# If the verification of the previous step is passed, the mining work on the local side must be suspended and the next new block will be mined directly.

# Therefore, modifying the nonce generation method is no longer unified from 1 to gradually +1, 
# otherwise the node with the highest computing power will always be dug.
