# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ovm_pb2 as ovm__pb2


class OtazkyVaclavaMoravceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.VaclavMoravec = channel.unary_unary(
                '/ovm.OtazkyVaclavaMoravce/VaclavMoravec',
                request_serializer=ovm__pb2.MoravecRequest.SerializeToString,
                response_deserializer=ovm__pb2.Response.FromString,
                )
        self.VaclavKlaus = channel.unary_unary(
                '/ovm.OtazkyVaclavaMoravce/VaclavKlaus',
                request_serializer=ovm__pb2.KlausRequest.SerializeToString,
                response_deserializer=ovm__pb2.Response.FromString,
                )
        self.MilosZeman = channel.unary_unary(
                '/ovm.OtazkyVaclavaMoravce/MilosZeman',
                request_serializer=ovm__pb2.ZemanRequest.SerializeToString,
                response_deserializer=ovm__pb2.Response.FromString,
                )


class OtazkyVaclavaMoravceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def VaclavMoravec(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VaclavKlaus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MilosZeman(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OtazkyVaclavaMoravceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'VaclavMoravec': grpc.unary_unary_rpc_method_handler(
                    servicer.VaclavMoravec,
                    request_deserializer=ovm__pb2.MoravecRequest.FromString,
                    response_serializer=ovm__pb2.Response.SerializeToString,
            ),
            'VaclavKlaus': grpc.unary_unary_rpc_method_handler(
                    servicer.VaclavKlaus,
                    request_deserializer=ovm__pb2.KlausRequest.FromString,
                    response_serializer=ovm__pb2.Response.SerializeToString,
            ),
            'MilosZeman': grpc.unary_unary_rpc_method_handler(
                    servicer.MilosZeman,
                    request_deserializer=ovm__pb2.ZemanRequest.FromString,
                    response_serializer=ovm__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ovm.OtazkyVaclavaMoravce', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OtazkyVaclavaMoravce(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def VaclavMoravec(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ovm.OtazkyVaclavaMoravce/VaclavMoravec',
            ovm__pb2.MoravecRequest.SerializeToString,
            ovm__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VaclavKlaus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ovm.OtazkyVaclavaMoravce/VaclavKlaus',
            ovm__pb2.KlausRequest.SerializeToString,
            ovm__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MilosZeman(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ovm.OtazkyVaclavaMoravce/MilosZeman',
            ovm__pb2.ZemanRequest.SerializeToString,
            ovm__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
