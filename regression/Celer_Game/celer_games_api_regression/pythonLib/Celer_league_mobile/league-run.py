import grpc
import collections
from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_league_mobile import league_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_league_mobile import league_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key


def league_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = league_mobile_pb2_grpc.MobileStub(intercept_channel)
    # enum = league_mobile_pb2.LeagueStatusEnum.Value(
    #     'ENDED'
    # )
    # # print(enum)

    response = stub.GetMyLeagueRanking(league_mobile_pb2.LeagueIdStringRequest(
        league_id='1'
    ))
    print(response.error, response.ranking)

    # enum1 = league_mobile_pb2.LeagueTypeEnum.Value(
    #     'CASH_LEAGUE'
    # )
    response2 = stub.GetActiveLeague(league_mobile_pb2.LeagueTypeRequest(
        league_type=league_mobile_pb2.UNKNOWN_LEAGUE_TYPE
    ))
    print(response2.error, response2.league_bucket)

    response3 = stub.GetMyActiveLeagueRanking(league_mobile_pb2.LeagueTypeRequest(
        league_type=league_mobile_pb2.CASH_LEAGUE
    ))
    print(response3.error, response3.ranking)

    response4 = stub.GetActiveLeagueRankings(league_mobile_pb2.GetActiveLeagueRankingsRequest(
        limit=1,
        next_page_token=None,
        league_type=league_mobile_pb2.CASH_LEAGUE
    ))
    print(response4.error, response4.league_bucket)

    response5 = stub.GetLeagueRankings(league_mobile_pb2.GetLeagueRankingsRequest(
        limit=1,
        next_page_token=None,
        league_id='2'
    ))
    print(response5.error, response5.league_bucket)


if __name__ == '__main__':
    league_API()
