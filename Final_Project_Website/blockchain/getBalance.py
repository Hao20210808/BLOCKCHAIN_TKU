def getBalance(self, account):
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
