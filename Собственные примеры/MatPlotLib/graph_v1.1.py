#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
plt.style.use('seaborn-pastel')

n = int(input('Enter N '))
m = int(input('Enter M '))

fig = plt.figure()
#creating a subplot
# ax1 = fig.add_subplot(1,1,1)
ax1 = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
line, = ax1.plot([], [], lw=3)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Live graph with matplotlib')
plt.grid()

def init():
    line.set_data([], [])
    return line,

def animate(i):
    t = 0.1*i
    data = open('stock.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []
    # xss = [1, 5, 10, 15, 20]
    # yss = [1, 7, 3, 5, 11]
    # ax1.clear()
    print(lines)
    for item in lines:
        x, y = item.split(' ') # Delimiter is comma
        xs.append(float(x))
        ys.append(float(y))
    p = sns.lineplot(x=xs[:i], y=ys[:i], color='r')
    # ax1.plot(xs, ys, color='red')
    # ax1.plot(xss, yss, color='blue')
    # line.set_data(xs, ys)

    # p = sns.lineplot(x=xs[:i], y=ys[:i], color='r')
    # p.tick_params(labelsize=17)
    # plt.setp(p.lines, linewidth=7)
    # plt.plot(xs[:3], ys[:3], xs[3:len(xs)], ys[3:len(ys)])

ani = animation.FuncAnimation(fig, animate, frames=17, repeat=True)
plt.show()