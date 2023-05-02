def encode_string(input_str):
    """
    Encodes an input string as an ASCII binary representation
    :param input_str: string to be encoded
    :return: array that contains binary code for each character
    """
    ascii_binary_encoded_str_arr = [format(ord(c), 'b') for c in input_str]
    return ascii_binary_encoded_str_arr


def decode_string(binary_arr):
    """
    Decodes a binary array into thir ASCII characters
    :param binary_arr: binary character array: [10110101, 1001011 ... ] for each character
    :return: decoded string
    """
    output_str = ""
    for c in binary_arr:
        output_str += chr(int(str(c), 2))
    return output_str
