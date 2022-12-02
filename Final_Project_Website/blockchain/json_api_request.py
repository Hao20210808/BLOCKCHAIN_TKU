import request
import json

src = ''
r = request.get(url)
data = json.load(json_file)
for block in data:
  name = block['name']
  email = block['email']
  balance = block['balance']
    
  person_block = {
    'name':name,
    'email':email,
    'balance':balance
  }    
  
