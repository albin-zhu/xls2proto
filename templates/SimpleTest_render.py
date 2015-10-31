#!/bin/evn python

#coding: UTF-8

from proto_render import ProtoRender

from protos.SimpleTest_pb2 import SimpleTest as Desc

class SimpleTestRender(ProtoRender):

	def __init__(self):

		ProtoRender.__init__(self)



	def render(self, data):
		return ProtoRender.common_render(self, data["simple_test"], Desc)



