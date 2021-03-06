# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

# import invitation_mobile_pb2 as invitation__mobile__pb2
from Celer_Game.celer_games_api_regression.pythonLib.Celer_invitation_mobile import invitation_mobile_pb2 as \
    invitation__mobile__pb2


class MobileStub(object):
    """---------------------- interface to be called by app ------------------
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetInvitationCode = channel.unary_unary(
                '/invite.Mobile/GetInvitationCode',
                request_serializer=invitation__mobile__pb2.InvitationCodeRequest.SerializeToString,
                response_deserializer=invitation__mobile__pb2.InvitationCodeResponse.FromString,
                )
        self.QueryInviterBonus = channel.unary_unary(
                '/invite.Mobile/QueryInviterBonus',
                request_serializer=invitation__mobile__pb2.QueryInviterBonusRequest.SerializeToString,
                response_deserializer=invitation__mobile__pb2.QueryInviterBonusResponse.FromString,
                )
        self.QueryInviteeBonus = channel.unary_unary(
                '/invite.Mobile/QueryInviteeBonus',
                request_serializer=invitation__mobile__pb2.QueryInviteeBonusRequest.SerializeToString,
                response_deserializer=invitation__mobile__pb2.QueryInviteeBonusResponse.FromString,
                )
        self.SubmitInvitationCode = channel.unary_unary(
                '/invite.Mobile/SubmitInvitationCode',
                request_serializer=invitation__mobile__pb2.SubmitInvitationCodeRequest.SerializeToString,
                response_deserializer=invitation__mobile__pb2.SubmitInvitationCodeResponse.FromString,
                )


class MobileServicer(object):
    """---------------------- interface to be called by app ------------------
    """

    def GetInvitationCode(self, request, context):
        """Functions to be called by inviters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryInviterBonus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryInviteeBonus(self, request, context):
        """Functions to be called by invitees.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitInvitationCode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MobileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetInvitationCode': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInvitationCode,
                    request_deserializer=invitation__mobile__pb2.InvitationCodeRequest.FromString,
                    response_serializer=invitation__mobile__pb2.InvitationCodeResponse.SerializeToString,
            ),
            'QueryInviterBonus': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryInviterBonus,
                    request_deserializer=invitation__mobile__pb2.QueryInviterBonusRequest.FromString,
                    response_serializer=invitation__mobile__pb2.QueryInviterBonusResponse.SerializeToString,
            ),
            'QueryInviteeBonus': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryInviteeBonus,
                    request_deserializer=invitation__mobile__pb2.QueryInviteeBonusRequest.FromString,
                    response_serializer=invitation__mobile__pb2.QueryInviteeBonusResponse.SerializeToString,
            ),
            'SubmitInvitationCode': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitInvitationCode,
                    request_deserializer=invitation__mobile__pb2.SubmitInvitationCodeRequest.FromString,
                    response_serializer=invitation__mobile__pb2.SubmitInvitationCodeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'invite.Mobile', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mobile(object):
    """---------------------- interface to be called by app ------------------
    """

    @staticmethod
    def GetInvitationCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/invite.Mobile/GetInvitationCode',
            invitation__mobile__pb2.InvitationCodeRequest.SerializeToString,
            invitation__mobile__pb2.InvitationCodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryInviterBonus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/invite.Mobile/QueryInviterBonus',
            invitation__mobile__pb2.QueryInviterBonusRequest.SerializeToString,
            invitation__mobile__pb2.QueryInviterBonusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryInviteeBonus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/invite.Mobile/QueryInviteeBonus',
            invitation__mobile__pb2.QueryInviteeBonusRequest.SerializeToString,
            invitation__mobile__pb2.QueryInviteeBonusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitInvitationCode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/invite.Mobile/SubmitInvitationCode',
            invitation__mobile__pb2.SubmitInvitationCodeRequest.SerializeToString,
            invitation__mobile__pb2.SubmitInvitationCodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
