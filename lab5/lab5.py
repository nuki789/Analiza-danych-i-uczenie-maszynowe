import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
x2 = [0, 1, 2, 3, 4, 5]
y = [0, 1.1, 1.9, 3.2, 4.1, 5.15]
y2 = [0, 2*1.1, 2*1.9, 2*3.2, 2*4.1, 2*5.15]


plt.plot(x, y, '-<k')
plt.plot(x2, y2, '-db')
plt.title("Tytuł wykresu", fontsize = 20)
plt.axis(xmin = 1, xmax = 3, ymin = 1, ymax = 10)
plt.ylabel("Oś Y", fontsize = 20)
plt.xlabel("Oś X", fontsize = 20)
plt.legend(["w1", "w2"])
plt.grid()
plt.show()