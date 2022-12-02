import hashlib

def transaction_to_string(self, transaction):
    transaction_dict = {
        'sender': str(transaction.sender),
        'receiver': str(transaction.receiver),
        'amounts': transaction.amounts,
        'fee': transaction.fee,
        'message': transaction.message
    }
    return str(transaction_dict)

def get_transactions_string(self, block):
    transaction_str = ''
    for transaction in block.transactions:
        transaction_str += self.transaction_to_string(transaction)
    return transaction_str

def get_hash(self, block, nonce):
    s = hashlib.sha1()
    s.update(
        (
            block.previous_hash
            + str(block.timestamp)
            + self.get_transactions_string(block)
            + str(nonce)
        ).encode("utf-8")
    )
    h = s.hexdigest()
    return h

# A hash function can be thought of as a one-way conversion method that converts an input of any length into a fixed-length output

# The hash function must meet two conditions at the same time:
# (1)The same input value will result in the same output value
# (2)The output hash number cannot be deduced back to the original data

# The following data are concatenated as input to the hash function:
# (1) previous_hash
# (2) timestamp
# (3) transactions
# (4) nonce
