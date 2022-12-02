def handle_receive():
    while True:
        response = client.recv(4096)
        if response:
            print(f"[*] Message from node: {response}")

if __name__ == "__main__":
    target_host = "127.0.0.1"
    target_port = int(sys.argv[1])
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))

    receive_handler = threading.Thread(target=handle_receive, args=())
    receive_handler.start()
