import pyaudio
import numpy as np

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 40


def get_color(freq):
    if freq > 0 and freq <= 300:
        # return "#800080"
        return "\u001b[44m" + str(freq)
    elif freq > 300 and freq <= 1500:
        # return "#00FFFF"
        return "\u001b[46m" + str(freq)
    elif freq > 1500 and freq <= 5000:
        # return "#98FF98"
        return "\u001b[42m" + str(freq)
    elif freq > 5000 and freq <= 19000:
        # return "#FF0090"
        return "\u001b[45m" + str(freq)
    elif freq > 19000:
        # return "#E3242B"
        return "\u001b[41m" + str(freq)


def get_peak_frequency(data):
    data = data * np.hanning(len(data))  # smooth the FFT by windowing data
    fft = abs(np.fft.fft(data).real)
    fft = fft[:int(len(fft)/2)]

    fft_freq = np.fft.fftfreq(data.size, 1.0/RATE)
    fft_freq = fft_freq[:int(len(fft))]
    # focus on only the positive frequencies
    pos_mask = np.where(fft_freq > 0)
    fft_freq = fft_freq[pos_mask]

    peak_freq = fft_freq[fft[pos_mask].argmax()]

    # print(f"peak frequency: {peak_freq} Hz")
    return int(peak_freq * 2)


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("Started Listening")


while True:
    try:
        raw_data = stream.read(CHUNK)
        data = np.frombuffer(raw_data, dtype=np.int16)
        freq = get_peak_frequency(data)
        print(get_color(freq))

    except KeyboardInterrupt:
        print("\nStopped")
        stream.stop_stream()
        stream.close()
        p.terminate()
