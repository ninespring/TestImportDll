from ctypes import *
# mydll=windll.LoadLibrary('TestSum.dll')
import os
print os.getcwd();
dllpath=os.getcwd();
os.environ['PATH']=";".join([dllpath,os.environ['PATH']]);
mydll=cdll.LoadLibrary(os.path.join(dllpath,'TestSum.dll'))