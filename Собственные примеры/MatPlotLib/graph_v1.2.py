#importing libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
from matplotlib import rcParams

rcParams['animation.convert_path'] = r'/usr/bin/convert'

plt.style.use('seaborn-pastel')

n = int(input('Enter N '))
m = int(input('Enter M '))

# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)

fig = plt.figure()
#creating a subplot
# ax1 = fig.add_subplot(1,1,1)
ax1 = plt.axes(xlim=(0, 200), ylim=(0, 200))
line, = ax1.plot([], [], lw=1)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gif')
plt.grid()

# def init():
#     line.set_data([], [])
#     return line,

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
            #временные массивы для Х Y чтобы их отоброжать поочереди
            dx.append(temp_x[j])
            dy.append(temp_y[j])
        # print(dx)
        # print(dy)
        p = sns.lineplot(x=dx[:i], y=dy[:i], color='r')
        nold=nnew
        nnew=nnew+n
        temp_i += 1
    return line,

    # while temp_i != 3:
    #     dx = list()
    #     dy = list()
    #     for j in range(nold, nnew):
    #         #временные массивы для Х Y чтобы их отоброжать поочереди
    #         dx.append(temp_x[j])
    #         dy.append(temp_y[j])
    #     # print(dx)
    #     # print(dy)
    #     # p = sns.lineplot(x=dx[:i], y=dy[:i], color='r')
    #     line.set_data(dx[:i], dy[:i])
    #     print(1)
    #     nold=nnew
    #     nnew=nnew+n
    #     temp_i += 1
    # return line,

myAnimation = animation.FuncAnimation(fig, animate, frames=n+10, interval=10, repeat=False)
# ani.save('test.mp4', writer=writer)
plt.show()
# myAnimation.save('myAnimation.gif', writer='imagemagick', fps=30)