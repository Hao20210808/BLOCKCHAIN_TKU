import rsa

def generate_address(self):
    public, private = rsa.newkeys(512)
    public_key = public.save_pkcs1()
    private_key = private.save_pkcs1()
    return self.get_address_from_public(public_key), private_key

# Use RSA encryption method to randomly generate a pair of public and private keys, 
# and transfer them to pkcs1 form
