def start_socket_server(self):
    t = threading.Thread(target=self.wait_for_socket_connection)
    t.start()

def wait_for_socket_connection(self):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((self.socket_host, self.socket_port))
        s.listen()
        while True:
            conn, address = s.accept()

            client_handler = threading.Thread(
                target=self.receive_socket_message,
                args=(conn, address)
            )
            client_handler.start()
            
# Receive external information while packaging transactions and mining
# (1) Open a thread to wait for the new external connection s.accept() after bind, 
# (2) Open a thread for each independent connection to receive and process information after each new connection is established.
