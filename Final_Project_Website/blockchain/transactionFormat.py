# according to the DBset:
# Transaction{ sender, receiver, images, amounts, fee, content }

class Transaction:
    def __init__(self,sender,receiver,amounts,fee,message):
        self.sender = sender
        self.receiver = receiver
        self.images = images
        self.amounts = amounts
        self.fee = fee
        self.content = content
