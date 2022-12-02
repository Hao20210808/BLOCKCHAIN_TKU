def initialize_transaction(self, sender, receiver, amount, fee, message):
    if self.get_balance(sender) < amount + fee:
        print("Balance not enough!")
        return False
    new_transaction = Transaction(sender, receiver, amount, fee, message)
    return new_transaction

def sign_transaction(self, transaction, private_key):
    private_key_pkcs = rsa.PrivateKey.load_pkcs1(private_key)
    transaction_str = self.transaction_to_string(transaction)
    signature = rsa.sign(transaction_str.encode('utf-8'), private_key_pkcs, 'SHA-1')
    return signature

def add_transaction(self, transaction, signature):
    public_key = '-----BEGIN RSA PUBLIC KEY-----\n'
    public_key += transaction.sender
    public_key += '\n-----END RSA PUBLIC KEY-----\n'
    public_key_pkcs = rsa.PublicKey.load_pkcs1(public_key.encode('utf-8'))
    transaction_str = self.transaction_to_string(transaction)
    if transaction.fee + transaction.amounts > self.get_balance(transaction.sender):
        print("Balance not enough!")
        return False
    try:
        rsa.verify(transaction_str.encode('utf-8'), signature, public_key_pkcs)
        print("Authorized successfully!")
        self.pending_transactions.append(transaction)
        return True
    except Exception:
        print("RSA Verified wrong!")
        
# After generating the public and private keys, first initialize a transaction through initialize_transaction,
# At this time, you can use the get_balance function written yesterday to determine whether the sender's account balance is sufficient.

# After initialization, it can be signed through sign_transaction.
# The two actions of initialize_transaction and sign_transaction are performed on the client's local side to avoid the risk of private key leakage.

# After signing, use add_transaction to send the transaction record and signature to the chain and wait for miners to confirm.
# Because we have signed it, miners can use the public key to decrypt the signature to confirm that the transaction was indeed sent by us.
