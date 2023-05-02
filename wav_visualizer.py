import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read


def visualize_wav_data(wav_data, duration_ms):
    duration_x_values = np.arange(0, duration_ms, duration_ms / len(wav_data))
    plt.plot(duration_x_values, wav_data)
    plt.ylabel('amplitude')
    plt.xlabel('time (ms)')
    plt.show()


def visualize_wav_file(wav_fn, duration_ms):
    input_data = read(wav_fn)
    wav_data = input_data[1]
    duration_x_values = np.arange(0, duration_ms, duration_ms / len(wav_data))
    plt.plot(duration_x_values, wav_data)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.title("'Hello World!' Binary Encoded .Wav File Visualization")
    plt.show()
