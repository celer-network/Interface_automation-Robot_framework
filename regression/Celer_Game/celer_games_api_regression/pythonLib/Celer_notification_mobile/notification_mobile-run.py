import grpc
import collections

from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_notification_mobile import notification_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_notification_mobile import notification_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key


def notification_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = notification_mobile_pb2_grpc.MobileStub(intercept_channel)
    response = stub.RegisterEndpoint(notification_mobile_pb2.RegisterEndpointRequest(
        device_id='',
        app_id='',
        firebase_push_notification_token='',
        app_version='',
        device_type='',
        push_permission_granted=''
    ))
    print(response.error)

    response1 = stub.GetPopupInAppMessages(notification_mobile_pb2.GetPopupInAppMessagesRequest(
        game_id=1,
        app_id=2,
        app_version='',
        device_type=''

    ))
    print(response1.error, response1.popup_in_app_messages)

    response2 = stub.GetBannerInAppMessages(notification_mobile_pb2.GetBannerInAppMessagesRequest(
        app_id='',
        app_version='',
        device_type=''

    ))
    print(response2.error, response2.banner_in_app_messages)


if __name__ == '__main__':
    notification_API()
