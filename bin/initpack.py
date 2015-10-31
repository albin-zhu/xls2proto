import os
import sys

p = sys.argv[1:][0]
t = open(os.path.join(p,"__init__.py"), "w")
for root, dirs, files in os.walk(p):
	for f in files:
		if f.split('.')[-1] == "py" and "__init__" not in f:
			t.write("import " + f[:-3] + '\n')

t.close()
	