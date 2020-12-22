import grpc
import json

from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run

from Celer_Game.celer_games_api_regression.pythonLib.Celer_campaign_mobile import campaign_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_campaign_mobile import campaign_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key


def campaign_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    # 调用 rpc 服务
    stub = campaign_mobile_pb2_grpc.MobileStub(intercept_channel)
    response = stub.GetTimeLimitedDepositOptions(campaign_mobile_pb2.GetTimeLimitedDepositOptionsRequest(
        # The parameter can be null
    ))
    print(response.deposit_options)  # Return an empty list

    response2 = stub.GetNotTimeLimitedDepositOptions(campaign_mobile_pb2.GetNonTimeLimitedDepositOptionsRequest(
        # The parameter can be null
    ))
    print(response2.deposit_options)  # Return an empty list

    response3 = stub.GetAllEligibleDepositOptions(campaign_mobile_pb2.GetAllEligibleDepositOptionsRequest(
        # The parameter can be null
    ))
    print(response3.deposit_options)

    response4 = stub.GetDepositCampaignTaskOffer(campaign_mobile_pb2.GetDepositCampaignTaskOfferRequest(
        # The parameter can be null
    ))
    print(response4.err, response4.offer)   # Returns an empty

    response5 = stub.QueryCampaignIsDepositable(campaign_mobile_pb2.QueryCampaignIsDepositableRequest(
        campaign_id='4'
    ))
    print(response5.err, response5.depositable)

    response6 = stub.DismissNotificationForCampaignOffer(campaign_mobile_pb2.DismissNotificationForCampaignOfferRequest(
        campaign_id='3'
    ))
    print(response6.err, response6.campaign_id)

    response7 = stub.MarkCampaignOfferPassed(campaign_mobile_pb2.MarkCampaignOfferPassedRequest(
        campaign_id='5'
    ))
    print(response7.err, response7.campaign_id)


if __name__ == '__main__':
    campaign_API()
