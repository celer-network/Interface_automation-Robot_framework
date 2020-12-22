import grpc
import collections

from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_match_ticket_mobile import match_ticket_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_match_ticket_mobile import match_ticket_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key


def match_ticket_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = match_ticket_mobile_pb2_grpc.MobileStub(intercept_channel)
    response = stub.GetMatchDetailByTicketId(match_ticket_mobile_pb2.GetMatchDetailByTicketIdRequest(
        ticket_id='',
        app_version='',
        device_type=''
    ))
    print(response.error, response.match_detail_info)

    response1 = stub. RefundWhenGameCrashed(match_ticket_mobile_pb2. RefundWhenGameCrashedRequest(
        ticket_id='',
        token='',
        submit_time=''
    ))
    print(response1.error, response1. refund_result)


if __name__ == '__main__':
    match_ticket_API()
