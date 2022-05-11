# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ovm.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ovm.proto',
  package='ovm',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tovm.proto\x12\x03ovm\")\n\x0eMoravecRequest\x12\x17\n\x04mood\x18\x01 \x01(\x0e\x32\t.ovm.Mood\"B\n\x0cKlausRequest\x12\x17\n\x04mood\x18\x01 \x01(\x0e\x32\t.ovm.Mood\x12\x19\n\x05sport\x18\x02 \x01(\x0e\x32\n.ovm.Sport\"B\n\x0cZemanRequest\x12\x17\n\x04mood\x18\x01 \x01(\x0e\x32\t.ovm.Mood\x12\x19\n\x05\x62ooze\x18\x02 \x01(\x0e\x32\n.ovm.Booze\";\n\x08Response\x12 \n\tsentences\x18\x01 \x03(\x0b\x32\r.ovm.Sentence\x12\r\n\x05score\x18\x02 \x01(\x05\"\x18\n\x08Sentence\x12\x0c\n\x04text\x18\x01 \x01(\t*8\n\x05\x42ooze\x12\n\n\x06\x42\x45\x43HER\x10\x00\x12\n\n\x06\x46\x45RNET\x10\x01\x12\x0b\n\x07JELINEK\x10\x02\x12\n\n\x06VIROZA\x10\x03*-\n\x05Sport\x12\n\n\x06TENNIS\x10\x00\x12\x07\n\x03SKI\x10\x01\x12\x06\n\x02\x46\x31\x10\x02\x12\x07\n\x03\x45GO\x10\x03*N\n\x04Mood\x12\x08\n\x04GOOD\x10\x00\x12\x1a\n\x16NOT_GREAT_NOT_TERRIBLE\x10\x02\x12\x07\n\x03\x42\x41\x44\x10\x03\x12\x17\n\x13NOT_THIS_SHIT_AGAIN\x10\x04\x32\xb2\x01\n\x14OtazkyVaclavaMoravce\x12\x35\n\rVaclavMoravec\x12\x13.ovm.MoravecRequest\x1a\r.ovm.Response\"\x00\x12\x31\n\x0bVaclavKlaus\x12\x11.ovm.KlausRequest\x1a\r.ovm.Response\"\x00\x12\x30\n\nMilosZeman\x12\x11.ovm.ZemanRequest\x1a\r.ovm.Response\"\x00\x62\x06proto3')
)

_BOOZE = _descriptor.EnumDescriptor(
  name='Booze',
  full_name='ovm.Booze',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BECHER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FERNET', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JELINEK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIROZA', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=284,
  serialized_end=340,
)
_sym_db.RegisterEnumDescriptor(_BOOZE)

Booze = enum_type_wrapper.EnumTypeWrapper(_BOOZE)
_SPORT = _descriptor.EnumDescriptor(
  name='Sport',
  full_name='ovm.Sport',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TENNIS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKI', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='F1', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGO', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=342,
  serialized_end=387,
)
_sym_db.RegisterEnumDescriptor(_SPORT)

Sport = enum_type_wrapper.EnumTypeWrapper(_SPORT)
_MOOD = _descriptor.EnumDescriptor(
  name='Mood',
  full_name='ovm.Mood',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GOOD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_GREAT_NOT_TERRIBLE', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_THIS_SHIT_AGAIN', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=389,
  serialized_end=467,
)
_sym_db.RegisterEnumDescriptor(_MOOD)

Mood = enum_type_wrapper.EnumTypeWrapper(_MOOD)
BECHER = 0
FERNET = 1
JELINEK = 2
VIROZA = 3
TENNIS = 0
SKI = 1
F1 = 2
EGO = 3
GOOD = 0
NOT_GREAT_NOT_TERRIBLE = 2
BAD = 3
NOT_THIS_SHIT_AGAIN = 4



_MORAVECREQUEST = _descriptor.Descriptor(
  name='MoravecRequest',
  full_name='ovm.MoravecRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mood', full_name='ovm.MoravecRequest.mood', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=59,
)


_KLAUSREQUEST = _descriptor.Descriptor(
  name='KlausRequest',
  full_name='ovm.KlausRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mood', full_name='ovm.KlausRequest.mood', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sport', full_name='ovm.KlausRequest.sport', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=127,
)


