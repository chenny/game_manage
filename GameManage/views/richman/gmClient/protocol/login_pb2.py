# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import db_cache_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='login.proto',
  package='',
  serialized_pb='\n\x0blogin.proto\x1a\x0e\x64\x62_cache.proto\"\x96\x01\n\x0c\x43\x32S_LoginReq\x12\x11\n\tuser_type\x18\x01 \x02(\x05\x12\x0f\n\x07user_id\x18\x02 \x02(\t\x12\x0c\n\x04sign\x18\x03 \x02(\t\x12\x11\n\ttimestamp\x18\x04 \x02(\x05\x12\x13\n\x0b\x63hannel_key\x18\x05 \x02(\t\x12\x16\n\x0e\x63lient_version\x18\x06 \x02(\t\x12\x14\n\x0cterminate_id\x18\x07 \x02(\t\"?\n\x0cS2C_LoginRsp\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07role_id\x18\x02 \x02(\x05\x12\x11\n\terror_msg\x18\x03 \x01(\x0c\"K\n\x0eLoginTotalInfo\x12#\n\nplayerInfo\x18\x01 \x02(\x0b\x32\x0f.DBCACHE.Player\x12\x14\n\x0cplaying_game\x18\x02 \x01(\x08\"(\n\x10S2C_RoleCardInfo\x12\x14\n\x0crolecardUuid\x18\x01 \x03(\x05\"7\n\x13\x43\x32S_Create_Role_Req\x12\x0e\n\x06\x63\x61rdId\x18\x01 \x02(\x05\x12\x10\n\x08nickName\x18\x02 \x02(\x0c\"\'\n\x13S2C_Create_Role_Rsp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\"$\n\x12\x43\x32S_LoginNotVerify\x12\x0e\n\x06userid\x18\x01 \x02(\x05\"D\n\x18S2C_Player_Card_List_Rsp\x12(\n\x0bplayer_card\x18\x01 \x03(\x0b\x32\x13.DBCACHE.PlayerCard\"A\n\x17S2C_Player_Die_List_Rsp\x12&\n\nplayer_die\x18\x01 \x03(\x0b\x32\x12.DBCACHE.PlayerDie\"/\n\x17\x43\x32S_Modify_NickName_Req\x12\x14\n\x0cnew_nickname\x18\x01 \x02(\x0c\"&\n\x17S2C_Modify_NickName_Rsp\x12\x0b\n\x03ret\x18\x01 \x02(\x05\"3\n\x19\x43\x32S_Modify_UnderWrite_Req\x12\x16\n\x0enew_underwrite\x18\x01 \x02(\x0c\"(\n\x19S2C_Modify_UnderWrite_Rsp\x12\x0b\n\x03ret\x18\x01 \x02(\x05\"_\n\x1aS2C_Notify_Player_Level_Up\x12\x11\n\tnew_level\x18\x01 \x02(\r\x12\x0f\n\x07new_exp\x18\x02 \x02(\r\x12\x1d\n\x06reward\x18\x03 \x01(\x0b\x32\r.DBCACHE.Prop\".\n\x1a\x43\x32S_Upload_Custom_Head_Req\x12\x10\n\x08new_head\x18\x01 \x02(\t\".\n\x1aS2C_Upload_Custom_Head_Rsp\x12\x10\n\x08ret_code\x18\x01 \x02(\x05\"[\n\x16S2C_New_System_Message\x12\x14\n\x0cmessage_type\x18\x01 \x02(\r\x12\x12\n\nmessage_id\x18\x02 \x02(\x05\x12\x17\n\x0fmessage_context\x18\x03 \x01(\x0c\"\xab\x01\n\x11S2C_Kick_Off_User\x12\x0e\n\x06reason\x18\x01 \x02(\x05\"\x85\x01\n\nKickReason\x12!\n\x1d\x61\x63\x63ount_login_in_orther_place\x10\x01\x12\x17\n\x13\x61\x63\x63ount_were_banned\x10\x02\x12\x14\n\x10service_has_stop\x10\x03\x12\x11\n\rlogin_timeout\x10\x04\x12\x12\n\x0eserver_is_full\x10\x05\"B\n S2C_Present_Points_Reward_Notify\x12\x0e\n\x06\x61mount\x18\x01 \x02(\r\x12\x0e\n\x06reason\x18\x02 \x02(\r')



