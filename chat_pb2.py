# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='chat',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nchat.proto\x12\x04\x63hat\",\n\x0b\x43hatMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x19\n\x05\x43ores\x12\x10\n\x04\x64\x61ta\x18\x01 \x03(\x05\x42\x02\x10\x01\"\x12\n\x03\x43or\x12\x0b\n\x03\x63or\x18\x01 \x01(\x05\"\x18\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\x08\"#\n\x03Pos\x12\x0b\n\x03\x63or\x18\x01 \x01(\x05\x12\x0f\n\x03pos\x18\x02 \x03(\x05\x42\x02\x10\x01\"\xa3\x01\n\tTabuleiro\x12\x11\n\x05line1\x18\x01 \x03(\x05\x42\x02\x10\x01\x12\x11\n\x05line2\x18\x02 \x03(\x05\x42\x02\x10\x01\x12\x11\n\x05line3\x18\x03 \x03(\x05\x42\x02\x10\x01\x12\x11\n\x05line4\x18\x04 \x03(\x05\x42\x02\x10\x01\x12\x11\n\x05line5\x18\x05 \x03(\x05\x42\x02\x10\x01\x12\x11\n\x05line6\x18\x06 \x03(\x05\x42\x02\x10\x01\x12\x11\n\x05line7\x18\x07 \x03(\x05\x42\x02\x10\x01\x12\x11\n\x05line8\x18\x08 \x03(\x05\x42\x02\x10\x01\"\x07\n\x05\x45mpty2\x9b\x03\n\x04\x43hat\x12-\n\x0bSendMessage\x12\x11.chat.ChatMessage\x1a\x0b.chat.Empty\x12\x32\n\x0eReceiveMessage\x12\x0b.chat.Empty\x1a\x11.chat.ChatMessage0\x01\x12,\n\x10\x43oresDisponiveis\x12\x0b.chat.Empty\x1a\x0b.chat.Cores\x12&\n\x0b\x43hoiceColor\x12\t.chat.Cor\x1a\x0c.chat.Status\x12$\n\nTurnoAtual\x12\x0b.chat.Empty\x1a\t.chat.Cor\x12(\n\rTrocarDeTurno\x12\t.chat.Cor\x1a\x0c.chat.Status\x12.\n\x0eTabuleiroAtual\x12\x0b.chat.Empty\x1a\x0f.chat.Tabuleiro\x12*\n\x0f\x43hangeTabuleiro\x12\t.chat.Pos\x1a\x0c.chat.Status\x12.\n\x10RefreshTabuleiro\x12\x0b.chat.Empty\x1a\x0b.chat.Empty0\x01\x62\x06proto3'
)




_CHATMESSAGE = _descriptor.Descriptor(
  name='ChatMessage',
  full_name='chat.ChatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chat.ChatMessage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='chat.ChatMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=20,
  serialized_end=64,
)


_CORES = _descriptor.Descriptor(
  name='Cores',
  full_name='chat.Cores',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='chat.Cores.data', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=66,
  serialized_end=91,
)


_COR = _descriptor.Descriptor(
  name='Cor',
  full_name='chat.Cor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cor', full_name='chat.Cor.cor', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=93,
  serialized_end=111,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='chat.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='chat.Status.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=113,
  serialized_end=137,
)


_POS = _descriptor.Descriptor(
  name='Pos',
  full_name='chat.Pos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cor', full_name='chat.Pos.cor', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pos', full_name='chat.Pos.pos', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=139,
  serialized_end=174,
)


_TABULEIRO = _descriptor.Descriptor(
  name='Tabuleiro',
  full_name='chat.Tabuleiro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='line1', full_name='chat.Tabuleiro.line1', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line2', full_name='chat.Tabuleiro.line2', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line3', full_name='chat.Tabuleiro.line3', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line4', full_name='chat.Tabuleiro.line4', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line5', full_name='chat.Tabuleiro.line5', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line6', full_name='chat.Tabuleiro.line6', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line7', full_name='chat.Tabuleiro.line7', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line8', full_name='chat.Tabuleiro.line8', index=7,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=177,
  serialized_end=340,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='chat.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=342,
  serialized_end=349,
)

DESCRIPTOR.message_types_by_name['ChatMessage'] = _CHATMESSAGE
DESCRIPTOR.message_types_by_name['Cores'] = _CORES
DESCRIPTOR.message_types_by_name['Cor'] = _COR
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['Pos'] = _POS
DESCRIPTOR.message_types_by_name['Tabuleiro'] = _TABULEIRO
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChatMessage = _reflection.GeneratedProtocolMessageType('ChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _CHATMESSAGE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.ChatMessage)
  })
_sym_db.RegisterMessage(ChatMessage)

Cores = _reflection.GeneratedProtocolMessageType('Cores', (_message.Message,), {
  'DESCRIPTOR' : _CORES,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Cores)
  })
_sym_db.RegisterMessage(Cores)

Cor = _reflection.GeneratedProtocolMessageType('Cor', (_message.Message,), {
  'DESCRIPTOR' : _COR,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Cor)
  })
_sym_db.RegisterMessage(Cor)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Status)
  })
_sym_db.RegisterMessage(Status)

Pos = _reflection.GeneratedProtocolMessageType('Pos', (_message.Message,), {
  'DESCRIPTOR' : _POS,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Pos)
  })
_sym_db.RegisterMessage(Pos)

Tabuleiro = _reflection.GeneratedProtocolMessageType('Tabuleiro', (_message.Message,), {
  'DESCRIPTOR' : _TABULEIRO,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Tabuleiro)
  })
_sym_db.RegisterMessage(Tabuleiro)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:chat.Empty)
  })
_sym_db.RegisterMessage(Empty)


_CORES.fields_by_name['data']._options = None
_POS.fields_by_name['pos']._options = None
_TABULEIRO.fields_by_name['line1']._options = None
_TABULEIRO.fields_by_name['line2']._options = None
_TABULEIRO.fields_by_name['line3']._options = None
_TABULEIRO.fields_by_name['line4']._options = None
_TABULEIRO.fields_by_name['line5']._options = None
_TABULEIRO.fields_by_name['line6']._options = None
_TABULEIRO.fields_by_name['line7']._options = None
_TABULEIRO.fields_by_name['line8']._options = None

_CHAT = _descriptor.ServiceDescriptor(
  name='Chat',
  full_name='chat.Chat',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=352,
  serialized_end=763,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='chat.Chat.SendMessage',
    index=0,
    containing_service=None,
    input_type=_CHATMESSAGE,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReceiveMessage',
    full_name='chat.Chat.ReceiveMessage',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CHATMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CoresDisponiveis',
    full_name='chat.Chat.CoresDisponiveis',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CORES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChoiceColor',
    full_name='chat.Chat.ChoiceColor',
    index=3,
    containing_service=None,
    input_type=_COR,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TurnoAtual',
    full_name='chat.Chat.TurnoAtual',
    index=4,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_COR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TrocarDeTurno',
    full_name='chat.Chat.TrocarDeTurno',
    index=5,
    containing_service=None,
    input_type=_COR,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TabuleiroAtual',
    full_name='chat.Chat.TabuleiroAtual',
    index=6,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_TABULEIRO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChangeTabuleiro',
    full_name='chat.Chat.ChangeTabuleiro',
    index=7,
    containing_service=None,
    input_type=_POS,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RefreshTabuleiro',
    full_name='chat.Chat.RefreshTabuleiro',
    index=8,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHAT)

DESCRIPTOR.services_by_name['Chat'] = _CHAT

# @@protoc_insertion_point(module_scope)
