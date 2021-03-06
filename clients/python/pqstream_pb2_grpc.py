# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pqstream_pb2 as pqstream__pb2


class PQStreamStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Listen = channel.unary_stream(
        '/pqs.PQStream/Listen',
        request_serializer=pqstream__pb2.ListenRequest.SerializeToString,
        response_deserializer=pqstream__pb2.Event.FromString,
        )


class PQStreamServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Listen(self, request, context):
    """Listen responds with a stream of database operations.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PQStreamServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Listen': grpc.unary_stream_rpc_method_handler(
          servicer.Listen,
          request_deserializer=pqstream__pb2.ListenRequest.FromString,
          response_serializer=pqstream__pb2.Event.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pqs.PQStream', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