_ZEMANREQUEST = _descriptor.Descriptor(
  name='ZemanRequest',
  full_name='ovm.ZemanRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mood', full_name='ovm.ZemanRequest.mood', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='booze', full_name='ovm.ZemanRequest.booze', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=195,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ovm.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sentences', full_name='ovm.Response.sentences', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='ovm.Response.score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=256,
)


_SENTENCE = _descriptor.Descriptor(
  name='Sentence',
  full_name='ovm.Sentence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='ovm.Sentence.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=258,
  serialized_end=282,
)

_MORAVECREQUEST.fields_by_name['mood'].enum_type = _MOOD
_KLAUSREQUEST.fields_by_name['mood'].enum_type = _MOOD
_KLAUSREQUEST.fields_by_name['sport'].enum_type = _SPORT
_ZEMANREQUEST.fields_by_name['mood'].enum_type = _MOOD
_ZEMANREQUEST.fields_by_name['booze'].enum_type = _BOOZE
_RESPONSE.fields_by_name['sentences'].message_type = _SENTENCE
DESCRIPTOR.message_types_by_name['MoravecRequest'] = _MORAVECREQUEST
DESCRIPTOR.message_types_by_name['KlausRequest'] = _KLAUSREQUEST
DESCRIPTOR.message_types_by_name['ZemanRequest'] = _ZEMANREQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Sentence'] = _SENTENCE
DESCRIPTOR.enum_types_by_name['Booze'] = _BOOZE
DESCRIPTOR.enum_types_by_name['Sport'] = _SPORT
DESCRIPTOR.enum_types_by_name['Mood'] = _MOOD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MoravecRequest = _reflection.GeneratedProtocolMessageType('MoravecRequest', (_message.Message,), {
  'DESCRIPTOR' : _MORAVECREQUEST,
  '__module__' : 'ovm_pb2'
  # @@protoc_insertion_point(class_scope:ovm.MoravecRequest)
  })
_sym_db.RegisterMessage(MoravecRequest)

KlausRequest = _reflection.GeneratedProtocolMessageType('KlausRequest', (_message.Message,), {
  'DESCRIPTOR' : _KLAUSREQUEST,
  '__module__' : 'ovm_pb2'
  # @@protoc_insertion_point(class_scope:ovm.KlausRequest)
  })
_sym_db.RegisterMessage(KlausRequest)

ZemanRequest = _reflection.GeneratedProtocolMessageType('ZemanRequest', (_message.Message,), {
  'DESCRIPTOR' : _ZEMANREQUEST,
  '__module__' : 'ovm_pb2'
  # @@protoc_insertion_point(class_scope:ovm.ZemanRequest)
  })
_sym_db.RegisterMessage(ZemanRequest)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'ovm_pb2'
  # @@protoc_insertion_point(class_scope:ovm.Response)
  })
_sym_db.RegisterMessage(Response)

Sentence = _reflection.GeneratedProtocolMessageType('Sentence', (_message.Message,), {
  'DESCRIPTOR' : _SENTENCE,
  '__module__' : 'ovm_pb2'
  # @@protoc_insertion_point(class_scope:ovm.Sentence)
  })
_sym_db.RegisterMessage(Sentence)



_OTAZKYVACLAVAMORAVCE = _descriptor.ServiceDescriptor(
  name='OtazkyVaclavaMoravce',
  full_name='ovm.OtazkyVaclavaMoravce',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=470,
  serialized_end=648,
  methods=[
  _descriptor.MethodDescriptor(
    name='VaclavMoravec',
    full_name='ovm.OtazkyVaclavaMoravce.VaclavMoravec',
    index=0,
    containing_service=None,
    input_type=_MORAVECREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='VaclavKlaus',
    full_name='ovm.OtazkyVaclavaMoravce.VaclavKlaus',
    index=1,
    containing_service=None,
    input_type=_KLAUSREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MilosZeman',
    full_name='ovm.OtazkyVaclavaMoravce.MilosZeman',
    index=2,
    containing_service=None,
    input_type=_ZEMANREQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_OTAZKYVACLAVAMORAVCE)

DESCRIPTOR.services_by_name['OtazkyVaclavaMoravce'] = _OTAZKYVACLAVAMORAVCE

# @@protoc_insertion_point(module_scope)
