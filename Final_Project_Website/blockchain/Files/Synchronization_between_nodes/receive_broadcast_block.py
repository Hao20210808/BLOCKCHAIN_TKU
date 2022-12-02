def receive_broadcast_block(self, block_data):
    last_block = self.chain[-1]
    # Check the hash of received block
    if block_data.previous_hash != last_block.hash:
        print("[**] Received block error: Previous hash not matched!")
        return False
    elif block_data.difficulty != self.difficulty:
        print("[**] Received block error: Difficulty not matched!")
        return False
    elif block_data.hash != self.get_hash(block_data, block_data.nonce):
        print(block_data.hash)
        print("[**] Received block error: Hash calculation not matched!")
        return False
    else:
        if block_data.hash[0: self.difficulty] == '0' * self.difficulty:
            for transaction in block_data.transactions:
                self.chain.remove(transaction)
            self.receive_verified_block = True
            self.chain.append(block_data)
            return True
        else:
            print(f"[**] Received block error: Hash not matched by diff!")
            return False

#　Once a new block is received, the content and hash of the block must be verified to confirm that the format of the data is correct and the packaged transaction inside must be removed from the pending transaction pending_transactions, 
#　otherwise the transaction will be deleted execute twice
