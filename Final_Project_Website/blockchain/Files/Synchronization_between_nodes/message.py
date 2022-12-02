elif parsed_message["request"] == "clone_blockchain":
    print(f"[*] Receive blockchain clone request by {address}...")
    message = {
        "request": "upload_blockchain",
        "blockchain_data": self
    }
    connection.sendall(pickle.dumps(message))
    continue

elif parsed_message["request"] == "broadcast_block":
    print(f"[*] Receive block broadcast by {address}...")
    self.receive_broadcast_block(parsed_message["data"])
    continue

elif parsed_message["request"] == "broadcast_transaction":
    print(f"[*] Receive transaction broadcast by {address}...")
    self.pending_transactions.append(parsed_message["data"])
    continue

elif parsed_message["request"] == "add_node":
    print(f"[*] Receive add_node broadcast by {address}...")
    self.node_address.add(parsed_message["data"])
    continue
    
# The part that receives information needs to deal with the information sent by other nodes.

# (1) Received a request to synchronize blocks: 
#   dump a copy of the data on the current blockchain to the other party

# (2) Receive the mined new block: 
#   confirm whether there is a rule that meets the Hash, if so, add it to the chain, and dig the next block

# (3) Received a broadcasted transaction: 
#   put the transaction in pending transactions pending_transactions

# (4) Received a request for a new node: 
#   add the location to the list to be broadcast later
