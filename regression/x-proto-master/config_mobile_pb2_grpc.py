# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import config_mobile_pb2 as config__mobile__pb2


class MobileStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IsBlockedByDevice = channel.unary_unary(
                '/config.Mobile/IsBlockedByDevice',
                request_serializer=config__mobile__pb2.IsBlockedByDeviceRequest.SerializeToString,
                response_deserializer=config__mobile__pb2.IsBlockedByDeviceResponse.FromString,
                )
        self.GetTournamentBuckets = channel.unary_unary(
                '/config.Mobile/GetTournamentBuckets',
                request_serializer=config__mobile__pb2.GetTournamentBucketsRequest.SerializeToString,
                response_deserializer=config__mobile__pb2.GetTournamentBucketsResponse.FromString,
                )
        self.GetGameBucketList = channel.unary_unary(
                '/config.Mobile/GetGameBucketList',
                request_serializer=config__mobile__pb2.GetGameBucketListRequest.SerializeToString,
                response_deserializer=config__mobile__pb2.GetGameBucketListResponse.FromString,
                )
        self.GetHomeNotifications = channel.unary_unary(
                '/config.Mobile/GetHomeNotifications',
                request_serializer=config__mobile__pb2.HomeNotificationRequest.SerializeToString,
                response_deserializer=config__mobile__pb2.HomeNotificationResponse.FromString,
                )
        self.GetPracticeBucket = channel.unary_unary(
                '/config.Mobile/GetPracticeBucket',
                request_serializer=config__mobile__pb2.GetPracticeBucketRequest.SerializeToString,
                response_deserializer=config__mobile__pb2.GetPracticeBucketResponse.FromString,
                )
        self.GetGameInfoByGameID = channel.unary_unary(
                '/config.Mobile/GetGameInfoByGameID',
                request_serializer=config__mobile__pb2.GetGameInfoByGameIDRequest.SerializeToString,
                response_deserializer=config__mobile__pb2.GetGameInfoByGameIDResponse.FromString,
                )
        self.SetMarketingCampaignTag = channel.unary_unary(
                '/config.Mobile/SetMarketingCampaignTag',
                request_serializer=config__mobile__pb2.SetMarketingCampaignTagRequest.SerializeToString,
                response_deserializer=config__mobile__pb2.SetMarketingCampaignTagResponse.FromString,
                )
        self.GetGameActivePlayersCount = channel.unary_unary(
                '/config.Mobile/GetGameActivePlayersCount',
                request_serializer=config__mobile__pb2.GetGameActivePlayersCountRequest.SerializeToString,
                response_deserializer=config__mobile__pb2.GetGameActivePlayersCountResponse.FromString,
                )
        self.SetABTestingExperimentTag = channel.unary_unary(
                '/config.Mobile/SetABTestingExperimentTag',
                request_serializer=config__mobile__pb2.SetABTestingExperimentTagRequest.SerializeToString,
                response_deserializer=config__mobile__pb2.SetABTestingExperimentTagResponse.FromString,
                )


