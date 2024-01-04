import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 

sns.set_style("darkgrid")

fields = np.linspace(0, 2 * np.pi)

def sin(x):
    return np.sin(x)

def cos(x):
    return np.cos(x)

data = sin(fields)

data2 = cos(fields)

plt.plot(fields, data)
ax = plt.plot(fields, data2)


plt.title("Sin(x) and Cos(x)")

plt.xlabel("x")
plt.ylabel("y")
fig = plt.legend(["Sin(x)", "Cos(x)"])

plt.scatter([np.pi, np.pi], [np.sin(np.pi), np.cos(np.pi)], color="green")

plt.plot([np.pi, np.pi], [np.sin(np.pi), np.cos(np.pi)], linestyle="--", color="black")


plt.show()