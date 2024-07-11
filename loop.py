import random
import time
import matplotlib.pyplot as plt
import numpy as np

num=1
K=[]
tm=0
#num = random.randint(1, 9)

while True:
    L = []
    def func(n):
        global tm
        global L
        k = n
        L.append(k)
        print(L)
        print(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        n = int(n)
        #time.sleep(1)
        tm+=1
        if k != 1:
            func(n)
        #else:
         #   y = np.array(L)
          #  plt.plot(y)
           # plt.show()
    func(num)
    print("No of runs taken: "+str(len(L)-1))
    K.append(len(L)-1)
    num+=1
    if num>200:
        break
K[0]=K[1]
L.clear()
func(K.index(max(K))+1)
y = np.array(L)
plt.plot(y)
plt.show()
print(K)
print("Min value with max runs: "+str(K.index(max(K))+1))
print("No of runs for {} : ".format(str(K.index(max(K))+1))+str(max(K)))
print("Total time taken: "+str(tm)+" seconds")