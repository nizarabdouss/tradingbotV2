from tokenize import PlainToken
import matplotlib.pyplot as plt 
import time

def currElapsed(t) -> float:
    return float(time.process_time() - t)

def getVolume(v)->float:
    vol = sum(v)
    return vol

def plotChart(c) -> None:
    x = []
    y =[]
    v = []
    for i in c:
        y.append(float(i[0]))
        v.append(float(i[1])/float(i[0]))
    for i in range(len(c)):
        x.append(i+1)
    plt.plot(x, y, label = 'BTC')
    plt.bar(x, v, label = 'Volume')
    plt.legend()
    plt.show()
'''
volume.append(float(res['q'])*float(res['p']))
            if 0.59 < currElapsed(T) <= 0.6:
                chart.append((res['p'], getVolume(volume)))
                T = time.process_time()
                plotChart(chart)
'''

plot = [('28958.57000000', 2141734.889630001), ('28972.10000000', 3402910.993751401), ('28920.71000000', 4735489.2290182), ('28915.93000000', 7269988.480987691), ('28969.79000000', 9915397.280514084), ('29017.88000000', 11795868.392296785), ('28942.65000000', 13888804.845489074), ('28961.99000000', 16077466.73976158), ('20000',0)]

plotChart(plot)