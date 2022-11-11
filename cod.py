import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

uno = np.loadtxt("uno.txt")
dos = np.loadtxt("dos.txt")
tre = np.loadtxt("tre.txt")
fire = np.loadtxt("fire.txt")

def derive(data):
    a = []
    x = data[:,0]
    y = data[:,1]
    for i in range(len(x)):
        if i == 0:
            i = 1
        a.append((y[i]-y[i-1])/(x[i]-x[i-1]))
    return a

def average(arr, length):
    a = []
    for i in range(length):
        a.append(mean(arr))
    return a

figure, axis = plt.subplots(2, 2, sharey=True)

axis[0, 0].grid()
axis[0, 0].set_title("uno")

axis[0, 1].grid()
axis[0, 1].set_title("dos")

axis[1, 0].grid()
axis[1, 0].set_title("tre")

axis[1, 1].grid()
axis[1, 1].set_title("fire")

axis[0, 0].plot(uno[:,0], derive(uno), label='speed')
axis[0, 1].plot(dos[:,0], derive(dos), label='speed')
axis[1, 0].plot(tre[:,0], derive(tre), label='speed')
axis[1, 1].plot(fire[:,0], derive(fire), label='speed')

axis[0, 0].plot(uno[:,0], average(derive(uno), len(uno[:,1])), label='avg speed')
axis[0, 1].plot(dos[:,0], average(derive(dos), len(dos[:,1])), label='avg speed')
axis[1, 0].plot(tre[:,0], average(derive(tre), len(tre[:,1])), label='avg speed')
axis[1, 1].plot(fire[:,0], average(derive(fire), len(fire[:,1])), label='avg speed')

axis[0, 0].legend()
axis[0, 1].legend()
axis[1, 0].legend()
axis[1, 1].legend()

plt.ylim(0, 5)

print(f"uno speed^2 = {average(derive(uno), len(uno[:,1]))[0]**2}")
print(f"dos speed^2 = {average(derive(dos), len(dos[:,1]))[0]**2}")
print(f"tre speed^2 = {average(derive(tre), len(tre[:,1]))[0]**2}")
print(f"fire speed^2 = {average(derive(fire), len(fire[:,1]))[0]**2}")

plt.show()