def start(self):
    address, private = self.generate_address()
    print(f"Miner address: {address}")
    print(f"Miner private: {private}")
    self.create_genesis_block()
    while(True):
        self.mine_block(address)
        self.adjust_difficulty()
