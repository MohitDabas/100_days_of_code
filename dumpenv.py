from ctypes import *
from ctypes.wintypes import *
import ctypes

GetEnvironmentStringsW = cdll.kernel32.GetEnvironmentStringsW
GetEnvironmentStringsW.restype = c_void_p
GetEnvironmentStringsW.argtypes = []

str_pointer = GetEnvironmentStringsW()
string = ctypes.wstring_at(str_pointer)

env_vars = {}
while string != '':
        if string[0].isalpha():
            name, value = string.split(u'=', 1)
            env_vars[name.encode('ascii')] = value
        # Include the trailing null byte, and measure each
        # char as 2 bytes since Windows uses UTF-16 for
        # wide chars
        str_pointer += (len(string) + 1) * 2
        string = ctypes.wstring_at(str_pointer)
        print(string)