_S2C_KICK_OFF_USER_KICKREASON = _descriptor.EnumDescriptor(
  name='KickReason',
  full_name='S2C_Kick_Off_User.KickReason',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='account_login_in_orther_place', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='account_were_banned', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='service_has_stop', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='login_timeout', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='server_is_full', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1150,
  serialized_end=1283,
)


_C2S_LOGINREQ = _descriptor.Descriptor(
  name='C2S_LoginReq',
  full_name='C2S_LoginReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_type', full_name='C2S_LoginReq.user_type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='C2S_LoginReq.user_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sign', full_name='C2S_LoginReq.sign', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='C2S_LoginReq.timestamp', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_key', full_name='C2S_LoginReq.channel_key', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_version', full_name='C2S_LoginReq.client_version', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='terminate_id', full_name='C2S_LoginReq.terminate_id', index=6,
      number=7, type=9, cpp_type=9, label=2,
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
  serialized_start=32,
  serialized_end=182,
)


_S2C_LOGINRSP = _descriptor.Descriptor(
  name='S2C_LoginRsp',
  full_name='S2C_LoginRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='S2C_LoginRsp.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='S2C_LoginRsp.role_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='S2C_LoginRsp.error_msg', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=184,
  serialized_end=247,
)


_LOGINTOTALINFO = _descriptor.Descriptor(
  name='LoginTotalInfo',
  full_name='LoginTotalInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerInfo', full_name='LoginTotalInfo.playerInfo', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playing_game', full_name='LoginTotalInfo.playing_game', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=249,
  serialized_end=324,
)


_S2C_ROLECARDINFO = _descriptor.Descriptor(
  name='S2C_RoleCardInfo',
  full_name='S2C_RoleCardInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rolecardUuid', full_name='S2C_RoleCardInfo.rolecardUuid', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=326,
  serialized_end=366,
)


_C2S_CREATE_ROLE_REQ = _descriptor.Descriptor(
  name='C2S_Create_Role_Req',
  full_name='C2S_Create_Role_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cardId', full_name='C2S_Create_Role_Req.cardId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickName', full_name='C2S_Create_Role_Req.nickName', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  serialized_start=368,
  serialized_end=423,
)


_S2C_CREATE_ROLE_RSP = _descriptor.Descriptor(
  name='S2C_Create_Role_Rsp',
  full_name='S2C_Create_Role_Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='S2C_Create_Role_Rsp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=425,
  serialized_end=464,
)


_C2S_LOGINNOTVERIFY = _descriptor.Descriptor(
  name='C2S_LoginNotVerify',
  full_name='C2S_LoginNotVerify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userid', full_name='C2S_LoginNotVerify.userid', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=466,
  serialized_end=502,
)


_S2C_PLAYER_CARD_LIST_RSP = _descriptor.Descriptor(
  name='S2C_Player_Card_List_Rsp',
  full_name='S2C_Player_Card_List_Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_card', full_name='S2C_Player_Card_List_Rsp.player_card', index=0,
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
  serialized_start=504,
  serialized_end=572,
)


_S2C_PLAYER_DIE_LIST_RSP = _descriptor.Descriptor(
  name='S2C_Player_Die_List_Rsp',
  full_name='S2C_Player_Die_List_Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_die', full_name='S2C_Player_Die_List_Rsp.player_die', index=0,
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
  serialized_start=574,
  serialized_end=639,
)


_C2S_MODIFY_NICKNAME_REQ = _descriptor.Descriptor(
  name='C2S_Modify_NickName_Req',
  full_name='C2S_Modify_NickName_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_nickname', full_name='C2S_Modify_NickName_Req.new_nickname', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  serialized_start=641,
  serialized_end=688,
)


_S2C_MODIFY_NICKNAME_RSP = _descriptor.Descriptor(
  name='S2C_Modify_NickName_Rsp',
  full_name='S2C_Modify_NickName_Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='S2C_Modify_NickName_Rsp.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=690,
  serialized_end=728,
)


_C2S_MODIFY_UNDERWRITE_REQ = _descriptor.Descriptor(
  name='C2S_Modify_UnderWrite_Req',
  full_name='C2S_Modify_UnderWrite_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_underwrite', full_name='C2S_Modify_UnderWrite_Req.new_underwrite', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  serialized_start=730,
  serialized_end=781,
)


_S2C_MODIFY_UNDERWRITE_RSP = _descriptor.Descriptor(
  name='S2C_Modify_UnderWrite_Rsp',
  full_name='S2C_Modify_UnderWrite_Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='S2C_Modify_UnderWrite_Rsp.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=783,
  serialized_end=823,
)


