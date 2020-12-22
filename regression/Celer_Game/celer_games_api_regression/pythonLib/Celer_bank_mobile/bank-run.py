# import Celer_Game.celer_games_api_regression.pythonLib.Celer_bank_mobile.bank_mobile_pb2
# import bank_mobile_pb2_grpc
import grpc
import json

from Celer_Game.celer_games_api_regression.pythonLib.Celer_bank_mobile import bank_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_bank_mobile import bank_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.common import token_extract


def bank_API():
    with open('server.crt', 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', creds)
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = bank_mobile_pb2_grpc.MobileStub(intercept_channel)
    response = stub.GetBalances(bank_mobile_pb2.GetBalancesRequest(
        jwt_token=account_mobile_run.test_run()
    ))
    print(response.error)


# def test02_run():
#     with open('server.crt', 'rb') as f:
#         certificate_chain = f.read()
#     cred = grpc.ssl_channel_credentials(certificate_chain)
#     token = account_mobile_run.test_run()
#     name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
#     channel = grpc.secure_channel('celerx-test.celer.app', cred)
#     intercept_channel = grpc.intercept_channel(channel, name)
#     # 调用 rpc 服务
#     stub = bank_mobile_pb2_grpc.MobileStub(intercept_channel)
#     response = stub.GetBalances(bank_mobile_pb2.GetBalancesRequest(
#         jwt_token=account_mobile_run.test_run()
#     ))
#     print(response.error)
    # print("Greeter client received: " + response.jwt_token)
    # print("password_hash:" + response.password_hash)
    # print("encrypted_phrase_download_url:" + response.encrypted_phrase_download_url)
    # print(json.dumps(response.error))

    # print(json.dumps(response.password_hash))
    # print(json.dumps(response.encrypted_phrase_download_url))


if __name__ == '__main__':
    bank_API()
