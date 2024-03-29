import numpy as np
import joint_positions as ag
from matplotlib import pyplot as plt
from matplotlib import animation

plt.rcParams["figure.figsize"] = [7.50, 7.50]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
xdata, ydata = [], []
xdata2, ydata2 = [], []
ln, = plt.plot([], [], color='yellow')
ln2, = plt.plot([], [], color='black')


def init_wave():
    ax.set_xlim(0, 2 * ag.WAVELENGTH)
    ax.set_ylim(-ag.WAVELENGTH, 1 * ag.WAVELENGTH)
    ln.set_data([], [])
    ln2.set_data([], [])
    return ln, ln2


def update_wave(frame):
    found_coords = ag.find_joint_coords(
        lambda x: ag.AMPLITUDE * np.sin((2 * np.pi / ag.WAVELENGTH) * x - (np.pi / 100) * frame))
    ln2.set_data(found_coords[0], found_coords[1])
    x = np.linspace(0, ag.WAVELENGTH * 2)
    y = ag.AMPLITUDE * np.sin((2 * np.pi / ag.WAVELENGTH) * x - np.pi / 100 * frame)
    ln.set_data(x, y)
    return ln, ln2


def do_wave_animation():
    anim = animation.FuncAnimation(fig, update_wave, init_func=init_wave, frames=200, interval=10, blit=True)
    plt.show()
    # f = r"C:\Users\Alex\PycharmProjects\Sidewinder\animation.gif"
    # writergif = animation.PillowWriter(fps=30)
    # anim.save(f, writer=writergif)

if __name__ == "__main__":
    do_wave_animation()
