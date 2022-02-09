import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams
import seaborn as sns

rcParams['animation.convert_path'] = r'/usr/bin/convert'
plt.style.use('seaborn-pastel')

fig, ax = plt.subplots()

n = int(input('Enter N '))
m = int(input('Enter M '))

ax = plt.axes(xlim=(0, 200), ylim=(0, 200))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gif')
plt.grid()

point = ax.plot()

def animate(i):
    data = open('stock.txt','r').read()
    lines = data.split('\n')

    temp_x = list()
    temp_y = list()
    for item in lines:
        x, y = item.split('\t')
        temp_x.append(float(x))
        temp_y.append(float(y))
    nold = 0
    nnew = n
    temp_i = 0
    while temp_i != (len(temp_x) // n):
        dx = list()
        dy = list()
        for j in range(nold, nnew):
            dx.append(temp_x[j])
            dy.append(temp_y[j])
        p = sns.lineplot(x=dx[:i], y=dy[:i], color='r')
        #p = plt.scatter(x=dx[:i], y=dy[:i], color='r')
        nold=nnew
        nnew=nnew+n
        temp_i += 1
    return p

myAnimation = animation.FuncAnimation(fig, animate, frames=n+20, \
                                      interval=10, repeat=False)

myAnimation.save('myAnimation.gif', writer='imagemagick', fps=30)