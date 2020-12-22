import grpc

import collections

from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_storage_mobile import storage_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_storage_mobile import storage_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key


def storage_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = storage_mobile_pb2_grpc.MobileStub(intercept_channel)
    response = stub.RecordInviterInfo(storage_mobile_pb2.RecordInviterInfoRequest(
        inviter_username='proud.asdic',
        invitation_code='2PU3W7',
        inviter_avatar_url='https://celerx.app/invitation/?device=ios&app=network.celer.celerx&inviter=proud.asdic&code=2PU3W7',
        inviter_visible_username='proud.asdic'
    ))
    print(response.error)


if __name__ == '__main__':
    storage_API()