_S2C_NOTIFY_PLAYER_LEVEL_UP = _descriptor.Descriptor(
  name='S2C_Notify_Player_Level_Up',
  full_name='S2C_Notify_Player_Level_Up',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_level', full_name='S2C_Notify_Player_Level_Up.new_level', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_exp', full_name='S2C_Notify_Player_Level_Up.new_exp', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward', full_name='S2C_Notify_Player_Level_Up.reward', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=825,
  serialized_end=920,
)


_C2S_UPLOAD_CUSTOM_HEAD_REQ = _descriptor.Descriptor(
  name='C2S_Upload_Custom_Head_Req',
  full_name='C2S_Upload_Custom_Head_Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_head', full_name='C2S_Upload_Custom_Head_Req.new_head', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=922,
  serialized_end=968,
)


_S2C_UPLOAD_CUSTOM_HEAD_RSP = _descriptor.Descriptor(
  name='S2C_Upload_Custom_Head_Rsp',
  full_name='S2C_Upload_Custom_Head_Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='S2C_Upload_Custom_Head_Rsp.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=970,
  serialized_end=1016,
)


_S2C_NEW_SYSTEM_MESSAGE = _descriptor.Descriptor(
  name='S2C_New_System_Message',
  full_name='S2C_New_System_Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='S2C_New_System_Message.message_type', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='S2C_New_System_Message.message_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_context', full_name='S2C_New_System_Message.message_context', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=1018,
  serialized_end=1109,
)


_S2C_KICK_OFF_USER = _descriptor.Descriptor(
  name='S2C_Kick_Off_User',
  full_name='S2C_Kick_Off_User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='S2C_Kick_Off_User.reason', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _S2C_KICK_OFF_USER_KICKREASON,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1112,
  serialized_end=1283,
)


_S2C_PRESENT_POINTS_REWARD_NOTIFY = _descriptor.Descriptor(
  name='S2C_Present_Points_Reward_Notify',
  full_name='S2C_Present_Points_Reward_Notify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='S2C_Present_Points_Reward_Notify.amount', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='S2C_Present_Points_Reward_Notify.reason', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=1285,
  serialized_end=1351,
)

_LOGINTOTALINFO.fields_by_name['playerInfo'].message_type = db_cache_pb2._PLAYER
_S2C_PLAYER_CARD_LIST_RSP.fields_by_name['player_card'].message_type = db_cache_pb2._PLAYERCARD
_S2C_PLAYER_DIE_LIST_RSP.fields_by_name['player_die'].message_type = db_cache_pb2._PLAYERDIE
_S2C_NOTIFY_PLAYER_LEVEL_UP.fields_by_name['reward'].message_type = db_cache_pb2._PROP
_S2C_KICK_OFF_USER_KICKREASON.containing_type = _S2C_KICK_OFF_USER;
DESCRIPTOR.message_types_by_name['C2S_LoginReq'] = _C2S_LOGINREQ
DESCRIPTOR.message_types_by_name['S2C_LoginRsp'] = _S2C_LOGINRSP
DESCRIPTOR.message_types_by_name['LoginTotalInfo'] = _LOGINTOTALINFO
DESCRIPTOR.message_types_by_name['S2C_RoleCardInfo'] = _S2C_ROLECARDINFO
DESCRIPTOR.message_types_by_name['C2S_Create_Role_Req'] = _C2S_CREATE_ROLE_REQ
DESCRIPTOR.message_types_by_name['S2C_Create_Role_Rsp'] = _S2C_CREATE_ROLE_RSP
DESCRIPTOR.message_types_by_name['C2S_LoginNotVerify'] = _C2S_LOGINNOTVERIFY
DESCRIPTOR.message_types_by_name['S2C_Player_Card_List_Rsp'] = _S2C_PLAYER_CARD_LIST_RSP
DESCRIPTOR.message_types_by_name['S2C_Player_Die_List_Rsp'] = _S2C_PLAYER_DIE_LIST_RSP
DESCRIPTOR.message_types_by_name['C2S_Modify_NickName_Req'] = _C2S_MODIFY_NICKNAME_REQ
DESCRIPTOR.message_types_by_name['S2C_Modify_NickName_Rsp'] = _S2C_MODIFY_NICKNAME_RSP
DESCRIPTOR.message_types_by_name['C2S_Modify_UnderWrite_Req'] = _C2S_MODIFY_UNDERWRITE_REQ
DESCRIPTOR.message_types_by_name['S2C_Modify_UnderWrite_Rsp'] = _S2C_MODIFY_UNDERWRITE_RSP
DESCRIPTOR.message_types_by_name['S2C_Notify_Player_Level_Up'] = _S2C_NOTIFY_PLAYER_LEVEL_UP
DESCRIPTOR.message_types_by_name['C2S_Upload_Custom_Head_Req'] = _C2S_UPLOAD_CUSTOM_HEAD_REQ
DESCRIPTOR.message_types_by_name['S2C_Upload_Custom_Head_Rsp'] = _S2C_UPLOAD_CUSTOM_HEAD_RSP
DESCRIPTOR.message_types_by_name['S2C_New_System_Message'] = _S2C_NEW_SYSTEM_MESSAGE
DESCRIPTOR.message_types_by_name['S2C_Kick_Off_User'] = _S2C_KICK_OFF_USER
DESCRIPTOR.message_types_by_name['S2C_Present_Points_Reward_Notify'] = _S2C_PRESENT_POINTS_REWARD_NOTIFY

