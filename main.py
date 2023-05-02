import wav_decoder
import wav_encoder
import wav_visualizer
import string_to_binary_encoder


if __name__ == '__main__':
    data_in = "hij ! dsds"
    sample_rate = 4410  # industry standard sample rate
    max_amplitude = 1  # the floating point value we want to assign to our 1 bits
    duration_ms_per_bit = 2  # The duration of the wav
    fn = "wave_file.wav"

    print(string_to_binary_encoder.encode_string(data_in))

    encoded_wav = wav_encoder.encode_wav_as_step_function(
        data_arr=string_to_binary_encoder.encode_string(data_in),
        sample_rate=sample_rate,
        max_amplitude=max_amplitude,
        duration_ms_per_bit=duration_ms_per_bit)

    wav_encoder.convert_wav_data_to_wav_file(wav_encoded_data=encoded_wav, sample_rate=sample_rate, fn=fn)


    wav_visualizer.visualize_wav_file(fn, duration_ms_per_bit)
    #wav_visualizer.visualize_wav_data(encoded_wav, duration_ms_per_bit)

    wav_decoder.decode_wave(fn=fn, duration_ms_per_bit=duration_ms_per_bit, max_amplitude=max_amplitude)


    #wav_visualizer.visualize_wav_data(encoded_wav, 500)

