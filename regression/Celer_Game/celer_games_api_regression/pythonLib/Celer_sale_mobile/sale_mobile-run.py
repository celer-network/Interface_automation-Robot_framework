import grpc
import collections

from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_sale_mobile import sale_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_sale_mobile import sale_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key


def sale_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = sale_mobile_pb2_grpc.MobileStub(intercept_channel)
    response = stub.GetMyCoupons(sale_mobile_pb2.GetMyCouponsRequest(
        limit=2,
        next_page_token=bytes(123)
    ))
    print(response.error, response.orders, response.next_page_token)

    response1 = stub.GetMyUsableCouponsByBucketId(sale_mobile_pb2.GetMyUsableCouponsByBucketIdRequest(
        bucket_id=''
    ))
    print(response1.error, response1.orders)

    response2 = stub.GetSaleEvent(sale_mobile_pb2.GetSaleEventRequest(
    ))
    print(response2.error, response2.sale_event)

    response3 = stub.GetSaleBundle(sale_mobile_pb2.GetSaleBundleRequest(
        bundle_id=1
    ))
    print(response3.error, response3.bundle)


if __name__ == '__main__':
    sale_API()
