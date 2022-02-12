import zlib
import base64

filewrite = open("obfuscate.txt", "w")
filewrite.write(base64.b64encode(zlib.compress(b"""import os\n
os.system('cmd.exe')""")).decode())
filewrite.close()

freadf=open("obfuscate.txt", "r")
deob=zlib.decompress(base64.b64decode(freadf.read()))  
code=compile(deob, 'mulstring', 'exec')
exec(code)