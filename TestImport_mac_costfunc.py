from numpy import *
import numpy as np
from ctypes import *
import ctypes
n=100;
m=2;
xx=random.randn(n,m);
x1=ascontiguousarray(asarray(xx[:,0]));
x2=ascontiguousarray(asarray(xx[:,1]));
p=random.rand(2,1);
p1=p[0];
p2=p[1];
alpha=2.1;
ss=-78;
test=random.randn(20);
rest=empty_like(x1);

cv=ctypes.c_double;

#test1
myfun=cdll.LoadLibrary('test.so');

myfun.costFuncCore(ctypes.c_void_p(x1.ctypes.data),ctypes.c_void_p(x2.ctypes.data),ctypes.c_void_p(rest.ctypes.data),
	n,cv(p1),cv(p2),cv(alpha),cv(ss),
	ctypes.c_void_p(test.ctypes.data),len(test));

print rest

tSST=0;
D=sqrt((p1-x1)**2+(p2-x2)**2);
# print D
d0=1.6;
R=20*log10(D/d0);
for i in test:
	tSST=tSST+(ss-alpha*R-i)**2;
print tSST

print rest-tSST