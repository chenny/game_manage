// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: rcm_cmd.proto

#ifndef PROTOBUF_rcm_5fcmd_2eproto__INCLUDED
#define PROTOBUF_rcm_5fcmd_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 2005000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 2005000 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/generated_enum_reflection.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)

namespace rcm {

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_rcm_5fcmd_2eproto();
void protobuf_AssignDesc_rcm_5fcmd_2eproto();
void protobuf_ShutdownFile_rcm_5fcmd_2eproto();

class RCM_CMD;

enum RCM_CMD_CMD {
  RCM_CMD_CMD_CMD_CLIENT_LONGIN_REQ = 12290,
  RCM_CMD_CMD_CMD_CLIENT_LONGIN_RESP = 12291
};
bool RCM_CMD_CMD_IsValid(int value);
const RCM_CMD_CMD RCM_CMD_CMD_CMD_MIN = RCM_CMD_CMD_CMD_CLIENT_LONGIN_REQ;
const RCM_CMD_CMD RCM_CMD_CMD_CMD_MAX = RCM_CMD_CMD_CMD_CLIENT_LONGIN_RESP;
const int RCM_CMD_CMD_CMD_ARRAYSIZE = RCM_CMD_CMD_CMD_MAX + 1;

const ::google::protobuf::EnumDescriptor* RCM_CMD_CMD_descriptor();
inline const ::std::string& RCM_CMD_CMD_Name(RCM_CMD_CMD value) {
  return ::google::protobuf::internal::NameOfEnum(
    RCM_CMD_CMD_descriptor(), value);
}
inline bool RCM_CMD_CMD_Parse(
    const ::std::string& name, RCM_CMD_CMD* value) {
  return ::google::protobuf::internal::ParseNamedEnum<RCM_CMD_CMD>(
    RCM_CMD_CMD_descriptor(), name, value);
}
// ===================================================================

class RCM_CMD : public ::google::protobuf::Message {
 public:
  RCM_CMD();
  virtual ~RCM_CMD();

  RCM_CMD(const RCM_CMD& from);

  inline RCM_CMD& operator=(const RCM_CMD& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const RCM_CMD& default_instance();

  void Swap(RCM_CMD* other);

  // implements Message ----------------------------------------------

  RCM_CMD* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const RCM_CMD& from);
  void MergeFrom(const RCM_CMD& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  typedef RCM_CMD_CMD CMD;
  static const CMD CMD_CLIENT_LONGIN_REQ = RCM_CMD_CMD_CMD_CLIENT_LONGIN_REQ;
  static const CMD CMD_CLIENT_LONGIN_RESP = RCM_CMD_CMD_CMD_CLIENT_LONGIN_RESP;
  static inline bool CMD_IsValid(int value) {
    return RCM_CMD_CMD_IsValid(value);
  }
  static const CMD CMD_MIN =
    RCM_CMD_CMD_CMD_MIN;
  static const CMD CMD_MAX =
    RCM_CMD_CMD_CMD_MAX;
  static const int CMD_ARRAYSIZE =
    RCM_CMD_CMD_CMD_ARRAYSIZE;
  static inline const ::google::protobuf::EnumDescriptor*
  CMD_descriptor() {
    return RCM_CMD_CMD_descriptor();
  }
  static inline const ::std::string& CMD_Name(CMD value) {
    return RCM_CMD_CMD_Name(value);
  }
  static inline bool CMD_Parse(const ::std::string& name,
      CMD* value) {
    return RCM_CMD_CMD_Parse(name, value);
  }

  // accessors -------------------------------------------------------

  // @@protoc_insertion_point(class_scope:rcm.RCM_CMD)
 private:

  ::google::protobuf::UnknownFieldSet _unknown_fields_;


  mutable int _cached_size_;
  ::google::protobuf::uint32 _has_bits_[1];

  friend void  protobuf_AddDesc_rcm_5fcmd_2eproto();
  friend void protobuf_AssignDesc_rcm_5fcmd_2eproto();
  friend void protobuf_ShutdownFile_rcm_5fcmd_2eproto();

  void InitAsDefaultInstance();
  static RCM_CMD* default_instance_;
};
// ===================================================================


// ===================================================================

// RCM_CMD


// @@protoc_insertion_point(namespace_scope)

}  // namespace rcm

#ifndef SWIG
namespace google {
namespace protobuf {

template <>
inline const EnumDescriptor* GetEnumDescriptor< ::rcm::RCM_CMD_CMD>() {
  return ::rcm::RCM_CMD_CMD_descriptor();
}

}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_rcm_5fcmd_2eproto__INCLUDED
