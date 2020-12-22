import rsa
with open('public_key.pem', 'r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

message = 'cnblogs'
crypto = rsa.encrypt(message.encode(), pubkey)
print(crypto)
print(len(crypto))
