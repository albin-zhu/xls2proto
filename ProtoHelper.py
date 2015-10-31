#!/usr/bin/env python
# coding=UTF-8
# author: albin(albinyewen@gmail.com)

import protos
from google.protobuf import message
from google.protobuf.descriptor import FieldDescriptor

# 拿出所有proto的key值
__all_desc__ = [k for k in protos.__dict__.keys() if k[:2] != "__"]


"""protobuf的一些快捷方法，例如反射"""

class TypeDef(object):
    def __init__(self, type, isarray):
        self._type = type
        self._isarray = isarray

    @property
    def type(self):
        return self._type
    
    @property
    def is_arr(self):
        return self._isarray
    


class TypeMap(object):
    __maps = [None, 
        int,
        int,
        int,
        int,
        float,
        float,
        bool,
        int,
        str,
        object
    ]
    """docstring for TypeMap"""
    def __init__(self, arg):
        pass

    @staticmethod
    def get_type(desc):
        return TypeDef(TypeMap.__maps[desc.cpp_type], desc.label == FieldDescriptor.LABEL_REPEATED)
        


## 如果是简单类型直接返回 False
## 反之，反回所有keys
def is_msg_field(field):
    try:
        if issubclass(field,  message.Message):
            return True
    except:
        return False

def msg_to_dict(msg, objs):
    msg_name = msg.name
    msg_fields = msg.fields_by_name
    for field in msg_fields:
        child_msg = msg_fields[field]
        desc = TypeMap.get_type(child_msg)
        if desc.is_arr:
            objs[field] = []
            if desc.type == object:
                child_obj = {}
                msg_to_dict(child_msg.message_type, child_obj)
                objs[field].append(child_obj)
            else:
                objs[field].append(str(desc.type))
        else:
            if desc.type == object:
                child_obj = {}
                msg_to_dict(child_msg.message_type, child_obj)
                objs[field] = child_obj
            else:
                objs[field] = str(desc.type)


def get_protos_name():
    return __all_desc__
    
def get_proto_messages(proto):
    if type(proto) == str:
        if proto not in __all_desc__:
           return None
        proto = protos.__getattribute__(proto)
    
    return proto.DESCRIPTOR.message_types_by_name.keys()
    

def build_message(protofile, name):
    if protofile not in __all_desc__:
        return None
    proto = protos.__getattribute__(protofile)
    builder = proto.__getattribute__(name)

    if builder == None:
        return None
    return builder
    
def get_msg_fields(msg):
    return msg.DESCRIPTOR.fields_by_name
    
def __s(msg,  attr,  value):
    msg.__setattribute__(attr,  value)
    
def __g(msg,  attr):
    return msg.__getattribute__(attr)
