import numpy as np
#import wave
from  scipy.io import wavfile
import struct
import random


def calculate_num_bits(data_arr):
    # Flatten the binary list of characters to calculate the total number of characters
    len_data_arr = len("".join(data_arr))
    # Add 1 bit seperator for each character
    len_data_arr += len(data_arr)
    # Don't need a filler for the last character
    return len_data_arr - 1


def encode_wav_as_step_function(data_arr, sample_rate, max_amplitude, duration_ms_per_bit):
    """
    Encodes the binary data array as a wav data array to be used to generate thw wav file
    :param data: binary input array
    :param sample_rate: number of samples per second used
    :param max_amplitude: what floating point value characterizes a 1 (in binary)
    :param duration_ms:  duration of wav file
    :return: numpy array to be used in generating wav file
    """

    # use the sample rate and duration to calculate the number of samples we need to generate
    # we divide the sample rate by 1000 because the duration is in ms, not seconds and the
    # sample rate is in Hz (samples per second)
    num_samples = int(duration_ms_per_bit * (sample_rate / 1000))

    num_samples = (calculate_num_bits(data_arr) + 1) * int(duration_ms_per_bit * (sample_rate / 1000))

    # Holder numpy array already with the 0 bits filled in
    wav_data = np.zeros(num_samples)

    # calculate the number of samples we need to generate per bit
    samples_per_bit = int(num_samples / calculate_num_bits(data_arr))

    # We store the last index for each binary encoded character
    last_end_idx = 0
    temp_end_idx = 0
    for bin_character in data_arr:
        # iterate through each bit to be encoded
        for i in range(len(bin_character)):
            # Find the starting index in the wav array for this bit
            start_idx = (i * samples_per_bit) + last_end_idx
            # Find the ending index in the wav array for this bit
            end_idx = start_idx + samples_per_bit

            # Fill in all those values in the array with the bits value
            wav_data[start_idx:end_idx] = bin_character[i] * max_amplitude

            # Create temporary index so the seperator bit can be added
            temp_end_idx = end_idx

        last_end_idx = temp_end_idx
        # Add the seperator bit between each binary encoded character, set to half amplitude for decoding
        wav_data[last_end_idx:last_end_idx+samples_per_bit] = max_amplitude / 2
        # Update our index calculations
        last_end_idx = last_end_idx+samples_per_bit

    return wav_data


def convert_wav_data_to_wav_file(wav_encoded_data, sample_rate, fn):
    #wav_file = wave.open("wav_file.wav", "w")


    # wav_file.setnchannels(1)
    # wav_file.setsampwidth(2)
    # wav_file.setframerate(sample_rate)
    #
    # for sample in wav_encoded_data:
    #     data = struct.pack('<h', int(sample * 32767.0))
    #     wav_file.writeframesraw(data)
    #
    #    # wav_file.writeframesraw(struct.pack('h', int(sample * 32767.0)))

    wavfile.write(fn, sample_rate, wav_encoded_data)

    #wav_file.close()