class MobileServicer(object):
    """Missing associated documentation comment in .proto file."""

    def IsBlockedByDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTournamentBuckets(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGameBucketList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHomeNotifications(self, request, context):
        """For mobile home page notifications, Avoid mobile calculate these fields from different APIs,
        return HomeNotificationResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPracticeBucket(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGameInfoByGameID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMarketingCampaignTag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGameActivePlayersCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetABTestingExperimentTag(self, request, context):
        """tag user based on abtesting group
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MobileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IsBlockedByDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.IsBlockedByDevice,
                    request_deserializer=config__mobile__pb2.IsBlockedByDeviceRequest.FromString,
                    response_serializer=config__mobile__pb2.IsBlockedByDeviceResponse.SerializeToString,
            ),
            'GetTournamentBuckets': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTournamentBuckets,
                    request_deserializer=config__mobile__pb2.GetTournamentBucketsRequest.FromString,
                    response_serializer=config__mobile__pb2.GetTournamentBucketsResponse.SerializeToString,
            ),
            'GetGameBucketList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGameBucketList,
                    request_deserializer=config__mobile__pb2.GetGameBucketListRequest.FromString,
                    response_serializer=config__mobile__pb2.GetGameBucketListResponse.SerializeToString,
            ),
            'GetHomeNotifications': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHomeNotifications,
                    request_deserializer=config__mobile__pb2.HomeNotificationRequest.FromString,
                    response_serializer=config__mobile__pb2.HomeNotificationResponse.SerializeToString,
            ),
            'GetPracticeBucket': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPracticeBucket,
                    request_deserializer=config__mobile__pb2.GetPracticeBucketRequest.FromString,
                    response_serializer=config__mobile__pb2.GetPracticeBucketResponse.SerializeToString,
            ),
            'GetGameInfoByGameID': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGameInfoByGameID,
                    request_deserializer=config__mobile__pb2.GetGameInfoByGameIDRequest.FromString,
                    response_serializer=config__mobile__pb2.GetGameInfoByGameIDResponse.SerializeToString,
            ),
            'SetMarketingCampaignTag': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMarketingCampaignTag,
                    request_deserializer=config__mobile__pb2.SetMarketingCampaignTagRequest.FromString,
                    response_serializer=config__mobile__pb2.SetMarketingCampaignTagResponse.SerializeToString,
            ),
            'GetGameActivePlayersCount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGameActivePlayersCount,
                    request_deserializer=config__mobile__pb2.GetGameActivePlayersCountRequest.FromString,
                    response_serializer=config__mobile__pb2.GetGameActivePlayersCountResponse.SerializeToString,
            ),
            'SetABTestingExperimentTag': grpc.unary_unary_rpc_method_handler(
                    servicer.SetABTestingExperimentTag,
                    request_deserializer=config__mobile__pb2.SetABTestingExperimentTagRequest.FromString,
                    response_serializer=config__mobile__pb2.SetABTestingExperimentTagResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'config.Mobile', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mobile(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def IsBlockedByDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Mobile/IsBlockedByDevice',
            config__mobile__pb2.IsBlockedByDeviceRequest.SerializeToString,
            config__mobile__pb2.IsBlockedByDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTournamentBuckets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Mobile/GetTournamentBuckets',
            config__mobile__pb2.GetTournamentBucketsRequest.SerializeToString,
            config__mobile__pb2.GetTournamentBucketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGameBucketList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Mobile/GetGameBucketList',
            config__mobile__pb2.GetGameBucketListRequest.SerializeToString,
            config__mobile__pb2.GetGameBucketListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHomeNotifications(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Mobile/GetHomeNotifications',
            config__mobile__pb2.HomeNotificationRequest.SerializeToString,
            config__mobile__pb2.HomeNotificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPracticeBucket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Mobile/GetPracticeBucket',
            config__mobile__pb2.GetPracticeBucketRequest.SerializeToString,
            config__mobile__pb2.GetPracticeBucketResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGameInfoByGameID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Mobile/GetGameInfoByGameID',
            config__mobile__pb2.GetGameInfoByGameIDRequest.SerializeToString,
            config__mobile__pb2.GetGameInfoByGameIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetMarketingCampaignTag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Mobile/SetMarketingCampaignTag',
            config__mobile__pb2.SetMarketingCampaignTagRequest.SerializeToString,
            config__mobile__pb2.SetMarketingCampaignTagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetGameActivePlayersCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Mobile/GetGameActivePlayersCount',
            config__mobile__pb2.GetGameActivePlayersCountRequest.SerializeToString,
            config__mobile__pb2.GetGameActivePlayersCountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetABTestingExperimentTag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config.Mobile/SetABTestingExperimentTag',
            config__mobile__pb2.SetABTestingExperimentTagRequest.SerializeToString,
            config__mobile__pb2.SetABTestingExperimentTagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)