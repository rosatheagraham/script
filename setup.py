from distutils.core import setup
import py2exe
import sys
import time

sys.path.append(r'C:/Users/user/Desktop/script/Microsoft Visual C runtime DLL')
sys.path.append(r'C:/Users/user/Desktop/script/static')
sys.path.append(r'C:/Users/user/Desktop/script/template')
sys.path.append(r'C:/Users/user/AppData/Local/Programs/Python/Python39/Lib/site-packages')

from glob import glob
data_files = [("Microsoft.VC90.CRT", glob(r'C:\Users\user\Desktop\script\Microsoft Visual C runtime DLL\*.*')),
("static", glob(r'C:\Users\user\Desktop\script\static\*.*')),
("templates", glob(r'C:\Users\user\Desktop\script\templates\*.*')),
(".", glob(r'C:\Users\user\AppData\Local\Programs\Python\Python39\Lib\site-packages\Python.Runtime.dll'))]

#options = {'includes': ['lxml._elementpath']}

#options = {
#           'py2exe':options,
#       }
        
#setup(options=options,data_files=data_files,windows=['script.py'])

setup(data_files=data_files,windows=['script.py'])

#setup(console=['script.py'])