# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SimpleTest.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SimpleTest.proto',
  package='com.gamehero.sxd2.pro',
  serialized_pb='\n\x10SimpleTest.proto\x12\x15\x63om.gamehero.sxd2.pro\"[\n\x06Simple\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\r\x12\r\n\x05phone\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\x12\n\n\x02ps\x18\x06 \x01(\t\";\n\nSimpleTest\x12-\n\x06simple\x18\x01 \x03(\x0b\x32\x1d.com.gamehero.sxd2.pro.Simple')




_SIMPLE = _descriptor.Descriptor(
  name='Simple',
  full_name='com.gamehero.sxd2.pro.Simple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.gamehero.sxd2.pro.Simple.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='com.gamehero.sxd2.pro.Simple.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='age', full_name='com.gamehero.sxd2.pro.Simple.age', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phone', full_name='com.gamehero.sxd2.pro.Simple.phone', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address', full_name='com.gamehero.sxd2.pro.Simple.address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ps', full_name='com.gamehero.sxd2.pro.Simple.ps', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=43,
  serialized_end=134,
)


_SIMPLETEST = _descriptor.Descriptor(
  name='SimpleTest',
  full_name='com.gamehero.sxd2.pro.SimpleTest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='simple', full_name='com.gamehero.sxd2.pro.SimpleTest.simple', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=136,
  serialized_end=195,
)

_SIMPLETEST.fields_by_name['simple'].message_type = _SIMPLE
DESCRIPTOR.message_types_by_name['Simple'] = _SIMPLE
DESCRIPTOR.message_types_by_name['SimpleTest'] = _SIMPLETEST

class Simple(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIMPLE

  # @@protoc_insertion_point(class_scope:com.gamehero.sxd2.pro.Simple)

class SimpleTest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIMPLETEST

  # @@protoc_insertion_point(class_scope:com.gamehero.sxd2.pro.SimpleTest)


# @@protoc_insertion_point(module_scope)