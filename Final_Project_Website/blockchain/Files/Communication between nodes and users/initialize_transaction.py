class Transaction:
    def __init__(self, sender, receiver, amounts, fee, message):
        self.sender = sender
        self.receiver = receiver
        self.amounts = amounts
        self.fee = fee
        self.message = message

def initialize_transaction(sender, receiver, amount, fee, message):
    # No need to check balance
    new_transaction = Transaction(sender, receiver, amount, fee, message)
    return new_transaction
