# There are two options
# (1) Genesis block -> hash
# (2) -> block -> hash

def add_transaction_to_block(self, block):
    self.pending_transactions.sort(key=lambda x: x.fee, reverse=True)
    
    if len(self.pending_transactions) > self.block_limitation:
        transcation_accepted = self.pending_transactions[:self.block_limitation]
        self.pending_transactions = self.pending_transactions[self.block_limitation:]
    else:
        transcation_accepted = self.pending_transactions
        self.pending_transactions = []

    block.transactions = transcation_accepted
