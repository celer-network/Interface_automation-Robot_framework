import grpc
import collections
from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_invitation_mobile import invitation_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_invitation_mobile import invitation_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key


def invitation_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = invitation_mobile_pb2_grpc.MobileStub(intercept_channel)
    response = stub.SubmitInvitationCode(invitation_mobile_pb2.SubmitInvitationCodeRequest(
        jwt_token=account_mobile_run.test_run(),
        invitation_code='2PU3W7'
    ))
    print(response.error)

    response2 = stub.QueryInviteeBonus(invitation_mobile_pb2.QueryInviteeBonusRequest(
        invitee_username='proud.asdic'
    ))
    print(response2.bonus_amount, response2.currency, response2.invitee_username,
          response2.status, response2.error, response2.inviter_snip)

    response3 = stub.GetInvitationCode(invitation_mobile_pb2.InvitationCodeRequest(
        jwt_token=account_mobile_run.test_run()
    ))
    print(response3.invitation_code, response3.error)

    response4 = stub.QueryInviterBonus(invitation_mobile_pb2.QueryInviterBonusRequest(
        inviter_username='proud.asdic'
    ))
    print(response4.reward_cash_per_first_deposit, response4.currency, response4.error)


if __name__ == '__main__':
    invitation_API()
