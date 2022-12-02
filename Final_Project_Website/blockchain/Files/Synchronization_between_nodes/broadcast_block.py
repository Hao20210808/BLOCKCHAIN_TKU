def broadcast_block(self, new_block):
    self.broadcast_message_to_nodes("broadcast_block", new_block)

def broadcast_message_to_nodes(self, request, data=None):
    address_concat = self.socket_host + ":" + str(self.socket_port)
    message = {
        "request": request,
        "data": data
    }
    for node_address in self.node_address:
        if node_address != address_concat:
            target_host = node_address.split(":")[0]
            target_port = int(node_address.split(":")[1])
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_host, target_port))
            client.sendall(pickle.dumps(message))
            client.close()
# If a new block is dug by itself, it is necessary to broadcast the new block to other nodes
