import random
import numpy as np
import matplotlib.pyplot as mp
x=[]
y=[]
for i in range(50):
    x.append(random.uniform(-1,1))
    x.append(random.uniform(-1,1))
    x.append(1)
#    x.append(a)
#    a.clear()
    y.append(random.uniform(-1,1))
    y.append(random.uniform(-1,1))
    y.append(1)

#print(y)
w=[[1,1,0],[-1,-1,0],[0,0.5,0],[1,-1,5],[1.0,1.0,0.3]]
xa=[]
ya=[]
xb=[]
yb=[]
for i in range(0,150,3):
    xa.append(x[i])
    xb.append(x[i+1])
    ya.append(y[i])
    yb.append(y[i+1])

xa = np.asarray(xa)
xb = np.asarray(xb)
ya = np.asarray(ya)
yb = np.asarray(yb)

for i in range(5):
    correct=0
    for j in range(0,150,3):
        ans=w[i][0]*x[j] + w[i][1]*x[j+1] + w[i][2]*x[j+2]
        if(ans>0):
            correct = correct+1

        ans2=w[i][0]*y[j] + w[i][1]*y[j+1] + w[i][2]*y[j+2]
        if(ans2<0):
            correct = correct+1
    res = correct/100
    print(res)
    mp.figure()
    mp.scatter(xa, ya, color="green")
    mp.scatter(xb, yb, color="red")
    txt="w =[" + str(w[i][0]) + ',' + str(w[i][1])+ ',' + str(w[i][2]) + "]" + ", Accuracy=" + str(res)
    xi=np.linspace(-1,1,100)
    yi=(-w[i][2] - w[i][0]*xi)/w[i][1]
    mp.plot(xi, yi)
    mp.title(txt)
    mp.show()
