import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack


f = 10
f_s = 100

t = np.linspace(0, 2, 2 * f_s, endpoint=False)
x = np.sin(2 * np.pi * f * t)


# fig, ax = plt.subplots()
# ax.plot(t, x)
# ax.set_xlabel("Time [s]")
# ax.set_ylabel("Amplitude")

X = fftpack.fft(x)
X = X[:int(len(X)/2)]
freqs = fftpack.fftfreq(len(x)) * f_s
freqs = freqs[:int(len(freqs)/2)]
print(freqs)

fig, ax = plt.subplots()

ax.stem(freqs, np.abs(X))
ax.set_xlabel('Frequency in Hertz [Hz]')
ax.set_ylabel('Frequency Domain (Spectrum) Magnitude')
ax.set_xlim(-f_s / 2, f_s / 2)
ax.set_ylim(-5, 110)

plt.show()
