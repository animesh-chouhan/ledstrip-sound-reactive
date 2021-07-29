import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 40
WAVE_OUTPUT_FILENAME = "output.wav"

# freq_data = []


def get_peak_frequency(data):
    data = data * np.hanning(len(data))  # smooth the FFT by windowing data
    fft = abs(np.fft.fft(data).real)
    fft = fft[:int(len(fft)/2)]

    fft_freq = np.fft.fftfreq(CHUNK, 1.0/RATE)
    fft_freq = fft_freq[:int(len(fft))]

    print(len(fft))
    print(len(fft_freq))
    index = np.where(fft == np.max(fft))[0][0]

    freqPeak = int(fft_freq[index])
    # freq_data.append(freqPeak)
    # print(f"peak frequency: {freqPeak} Hz")
    return freqPeak


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    raw_data = stream.read(CHUNK)
    # data = np.fromstring(raw_data, dtype=np.int16)
    data = np.frombuffer(raw_data, dtype=np.int16)
    # stream.write(data, CHUNK)
    frames.append(data)
    print(get_peak_frequency(data))

# while 1:
#     data = stream.read(CHUNK)
#     stream.write(data, CHUNK)
#     frames.append(data)


print("* done recording")

stream.stop_stream()
stream.close()

# # detect devices:
# p = pyaudio.PyAudio()
# host_info = p.get_host_api_info_by_index(0)
# device_count = host_info.get('deviceCount')
# devices = []

# # iterate between devices:
# for i in range(0, device_count):
#     device = p.get_device_info_by_host_api_device_index(0, i)
#     devices.append(device['name'])

# print(devices)

# # Print devices
# for i in range(p.get_device_count()):
#     print(p.get_device_info_by_index(i))

p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


# plt.hist(freq_data, bins=100)
# plt.show()
