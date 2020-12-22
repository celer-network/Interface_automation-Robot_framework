import grpc
import collections

from Celer_Game.celer_games_api_regression.pythonLib.Celer_account_mobile import account_mobile_run
from Celer_Game.celer_games_api_regression.pythonLib.Celer_loyalty_mobile import loyalty_mobile_pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_loyalty_mobile import loyalty_mobile_pb2_grpc
from Celer_Game.celer_games_api_regression.common import token_extract
from Celer_Game.celer_games_api_regression.common import public_key

addr = '1'


def loyalty_API():
    token = account_mobile_run.test_run()
    name = token_extract.header_adder_interceptor('authorization', '{}'.format(token))
    channel = grpc.secure_channel('celerx-test.celer.app', public_key.public_key())
    intercept_channel = grpc.intercept_channel(channel, name)
    stub = loyalty_mobile_pb2_grpc.MobileStub(intercept_channel)
    response = stub.GetFirstGame(loyalty_mobile_pb2.GetFirstGameRequest(
        user_addr=addr,
        # auth=''
    ))
    print(response.error, response.got_reward, response.gain)

    response2 = stub.GetCheckin(loyalty_mobile_pb2.GetCheckinRequest(
        user_addr=addr,
        # auth=''
    ))
    print(response2.error, response2.has_checkin, response2.has_makeup,
          response2.start, response2.today, response2.now, response2.today_end, response2.days)

    response3 = stub.SubmitCheckin(loyalty_mobile_pb2.SubmitCheckinRequest(
        user_addr=addr,
        # auth=''
    ))
    print(response3.error, response3.got_reward, response3.reward)

    response4 = stub.ResetCheckin(loyalty_mobile_pb2.ResetCheckinRequest(
        user_addr=addr,
        # auth=''
    ))
    print(response4.error)

    response5 = stub.GetTasks(loyalty_mobile_pb2.GetTasksRequest(
        user_addr=addr,
        # auth=''
    ))
    print(response5.error, response5.tasks)

    response6 = stub.AcceptTask(loyalty_mobile_pb2.AcceptTaskRequest(
        user_addr=addr,
        # auth=''
        task_id=1
    ))
    print(response6.error, response6.started, response6.start, response6.deadline, response6.now)

    response7 = stub.AcceptAllTasks(loyalty_mobile_pb2.AcceptAllTasksRequest(
        user_addr=addr,
        # auth=''
    ))
    print(response7.error)

    response8 = stub.ClaimTask(loyalty_mobile_pb2.ClaimTaskRequest(
        user_addr=addr,
        # auth=''
        task_id=3

    ))
    print(response8.error, response8.got_reward, response8.gain, response8.reward)

    response9 = stub.GetRedeemTable(loyalty_mobile_pb2.GetRedeemTableRequest(
        user_addr=addr,
        # auth=''
    ))
    print(response9.error, response9.expiring_amount, response9.expiration, response9.entries)

    response10 = stub.Redeem(loyalty_mobile_pb2.RedeemRequest(
        user_addr=addr,
        # auth='',
        redeem_id=1,
        user_email='',    # only needed if "id" is for physical reward
        proof=bytes(),         # redeem proof passed to bank (addr/amount/symbol/ts)
        proofts=1        # UTC timestamp (in seconds) used by the proof
    ))
    print(response10.error, response10.got_reward)

    response11 = stub.GetTier(loyalty_mobile_pb2.GetTierRequest(
        user_addr=addr,
        # auth='',
    ))
    print(response11.error, response11.tier, response11.icon, response11.multiplier, response11.year)

    response12 = stub.GetTiers(loyalty_mobile_pb2.GetTiersRequest(

    ))
    print(response12.error, response12.entries)

    response13 = stub.ClaimFreeLootBox(loyalty_mobile_pb2.ClaimFreeLootBoxRequest(
        user_addr=addr,
        # auth='',

    ))
    print(response13.error, response13.options, response13.countdown_timer_duration)

    response14 = stub.GetDailyRewardsPreview(loyalty_mobile_pb2.GetDailyRewardsPreviewRequest(
        user_addr=addr,
        # auth='',
    ))
    print(response14.error, response14.daily_check_in_preview, response14.daily_tasks_preview,
          response14.free_loot_box_preview)


if __name__ == '__main__':
    loyalty_API()
