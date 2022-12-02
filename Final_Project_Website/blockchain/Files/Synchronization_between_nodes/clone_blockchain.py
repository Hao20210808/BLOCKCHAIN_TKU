def clone_blockchain(self, address):
    print(f"Start to clone blockchain by {address}")
    target_host = address.split(":")[0]
    target_port = int(address.split(":")[1])
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    message = {"request": "clone_blockchain"}
    client.send(pickle.dumps(message))
    response = b""
    print(f"Start to receive blockchain data by {address}")
    while True:
        response += client.recv(4096)
        if len(response) % 4096:
            break
    client.close()
    response = pickle.loads(response)["blockchain_data"]

    self.adjust_difficulty_blocks = response.adjust_difficulty_blocks
    self.difficulty = response.difficulty
    self.block_time = response.block_time
    self.miner_rewards = response.miner_rewards
    self.block_limitation = response.block_limitation
    self.chain = response.chain
    self.pending_transactions = response.pending_transactions
    self.node_address.update(response.node_address)
    
# In order to synchronize with the blockchain that is already in operation, it is necessary to initiate a request to a known node, 
# requiring the node to transmit all the current data.
