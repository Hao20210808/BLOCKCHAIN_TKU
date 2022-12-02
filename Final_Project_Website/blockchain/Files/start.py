def start(self):
    address, private = self.generate_address()
    self.create_genesis_block()
    while(True):            
        # Step1: initialize a transaction
        transaction = block.initialize_transaction(address, 'test123', 1, 1, 'Test')
        if transaction:
            # Step2: Sign your transaction
            signature = block.sign_transaction(transaction, private)
            # Step3: Send it to blockchain
            block.add_transaction(transaction, signature)
        self.mine_block(address)
        print(self.get_balance(address))
        self.adjust_difficulty()

# Start to run the Blockchain
# (1) Open an address, then create the first block. 
# (2) Start to [ mine new blocks → adjust the difficulty ] → [ mine new blocks → adjust the difficulty ] → (repeatedly). 
# In addition, transactions can be initiated in the middle
