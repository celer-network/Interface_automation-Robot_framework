from concurrent import futures
import time
import grpc
import account_mobile_pb2
import account_mobile_pb2_grpc


# 实现 proto 文件中定义的 mobileServicer

class Mobile(account_mobile_pb2_grpc.MobileServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def EmailLogin(self, request, context):
        return account_mobile_pb2.EmailLoginResponse(jwt_token='h{msg}'.format(msg=request.login_email))
        # return account_mobile_pb2.EmailLoginResponse(='h{msg}'.format(msg=request.password))


def server():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    account_mobile_pb2_grpc.add_MobileServicer_to_server(Mobile(), server)
    with open('server.crt', 'rb') as f:
        private_key = f.read()
    with open('public_key.pem', 'rb') as f:
        certificate_chain = f.read()
    server_credentials = grpc.ssl_server_credentials([(private_key, certificate_chain)])
    server.add_secure_port('celerx-test.celer.app:443', server_credentials)
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # one day in seconds
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    server()
