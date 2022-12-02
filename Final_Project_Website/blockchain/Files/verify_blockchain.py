def verify_blockchain(self):
    previous_hash = ''
    for idx,block in enumerate(self.chain):
        if self.get_hash(block, block.nonce) != block.hash:
            print("Error:Hash not matched!")
            return False
        elif previous_hash != block.previous_hash and idx:
            print("Error:Hash not matched to previous_hash")
            return False
        previous_hash = block.hash
    print("Hash correct!")
    return True

# In order to prevent the data from being tampered with, 
# it is also necessary to check the correctness of the data from time to time.

# (1) previous_hash
# (2) Timestamp when the block was generated
# (3) all transaction records
# (4) nonce

# Once a certain hash number in the middle is calculated and cannot be retrieved, 
# it means that one of the transaction records has been tampered with.
