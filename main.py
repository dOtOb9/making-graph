import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 

sns.set_style("darkgrid")

fields = np.linspace(0, 2 * np.pi, 1000)

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

data = sin(fields)

data2 = cos(fields)

data3 = sin(fields) * cos(fields)

plt.plot(fields, data)
plt.plot(fields, data2)
plt.plot(fields, data3)


plt.title("Sin(x), Cos(x) and Sin(x) * Cos(x)")

plt.xlabel("x")
plt.ylabel("y")

fig = plt.legend(["Sin(x)", "Cos(x)", "Sin(x) * Cos(x)"])

plt.scatter([np.pi, np.pi], [np.sin(np.pi), np.cos(np.pi)], color="black")

plt.plot([np.pi, np.pi], [np.sin(np.pi), np.cos(np.pi)], linestyle="--", color="black")

plt.show()