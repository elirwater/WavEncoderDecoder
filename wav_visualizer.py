import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read


def visualize_wav_data(wav_data, duration_ms):
    """
    Visual represenation of the binary encoded wav data
    :param wav_data: binary data array
    :param duration_ms: duration per bit in milliseconds (this is something that would normally
    be in a protocol)
    """
    duration_x_values = np.arange(0, duration_ms, duration_ms / len(wav_data))
    plt.plot(duration_x_values, wav_data)
    plt.ylabel('Amplitude')
    plt.xlabel('Time (ms)')
    plt.title("Visualized Binary Character Data for .Wav File")
    plt.show()


def visualize_wav_file(wav_fn, duration_ms):
    """
    Visual representation of .wav file
    :param wav_fn: filepath
    :param duration_ms: duration per bit in milliseconds (this is something that would normally
    be in a protocol)
    """
    input_data = read(wav_fn)
    wav_data = input_data[1]
    duration_x_values = np.arange(0, duration_ms, duration_ms / len(wav_data))
    plt.plot(duration_x_values, wav_data)
    plt.ylabel("Amplitude")
    plt.xlabel("Time (ms)")
    plt.title("Visualized .Wav File")
    plt.show()
