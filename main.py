import wav_decoder
import wav_encoder
import wav_visualizer
import string_to_binary_encoder
import argparse

if __name__ == '__main__':

    # Add our command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_string', type=str, required=True)
    parser.add_argument('--sample_rate', type=int, required=False, default=4410)
    parser.add_argument('--duration_per_bit', type=int, required=False, default=2)
    parser.add_argument('--wav_file_name', type=str, required=False, default="wav_file.wav")

    # Parse arguments
    args = parser.parse_args()
    data_in = args.input_string
    sample_rate = args.sample_rate
    max_amplitude = 1 # the floating point value we want to assign to our 1 bits
    duration_ms_per_bit = args.duration_per_bit  # The duration of the wav
    fn = args.wav_file_name

    # Call the encoder
    encoded_wav = wav_encoder.encode_wav_as_step_function(
        data_arr=string_to_binary_encoder.encode_string(data_in),
        sample_rate=sample_rate,
        max_amplitude=max_amplitude,
        duration_ms_per_bit=duration_ms_per_bit)

    # Save the encoded values to wav file
    wav_encoder.convert_wav_data_to_wav_file(wav_encoded_data=encoded_wav, sample_rate=sample_rate, fn=fn)

    # Visualize both the binary wav data and the wav file
    wav_visualizer.visualize_wav_file(fn, duration_ms_per_bit)
    wav_visualizer.visualize_wav_data(encoded_wav, duration_ms_per_bit)

    # Decode wav file
    decoded_string = wav_decoder.decode_wave(fn=fn, duration_ms_per_bit=duration_ms_per_bit, max_amplitude=max_amplitude)

    # Print out the interesting stuff
    print(f"Binary Data In Per Character: \n {string_to_binary_encoder.encode_string(data_in)}")
    print(f".Wav encoded binary data: \n {encoded_wav}")
    print(f"Output decoded string: {decoded_string}")

