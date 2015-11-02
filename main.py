#!/bin/evn python
# coding: UTF-8
# author: albin(albinyewen@gmail.com)

from xlslib import *
from templates import *
from protobuf_to_dict import protobuf_to_dict
import os

class XLSRender(object):
	def __init__(self, path):
		self._path = path
		self._dataSource = {}
		self._generate_sources()

	def _generate_sources(self):
		# generate data sources
		for root, dirs, files in os.walk('.'):
			for f in files:
				# maybe xlsx
				bName = f.split('.')
				if "xls" in bName[-1]: 
					full_path = os.path.join(root, f)
					print ("[Info] generate source %s" % full_path)
					self._dataSource[bName[0]] = sheet2list(full_path)

	def render(self, tmpl):
		return self._engine.render(tmpl, {"data":self._dataSource})

def main():
	render = XLSRender(os.path.join("sources", "xls"))
	data = render._dataSource

	for r in renders:
		proto = r().render(data)
		byts = open(os.path.join('binarys', proto.DESCRIPTOR.name + '.dat'), 'wb')
		byts.write(proto.SerializeToString())
		byts.close()

		# test
		# print (proto)
		rfile = open(os.path.join('binarys', proto.DESCRIPTOR.name + '.dat'), 'rb')
		rbytes = rfile.read()
		rfile.close()

		Desc = type(proto)
		t = Desc()
		t.MergeFromString(rbytes)
		print (protobuf_to_dict(t))
	raw_input()

if __name__ == '__main__':
	main()
