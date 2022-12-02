class BlockChain:
    def __init__(self):
        # For P2P connection
        self.socket_host = "127.0.0.1"
        self.socket_port = int(sys.argv[1])
        self.start_socket_server()
        
# The function of the node is not different from what we wrote before, that is, it needs to:

# (1) Generate public and private keys (wallet address)
# (2) Store transaction records
# (3) Confirm account balance
# (4) Verify the digital signature on the transaction
# (5) Pack transactions and mine new blocks
