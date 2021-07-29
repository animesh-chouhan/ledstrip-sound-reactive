from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

rate, audio = wavfile.read('nightingale.wav')

N = audio.shape[0]
L = N / rate
print(f"Audio length: {L:.2f} seconds")


# fig, ax = plt.subplots()
# ax.plot(np.arange(N) / rate, audio)
# ax.set_xlabel('Time [s]')
# ax.set_ylabel('Amplitude [unknown]')

# plt.show()

fft = abs(np.fft.fft(audio).real)
fft = fft[:int(len(fft)/2)]
print(len(fft))

fft_freq = np.fft.fftfreq(audio.size, 1.0/rate)
fft_freq = fft_freq[:int(len(fft_freq)/2)]
print(len(fft_freq))

# plt.hist(fft, bins=100)
# plt.show()

plt.plot(fft_freq, fft)
# plt.xlim(-50, 50)
# plt.ylim(-600, 600)
# plt.legend(loc=1)
plt.title("FFT in Frequency Domain")

plt.show()
