#!/bin/evn python
#coding: UTF-8
#
#

from proto_render import ProtoRender
from protos.FateConfig_pb2 import FateConfig as Desc

class FateConfigRender(ProtoRender):
	def render(self, data):
		proto = Desc()
		#数据准备
		fate_bonus = data["fate_bonus"]
		fate_candle = data["fate_candle"]
		chapter = {}
		candles = {}
		for c in fate_candle:
			if c[1] == 6:
				candles[c[0]] = c[2]

		for b in fate_bonus:
			if not chapter.has_key(b[0]):
				proto.chpaters.taks_id = candles[b[0]]
			cell = proto.chpaters.celss.add()
			fields = cell.DESCRIPTOR.fields
			for i in range(len(fields)):
				field = fields[i]
				v = ProtoRender._validate(self, field,b[i+2])
				if not v:
					continue
				else:
					cell.__setattr__(field.name, v)
		return proto

