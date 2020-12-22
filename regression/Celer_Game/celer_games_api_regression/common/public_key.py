import grpc
def public_key():
    with open('server.crt', 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
    return creds
