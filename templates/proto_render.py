#!/bin/evn python
# coding: UTF-8
# author: albin(albinyewen@gmail.com)
#

from google.protobuf import message
from google.protobuf.descriptor import FieldDescriptor

class ProtoRender(object):
    # static type map
    __maps = [None, 
        int,
        int,
        int,
        int,
        float,
        float,
        bool,
        int,
        unicode,
        object
    ]

    def common_render(self, data, desc):
        print data
        field = desc.DESCRIPTOR.fields
        if len(field) > 1:
            print ('[Error] mixed structes, %s' % desc.DESCRIPTOR.name)

        proto = desc()
        attr_name = field[0].name
        child = proto.__getattribute__(attr_name).add()
        fields = child.DESCRIPTOR.fields

        if len(data[0]) < len(fields):
            print ('[Error] xls has not enough fields for %s' % proto.DESCRIPTOR.name)
            return None

        proto = desc()
        for row in data:
            child = proto.__getattribute__(attr_name).add()
            for i in range(len(fields)):
                field = fields[i]
                v = ProtoRender._validate(self, field, row[i])
                if not v:
                    break
                child.__setattr__(field.name, v)
        return proto

    def render(self, data):
        self._builder = self._desc.__getattribute__(self._msg)
        # todo common render 

    def _validate(self, field, value):
        if not isinstance(field, FieldDescriptor):
            raise ("[Error] logic error in _validate, field must be type FieldDescriptor")
            return False
        t = ProtoRender.__maps[field.cpp_type]
        if ((isinstance(value, str) and len(value) == 0) or value == None) and field.label == FieldDescriptor.LABEL_OPTIONAL:
            return False
        if not isinstance(value, t):
            try:
                return t(value)
                return True
            except:
                raise (r"[Error] value error, %s need %s but %s" % (field.name, t, type(value)))
                return False
        else:
            return value
        return False

