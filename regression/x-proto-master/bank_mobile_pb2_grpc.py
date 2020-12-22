# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bank_mobile_pb2 as bank__mobile__pb2


class MobileStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBalances = channel.unary_unary(
                '/bank.Mobile/GetBalances',
                request_serializer=bank__mobile__pb2.GetBalancesRequest.SerializeToString,
                response_deserializer=bank__mobile__pb2.GetBalancesResponse.FromString,
                )
        self.GetRecentTxs = channel.unary_unary(
                '/bank.Mobile/GetRecentTxs',
                request_serializer=bank__mobile__pb2.GetRecentTxsRequest.SerializeToString,
                response_deserializer=bank__mobile__pb2.GetRecentTxsResponse.FromString,
                )
        self.GetRefidTxs = channel.unary_unary(
                '/bank.Mobile/GetRefidTxs',
                request_serializer=bank__mobile__pb2.GetRefidTxsRequest.SerializeToString,
                response_deserializer=bank__mobile__pb2.GetRefidTxsResponse.FromString,
                )


class MobileServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBalances(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecentTxs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRefidTxs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MobileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBalances': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBalances,
                    request_deserializer=bank__mobile__pb2.GetBalancesRequest.FromString,
                    response_serializer=bank__mobile__pb2.GetBalancesResponse.SerializeToString,
            ),
            'GetRecentTxs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecentTxs,
                    request_deserializer=bank__mobile__pb2.GetRecentTxsRequest.FromString,
                    response_serializer=bank__mobile__pb2.GetRecentTxsResponse.SerializeToString,
            ),
            'GetRefidTxs': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRefidTxs,
                    request_deserializer=bank__mobile__pb2.GetRefidTxsRequest.FromString,
                    response_serializer=bank__mobile__pb2.GetRefidTxsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bank.Mobile', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mobile(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBalances(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bank.Mobile/GetBalances',
            bank__mobile__pb2.GetBalancesRequest.SerializeToString,
            bank__mobile__pb2.GetBalancesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecentTxs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bank.Mobile/GetRecentTxs',
            bank__mobile__pb2.GetRecentTxsRequest.SerializeToString,
            bank__mobile__pb2.GetRecentTxsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRefidTxs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bank.Mobile/GetRefidTxs',
            bank__mobile__pb2.GetRefidTxsRequest.SerializeToString,
            bank__mobile__pb2.GetRefidTxsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
