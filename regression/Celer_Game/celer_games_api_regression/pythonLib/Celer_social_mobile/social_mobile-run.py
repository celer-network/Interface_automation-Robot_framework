import grpc

import collections

from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_social_mobile import social_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_social_mobile import social_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key


def social_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = social_mobile_pb2_grpc.MobileStub(intercept_channel)
    serverStub = social_mobile_pb2_grpc.SocialChallengeAPIsStub(intercept_channel)
    response = stub.GetUserFullProfile(social_mobile_pb2.GetUserFullProfileRequest(
        username='proud.asdic',
        primary_account_type='',
        app_id='',
        device_type=''
    ))
    print(response.error, response.user_social_profile, response.league_preview,
          response.game_records, response.match_flow_items)

    response1 = stub.GetUserSocialProfile(social_mobile_pb2.GetUserSocialProfileRequest(
        username='',
        primary_account_type=''
    ))
    print(response1.error, response1.user_social_profile)

    response2 = serverStub.CreateSocialChallengeRelation(social_mobile_pb2.CreateChallengeRelationRequest(
        opponent_username='',
        app_id='',
        match_bucket_id='',
        challenge_message='',
        challenge_message_id=''
    ))
    print(response2.error, response2.room_id)

    response2 = serverStub.GetSocialChallengeNotification(social_mobile_pb2.GetSocialChallengeNotificationRequest(
        app_id=None
    ))
    print(response2.error, response2.should_notify_social_challenge)

    response3 = stub.GetLiveFeedByAppId(social_mobile_pb2.GetLiveFeedByAppIdRequest(
        max_count=1,
        app_id='',
        device_type='',
        game_id=''
    ))
    print(response3.error, response3.live_feeds)

    response4 = stub.GetMegaWinsFeedItems(social_mobile_pb2.GetMegaWinsFeedItemsRequest(
        max_count=1,
        app_id='',
        device_type='',
        game_id=''
    ))
    print(response4.error, response4.feed)


if __name__ == '__main__':
    social_API()
