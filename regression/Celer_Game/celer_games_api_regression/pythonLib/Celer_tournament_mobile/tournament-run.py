import grpc

import collections

from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_tournament_mobile import tournament_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_tournament_mobile import tournament_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key


def tournament_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = tournament_mobile_pb2_grpc.MobileStub(intercept_channel)
    # response = stub.GetMyTournamentTickets(tournament_mobile_pb2.TournamentPaginationRequest(
    #     tournament_id='600',
    #     limit=1,
    #     next_page_token=''
    # ))
    # print(response.error, response.ticket, response.next_page_token)
    #
    # response2 = stub.GetTournamentRankings(tournament_mobile_pb2.TournamentPaginationRequest(
    #     tournament_id='600',
    #     limit=1,
    #     next_page_token=''
    # ))
    # print(response2.error, response2.tournament_bucket, response2.current_player_ranking,
    #       response2.rankings, response2.next_page_token)

    response3 = stub.GetTournamentDetail(tournament_mobile_pb2.TournamentIdRequest(
        tournament_id='600',
    ))
    print(response3.error, response3.bucket, response3.ranking, response3.should_notify,
          response3.exists_prize_to_claim, response3.gem_reward_note, response3.league_star_reward_note)


if __name__ == '__main__':
    tournament_API()
