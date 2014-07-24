from numpy import *
from ctypes import *
import ctypes
n=500;
x=arange(n);
weights=random.rand(n,1);
weights/=weights.sum();
print sum(weights)
print len(weights)
#input
ln=int(n);
C=cumsum(weights);
indices=empty_like(weights);
# u0=random.random();
u0=0.5;
print u0;

myfun=cdll.LoadLibrary('test.so')
import time
rnd=1;
st=time.time()
myfun.resample(ctypes.c_void_p(C.ctypes.data), ctypes.c_int(n), ctypes.c_double(u0), ctypes.c_void_p(indices.ctypes.data), ctypes.c_int(rnd))
ed=time.time();
print "TimeCost=%s, AveCost=%s" %(ed-st,(ed-st)/rnd)
print indices
#Calculation
# def fun1(C,indices,u0,n):
# 	myfun = cdll.LoadLibrary('test.so');
# 	myfun.resample(ctypes.c_void_p(C.ctypes.data), ctypes.c_int(n), ctypes.c_double(u0), ctypes.c_void_p(indices.ctypes.data))
# 	return indices

def fun2(C,indices,u0,n):
	j=0;
	Li=(u0+arange(n))*(1./n);
	print Li
	for i in xrange(n):
		while Li[i] > C[j]:
			j+=1
		indices[i]=j;
		print "%s,%s,%s,%s" %(i,j,Li[i],C[j])
	return indices
# fun2(C,indices,u0,n);
# ind1=fun1(C,indices,u0,n);
# ind2=fun2(C,indices,u0,n);
# print ind1
# print ind2
# print ind1-ind2