# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Anim.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Anim.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nAnim.proto\"\x18\n\x04\x41nim\x12\x10\n\x08\x61nimName\x18\x01 \x01(\tb\x06proto3')
)




_ANIM = _descriptor.Descriptor(
  name='Anim',
  full_name='Anim',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='animName', full_name='Anim.animName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=38,
)

DESCRIPTOR.message_types_by_name['Anim'] = _ANIM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Anim = _reflection.GeneratedProtocolMessageType('Anim', (_message.Message,), dict(
  DESCRIPTOR = _ANIM,
  __module__ = 'Anim_pb2'
  # @@protoc_insertion_point(class_scope:Anim)
  ))
_sym_db.RegisterMessage(Anim)


# @@protoc_insertion_point(module_scope)
