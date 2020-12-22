import multiprocessing

import account_mobile_pb2
import account_mobile_pb2_grpc
import grpc
import rsa
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend


def run():
    with open('server.crt', 'rb') as f:
        certificate_chain = f.read()
    cred = grpc.ssl_channel_credentials(certificate_chain)
    channel = grpc.secure_channel('celerx-test.celer.app', cred)
    # 调用 rpc 服务
    stub = account_mobile_pb2_grpc.MobileStub(channel)
    response = stub.EmailLogin(account_mobile_pb2.EmailLoginRequest(login_email='pknafg52837@chacuo.net', password='yandong001'))
    print("Greeter client received: " + response.jwt_token)
    print("password_hash:" + response.password_hash)
    print("encrypted_phrase_download_url:" + response.encrypted_phrase_download_url)


# cred = grpc.ssl_channel_credentials(root_certificates=root)
#
#
# def send():
#     channel = grpc.secure_channel('celerx-test.celer.app', cred)
#
#     # 调用 rpc 服务
#     stub = account_mobile_pb2_grpc.MobileStub(channel)
#     response = stub.EmailLogin(account_mobile_pb2.EmailLoginRequest(login_email='afgzni37052@chacuo.net'))
#     print("Greeter client received: " + response.jwt_token)
#
#
# def main():
#     # 使用 with 语句
#     with grpc.secure_channel('celerx-test.celer.app', cred) as channel:
#         stub = account_mobile_pb2_grpc.MobileStub(channel)
#         response_2 = stub.EmailLogin(account_mobile_pb2.EmailLoginRequest(password='abc123456'))
#         print("Greeter client received: " + response_2.jwt_token)
#         channel.close()

# p = multiprocessing.Process(target=send)
# p.start()
# p.join()


if __name__ == '__main__':
    run()
