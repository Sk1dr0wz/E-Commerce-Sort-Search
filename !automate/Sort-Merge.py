from subprocess import Popen, PIPE
import os

p = Popen(['python', 'main.py'], cwd=os.path.dirname(os.getcwd()), stdin=PIPE, stdout=PIPE, shell=False)
out = p.communicate(input=b'2\n2\n1\n2\n3\n4\n4\n4\n', timeout=5)
print(str(out[0]).replace('\\r\\n', '\n'))