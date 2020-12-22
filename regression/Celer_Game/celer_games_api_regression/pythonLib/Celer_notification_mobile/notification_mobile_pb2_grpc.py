# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
# import notification_mobile_pb2 as notification__mobile__pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_notification_mobile \
    import notification_mobile_pb2 as notification__mobile__pb2


class MobileStub(object):
    """************* below rpc should only be called by mobile *************//
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterEndpoint = channel.unary_unary(
                '/notification.Mobile/RegisterEndpoint',
                request_serializer=notification__mobile__pb2.RegisterEndpointRequest.SerializeToString,
                response_deserializer=notification__mobile__pb2.RegisterEndpointResponse.FromString,
                )
        self.ClickNotification = channel.unary_unary(
                '/notification.Mobile/ClickNotification',
                request_serializer=notification__mobile__pb2.ClickNotificationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetPopupInAppMessages = channel.unary_unary(
                '/notification.Mobile/GetPopupInAppMessages',
                request_serializer=notification__mobile__pb2.GetPopupInAppMessagesRequest.SerializeToString,
                response_deserializer=notification__mobile__pb2.GetPopupInAppMessagesResponse.FromString,
                )
        self.GetBannerInAppMessages = channel.unary_unary(
                '/notification.Mobile/GetBannerInAppMessages',
                request_serializer=notification__mobile__pb2.GetBannerInAppMessagesRequest.SerializeToString,
                response_deserializer=notification__mobile__pb2.GetBannerInAppMessagesResponse.FromString,
                )
        self.MarkInAppMessageAsSeenById = channel.unary_unary(
                '/notification.Mobile/MarkInAppMessageAsSeenById',
                request_serializer=notification__mobile__pb2.MarkInAppMessageAsSeenRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.MarkPushNotificationNotSeen = channel.unary_unary(
                '/notification.Mobile/MarkPushNotificationNotSeen',
                request_serializer=notification__mobile__pb2.MarkPushNotificationNotSeenRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class MobileServicer(object):
    """************* below rpc should only be called by mobile *************//
    """

    def RegisterEndpoint(self, request, context):
        """bind username and FCM token in aws SNS
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClickNotification(self, request, context):
        """should be called when the notification is clicked.
        will add click count and reset rate limit
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPopupInAppMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBannerInAppMessages(self, request, context):
        """request is username
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarkInAppMessageAsSeenById(self, request, context):
        """INPUT: InAppMessage notification_metadata_id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarkPushNotificationNotSeen(self, request, context):
        """backend need to know whether previous push notification is send when user app in front so he don't get to see it.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MobileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterEndpoint': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterEndpoint,
                    request_deserializer=notification__mobile__pb2.RegisterEndpointRequest.FromString,
                    response_serializer=notification__mobile__pb2.RegisterEndpointResponse.SerializeToString,
            ),
            'ClickNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.ClickNotification,
                    request_deserializer=notification__mobile__pb2.ClickNotificationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetPopupInAppMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPopupInAppMessages,
                    request_deserializer=notification__mobile__pb2.GetPopupInAppMessagesRequest.FromString,
                    response_serializer=notification__mobile__pb2.GetPopupInAppMessagesResponse.SerializeToString,
            ),
            'GetBannerInAppMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBannerInAppMessages,
                    request_deserializer=notification__mobile__pb2.GetBannerInAppMessagesRequest.FromString,
                    response_serializer=notification__mobile__pb2.GetBannerInAppMessagesResponse.SerializeToString,
            ),
            'MarkInAppMessageAsSeenById': grpc.unary_unary_rpc_method_handler(
                    servicer.MarkInAppMessageAsSeenById,
                    request_deserializer=notification__mobile__pb2.MarkInAppMessageAsSeenRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'MarkPushNotificationNotSeen': grpc.unary_unary_rpc_method_handler(
                    servicer.MarkPushNotificationNotSeen,
                    request_deserializer=notification__mobile__pb2.MarkPushNotificationNotSeenRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'notification.Mobile', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mobile(object):
    """************* below rpc should only be called by mobile *************//
    """

    @staticmethod
    def RegisterEndpoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notification.Mobile/RegisterEndpoint',
            notification__mobile__pb2.RegisterEndpointRequest.SerializeToString,
            notification__mobile__pb2.RegisterEndpointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClickNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notification.Mobile/ClickNotification',
            notification__mobile__pb2.ClickNotificationRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPopupInAppMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notification.Mobile/GetPopupInAppMessages',
            notification__mobile__pb2.GetPopupInAppMessagesRequest.SerializeToString,
            notification__mobile__pb2.GetPopupInAppMessagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBannerInAppMessages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notification.Mobile/GetBannerInAppMessages',
            notification__mobile__pb2.GetBannerInAppMessagesRequest.SerializeToString,
            notification__mobile__pb2.GetBannerInAppMessagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarkInAppMessageAsSeenById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notification.Mobile/MarkInAppMessageAsSeenById',
            notification__mobile__pb2.MarkInAppMessageAsSeenRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarkPushNotificationNotSeen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notification.Mobile/MarkPushNotificationNotSeen',
            notification__mobile__pb2.MarkPushNotificationNotSeenRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