class C2S_LoginReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_LOGINREQ

  # @@protoc_insertion_point(class_scope:C2S_LoginReq)

class S2C_LoginRsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_LOGINRSP

  # @@protoc_insertion_point(class_scope:S2C_LoginRsp)

class LoginTotalInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGINTOTALINFO

  # @@protoc_insertion_point(class_scope:LoginTotalInfo)

class S2C_RoleCardInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_ROLECARDINFO

  # @@protoc_insertion_point(class_scope:S2C_RoleCardInfo)

class C2S_Create_Role_Req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_CREATE_ROLE_REQ

  # @@protoc_insertion_point(class_scope:C2S_Create_Role_Req)

class S2C_Create_Role_Rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_CREATE_ROLE_RSP

  # @@protoc_insertion_point(class_scope:S2C_Create_Role_Rsp)

class C2S_LoginNotVerify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_LOGINNOTVERIFY

  # @@protoc_insertion_point(class_scope:C2S_LoginNotVerify)

class S2C_Player_Card_List_Rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_PLAYER_CARD_LIST_RSP

  # @@protoc_insertion_point(class_scope:S2C_Player_Card_List_Rsp)

class S2C_Player_Die_List_Rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_PLAYER_DIE_LIST_RSP

  # @@protoc_insertion_point(class_scope:S2C_Player_Die_List_Rsp)

class C2S_Modify_NickName_Req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_MODIFY_NICKNAME_REQ

  # @@protoc_insertion_point(class_scope:C2S_Modify_NickName_Req)

class S2C_Modify_NickName_Rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_MODIFY_NICKNAME_RSP

  # @@protoc_insertion_point(class_scope:S2C_Modify_NickName_Rsp)

class C2S_Modify_UnderWrite_Req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_MODIFY_UNDERWRITE_REQ

  # @@protoc_insertion_point(class_scope:C2S_Modify_UnderWrite_Req)

class S2C_Modify_UnderWrite_Rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_MODIFY_UNDERWRITE_RSP

  # @@protoc_insertion_point(class_scope:S2C_Modify_UnderWrite_Rsp)

class S2C_Notify_Player_Level_Up(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_NOTIFY_PLAYER_LEVEL_UP

  # @@protoc_insertion_point(class_scope:S2C_Notify_Player_Level_Up)

class C2S_Upload_Custom_Head_Req(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_UPLOAD_CUSTOM_HEAD_REQ

  # @@protoc_insertion_point(class_scope:C2S_Upload_Custom_Head_Req)

class S2C_Upload_Custom_Head_Rsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_UPLOAD_CUSTOM_HEAD_RSP

  # @@protoc_insertion_point(class_scope:S2C_Upload_Custom_Head_Rsp)

class S2C_New_System_Message(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_NEW_SYSTEM_MESSAGE

  # @@protoc_insertion_point(class_scope:S2C_New_System_Message)

class S2C_Kick_Off_User(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_KICK_OFF_USER

  # @@protoc_insertion_point(class_scope:S2C_Kick_Off_User)

class S2C_Present_Points_Reward_Notify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_PRESENT_POINTS_REWARD_NOTIFY

  # @@protoc_insertion_point(class_scope:S2C_Present_Points_Reward_Notify)


# @@protoc_insertion_point(module_scope)