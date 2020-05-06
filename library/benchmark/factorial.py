import time

def fact(n):             
    r=1           
    t1=time.ticks_us()                     
    while n>1:                  
        r=r*n                 
        n=n-1                 
    t2=time.ticks_us()                          
    print('elapsed: ', time.ticks_diff(t1,t2), 'us')                                     
    return r
