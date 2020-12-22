import account_mobile_pb2
import account_mobile_pb2_grpc
import grpc
import json


def test_run_01(login_email, password):

    with open('server.crt', 'rb') as f:

        certificate_chain = f.read()

    cred = grpc.ssl_channel_credentials(certificate_chain)

    channel = grpc.secure_channel('celerx-test.celer.app', cred)
    # 调用 rpc 服务
    stub = account_mobile_pb2_grpc.MobileStub(channel)
    response = stub.EmailLogin(account_mobile_pb2.EmailLoginRequest(
        # login_email='pknafg52837@chacuo.net',
        # password='yandong001'
        login_email=login_email,
        password=password))
    # print("Greeter client received: " + response.jwt_token)
    # print("password_hash:" + response.password_hash)
    # print("encrypted_phrase_download_url:" + response.encrypted_phrase_download_url)
    # print(json.dumps(response.jwt_token))
    # print(json.dumps(response.password_hash))
    # print(json.dumps(response.encrypted_phrase_download_url))
    if login_email and password:
        if login_email == "pknafg52837@chacuo.net" and password == "yandong001":
            resud = {"statuscode": '200', "message": "登录成功", 'Token': response.jwt_token}
            print(resud)
            return json.dumps(resud, ensure_ascii=False)
        else:
            resud = {'statuscode': "-1", 'message': '账号密码错误'}
            print(resud)
            return json.dumps(resud, ensure_ascii=False)
    else:
        resud = {'code': "10001", 'message': '参数不能为空！'}
        print(resud)
        return json.dumps(resud, ensure_ascii=False)


if __name__ == '__main__':
    test_run_01("pknafg52837@chacuo.net", "yandong01")
