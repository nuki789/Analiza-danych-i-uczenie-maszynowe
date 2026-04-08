import matplotlib.pyplot as plt
import math as mt

x = [i * 0.01 for i in range(0, 1200)]

y1 = []
y2 = []
y3 = []
y4 = []

for i in x:
    y1.append(mt.sin(i))
    y2.append(mt.cos(i))
    y3.append(2 * mt.sin(5 * i))
    y4.append(3 * mt.cos(2 * i))

plt.plot(x, y1, '-k')
plt.plot(x, y2, '-b')
plt.plot(x, y3, '-r')
plt.plot(x, y4, '-g')

plt.title("Tytuł wykresu", fontsize = 20)
#plt.axis(xmin = 1, xmax = 3, ymin = 1, ymax = 10)
plt.ylabel("Oś Y", fontsize = 20)
plt.xlabel("Oś X", fontsize = 20)
plt.legend(["w1", "w2", "w3", "w4"])
plt.grid()
plt.show()
