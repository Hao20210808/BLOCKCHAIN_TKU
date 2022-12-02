def add_transaction_to_block(self, block):
# Get the transaction with highest fee by block_limitation
    self.pending_transactions.sort(key=lambda x: x.fee, reverse=True)
    if len(self.pending_transactions) > self.block_limitation:
        transcation_accepted = self.pending_transactions[:self.block_limitation]
        self.pending_transactions = self.pending_transactions[self.block_limitation:]
    else:
        transcation_accepted = self.pending_transactions
        self.pending_transactions = []
    block.transactions = transcation_accepted

# The carrying capacity of each block has an upper limit, so miners will choose transactions with high handling fees to be processed first according to their own interests, 
# so here we choose the transactions with the highest handling fees to be added to the block first.
