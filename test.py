from numpy import *
A=random.rand(5000,2000);
B=random.rand(2000,3000);
print A.shape
print B.shape
import time
st=time.time()
C=A.dot(B);
ed=time.time();
print (ed-st)