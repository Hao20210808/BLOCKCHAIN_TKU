address, private = block.generate_address()

transaction = block.initialize_transaction(address, 'test123', 1, 1, 'Test')
if transaction:
    signature = block.sign_transaction(transaction, private)
    block.add_transaction(transaction, signature)
    
# Step1: initialize a transaction
# Step2: Sign your transaction
# Step3: Send it to blockchain
