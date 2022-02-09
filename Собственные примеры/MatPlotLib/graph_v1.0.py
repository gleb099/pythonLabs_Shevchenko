#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('seaborn-pastel')

fig = plt.figure()
#creating a subplot
# ax1 = fig.add_subplot(1,1,1)
ax1 = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
line, = ax1.plot([], [], lw=3)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Live graph with matplotlib')

def init():
    line.set_data([], [])
    return line,

def animate(i):
    data = open('stock.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []
    # xss = [1, 5, 10, 15, 20]
    # yss = [1, 7, 3, 5, 11]
    # ax1.clear()
    for item in lines:
        x, y = item.split(' ') # Delimiter is comma
        xs.append(float(x))
        ys.append(float(y))
    # ax1.plot(xs, ys, color='red')
    # ax1.plot(xss, yss, color='blue')
    line.set_data(xs, ys)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=500, interval=200, blit=True)
plt.show()