import grpc
import collections
from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_history_mobile import history_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_history_mobile import history_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key

proto_reg = history_mobile_pb2.GetGameHistoryRequest()
proto_GameHistoryPageParam = history_mobile_pb2.GameHistoryPageParam()
# proto_reg.page_request_list = [2]
mini = proto_reg.page_request_list.extend([proto_GameHistoryPageParam])
# name1 = proto_reg.page_request_list
name2 = proto_reg.primary_account_type
print(mini)
print(name2)


def history_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = history_mobile_pb2_grpc.MobileStub(intercept_channel)
    response = stub.c(history_mobile_pb2.GetGameHistoryRequest(
        page_request_list=mini,
        primary_account_type=2,
        needs_all_prize_claims=None,
        needs_top_acceptable_challenges=None,
        game_id='000403'
    ))

    print(response.error, response.page_list, response.total_claim_prize, response.top_acceptable_challenges)


if __name__ == '__main__':
    history_API()
