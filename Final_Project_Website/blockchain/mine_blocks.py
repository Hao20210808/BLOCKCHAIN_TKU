def mine_block(self, miner):
    start = time.process_time()

    last_block = self.chain[-1]
    new_block = Block(last_block.hash, self.difficulty, miner, self.miner_rewards)

    self.add_transaction_to_block(new_block)
    new_block.previous_hash = last_block.hash
    new_block.difficulty = self.difficulty
    new_block.hash = self.get_hash(new_block, new_block.nonce)

    while new_block.hash[0: self.difficulty] != '0' * self.difficulty:
        new_block.nonce += 1
        new_block.hash = self.get_hash(new_block, new_block.nonce)

    time_consumed = round(time.process_time() - start, 5)
    print(f"Hash found: {new_block.hash} @ difficulty {self.difficulty}, time cost: {time_consumed}s")
    self.chain.append(new_block)

# Every time the nonce is changed, a new hash is generated, and then it is confirmed whether it meets the requirements (there are several 0s at the beginning). 

# If it meets the requirements, it means that we have found a compliant nonce value
# If not, keep looking down
