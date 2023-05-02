def encode_string(input_str):
    ascii_binary_encoded_str_arr = [format(ord(c), 'b') for c in input_str]
    return ascii_binary_encoded_str_arr


def decode_string(binary_arr):
    output_str = ""
    for c in binary_arr:
        output_str += chr(int(str(c), 2))
    return output_str
