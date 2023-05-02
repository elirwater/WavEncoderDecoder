from scipy.io import wavfile
import string_to_binary_encoder

def decode_wave(fn, duration_ms_per_bit, max_amplitude):
    sample_rate, data = wavfile.read(fn)

    # Includes seperator character, this is the number of binary encoded values we have
    # ex. "h" -> [1101000] -> tons of 1s and 0s ->
    num_character_bits = (len(data) / int(duration_ms_per_bit * (sample_rate / 1000)))
    num_data_points_per_character_bit = int(len(data) / num_character_bits)

    print(data)

    output_binary_character_arr = []
    # We know there are x number of data points per character bit, so we iterate based on that factor
    # through our binary data
    character_binary_str = ""
    for i in range(0, len(data) - num_data_points_per_character_bit, num_data_points_per_character_bit):
        # If we hit a seperator bit, we move to the next character
        if data[i] == (max_amplitude / 2):
            output_binary_character_arr.append(character_binary_str)
            character_binary_str = ""
        else:
            character_binary_str += str(int(data[i]))
    output_binary_character_arr.append(character_binary_str)
    print(output_binary_character_arr)

    print(string_to_binary_encoder.decode_string(output_binary_character_arr))


