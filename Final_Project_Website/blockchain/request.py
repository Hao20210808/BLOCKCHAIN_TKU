import request
import json

src = ''
r = request.get(url)
data = json.load(json_file)
for transaction in data:
  sender = transaction['sender_id']
  receiver = transaction['receiver_id']
  amounts = transaction['amounts']
  fee = transaction['fee']
  message = transaction['message']
    
  transaction_list = {
    'sender':sender,
    'receiver':receiver,
    'amounts':amounts,
    'fee':fee,
    'message':message
  }    
if 404:
  return 'Request Failed!'
  
if __name__ == '__main__':
    block = BlockChain()
    block.start()
