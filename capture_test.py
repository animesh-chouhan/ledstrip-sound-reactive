# https://www.youtube.com/watch?v=AShHJdSIxkY&ab_channel=MarkJay

import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024 * 250
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

raw_data = stream.read(CHUNK)
data = np.frombuffer(raw_data, dtype=np.int16)
plt.plot(data)
plt.show()
