def receive_socket_message(self, connection, address):
    with connection:
        print(f'Connected by: {address}')
        while True:
            message = connection.recv(1024)
            print(f"[*] Received: {message}")
            try:
                parsed_message = pickle.loads(message)
            except Exception:
                print(f"{message} cannot be parsed")
            if message:
                if parsed_message["request"] == "get_balance":
                    print("Start to get the balance for client...")
                    address = parsed_message["address"]
                    balance = self.get_balance(address)
                    response = {
                        "address": address,
                        "balance": balance
                    }
                elif parsed_message["request"] == "transaction":
                    print("Start to transaction for client...")
                    new_transaction = parsed_message["data"]
                    result, result_message = self.add_transaction(
                        new_transaction,
                        parsed_message["signature"]
                    )
                    response = {
                        "result": result,
                        "result_message": result_message
                    }
                else:
                    response = {
                        "message": "Unknown command."
                    }
                response_bytes = str(response).encode('utf8')
                connection.sendall(response_bytes)
                
# Based on the information passed by the user, determine what the user wants to do

# (1) get account balance
# (2) Initiate a transaction

# Then receive different parameters according to what the user wants to do, and return the result to the user.
