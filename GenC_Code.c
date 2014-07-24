#include <stdio.h>
int sum(int a,int b){
	return a+b;
}

int resample(const void * indatav, int partcount, double randst ,void * outdatav , int round) {
    const double * indata = (double *) indatav;
    double * outdata = (double *) outdatav;
    int i;
    int j=0;
    int a;
    for (a = 0 ; a < round ; a++){
        double u0=(randst-1.0)/partcount;
        for(i=0 ; i<partcount ; i++){
        	u0+=1.0/partcount;
        	while (u0>indata[j]) {
                j++;
            }
        	outdata[i]=(double)j;
        }
    }
    return j;
}
#include "math.h"
#define sqr(x) ((x)*(x))
void costFuncCore(void * x1v,void * x2v, void * outdatav,int n, double p1,double p2, double alpha, double ss,void *testdatav, int td){
    double * x1 = (double *) x1v;
    double * x2 = (double *) x2v;
    double * testdata = (double *)testdatav;
    double * outdata = (double *)outdatav;
    printf("Successfully loaded.\n");
    int i;
    int j;
    for ( i = 0; i < n ; i ++){
        double d=sqrt(sqr(x1[i]-p1)+sqr(x2[i]-p2));
        double r=20*log10(d/1.6);
        double ts=0;
        for ( j = 0 ; j < td ; j ++){
            ts+=sqr(ss-alpha*r-testdata[j]);
        }
        outdata[i]=ts;
    }
}
