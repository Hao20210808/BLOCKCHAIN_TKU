class Transaction:
    def __init__(self,sender,receiver,amounts,fee,message):
        self.sender = sender
        self.receiver = receiver
        self.amounts = amounts
        self.fee = fee
        self.message = message
        
# sender: 
#   The initiator of the transaction, and at the same time confirm whether the balance under the sender is sufficient

# receiver: 
#   The recipient of the transaction, usually without the user's consent to receive money

# amounts: 
#   the amount of the transaction

# fee: 
#   the amount of handling fee to be paid during the transaction

# message: 
#   Leave information like a note on the transfer, usually for the payee to see
