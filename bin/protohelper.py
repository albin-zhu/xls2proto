#!/usr/bin/env python
# coding=UTF-8

import os, sys
import tenjin
from tenjin.helpers import *
import shutil

# step 1 生成 protobuf python代码
os.system(r"protoc -I=..\proto --python_out=..\protos ..\proto\*")

# step2 生成包结构 生成序列化类
tenjin = tenjin.Engine()
t = open(r"..\protos\__init__.py", "w")
init_py = open(r"..\templates\__init__.py", "w")
init_py.write('renders = []\n')
for root, dirs, files in os.walk(r"..\protos"):
	for f in files:
		if f.split('.')[-1] == "py" and "__init__" not in f:
			file_name = f[:-3]
			t.write("import " + file_name + '\n')
			proto = f[:-7]
			tmpl = open(r"outputs\%s_render.py" % proto, 'w')
			tmpl.write(tenjin.render(r"templates\template.pytmpl", {'proto':proto}))
			init_py.write('from %s_render import %sRender\n' % (proto, proto))
			init_py.write('renders.append(%sRender)\n' % proto)
			tmpl.close()
t.close()
init_py.close()

# step3 还没想好


