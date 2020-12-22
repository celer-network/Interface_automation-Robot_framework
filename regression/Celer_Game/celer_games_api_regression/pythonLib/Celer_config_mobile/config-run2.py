import grpc
import collections
from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_config_mobile import config_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_config_mobile import config_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key


def config_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = config_mobile_pb2_grpc.MobileStub(intercept_channel)
    response = stub.SetMarketingCampaignTag(config_mobile_pb2.SetMarketingCampaignTagRequest(
        marketing_campaign_tag=''
    ))
    print(response.error)

    response2 = stub.SetABTestingExperimentTag(config_mobile_pb2.SetABTestingExperimentTagRequest(
        experiment_tag_name='',
        experiment_user_tag=''
    ))
    print(response2.error)

    response3 = stub.GetGameInfoByGameID(config_mobile_pb2.GetGameInfoByGameIDRequest(
        game_id='000403'
    ))
    print(response3.error, response3.game_info)

    response4 = stub.GetPracticeBucket(config_mobile_pb2.GetPracticeBucketRequest(
        game_id='000403'
    ))
    print(response4.practice_bucket)

    response5 = stub.IsBlockedByDevice(config_mobile_pb2.IsBlockedByDeviceRequest(
        device_type='',
        device_id=''
    ))
    print(response5.error, response5.is_blocked)

    response6 = stub.GetTournamentBuckets(config_mobile_pb2.GetTournamentBucketsRequest(
        game_id='',  # if this is not specified, return all tournaments for this app
        primary_account_type='',
        tournament_status='',
        # // could be
        # // "celerx.app" for Android or  "network.celer.celerx" for iOS
        # // "celerx.app.solitaire"
        # // "celerx.app.fruitpunch"
        # // "celerx.app.cubematrix"
        # // "celerx.app.daubcash"
        app_id='',
        app_version='',
        device_type=''
    ))
    print(response6.error, response6.tournament_bucket_detail_list)

    response7 = stub.GetGameBucketList(config_mobile_pb2.GetGameBucketListRequest(
        game_id='',
        primary_account_type='',
        tournament_status='',
        # // could be
        # // "celerx.app" for Android or  "network.celer.celerx" for iOS
        # // "celerx.app.solitaire"
        # // "celerx.app.fruitpunch"
        # // "celerx.app.cubematrix"
        # // "celerx.app.daubcash"
        app_id='',
        app_version='',
        device_type='',
        need_special_bucket=''
    ))
    print(response7.error, response7.match_buckets, response7.tournament_buckets, response7.special_buckets)

    response8 = stub.GetHomeNotifications(config_mobile_pb2.HomeNotificationRequest(
        primary_account_type=''
    ))
    print(response8.error, response8.exists_unread_history, response8.exists_unclaimed_prize)

    response9 = stub.GetGameActivePlayersCount(config_mobile_pb2.GetGameActivePlayersCountRequest(
        game_ids=''
    ))
    print(response9.active_players)


if __name__ == '__main__':
    config_API()
