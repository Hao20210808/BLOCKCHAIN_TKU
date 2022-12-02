def get_balance(self, account):
    balance = 0
    for block in self.chain:
        # Check miner reward
        miner = False
        if block.miner == account:
            miner = True
            balance += block.miner_rewards
        for transaction in block.transactions:
            if miner:
                balance += transaction.fee
            if transaction.sender == account:
                balance -= transaction.amounts
                balance -= transaction.fee
            elif transaction.receiver == account:
                balance += transaction.amounts
    return balance

# At the moment of initiating a transaction, it is also necessary to check whether the balance of the remitter is sufficient, and at the same time, it is also restricted that the remittance cannot exceed the balance of its own account, and there are only three sources of account balance in the blockchain:

# Block Reward: 
#   The miner who digs out the block can get the block reward of the block

# Handling fee: 
#   The miner who dug out the block can get the handling fee of all transactions in the block

# Remittance income: 
#   Remittances received from others
