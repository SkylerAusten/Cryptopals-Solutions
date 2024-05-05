def fixed_xor(hex_1: str, hex_2: str) -> str:
    """XOR two same-length hexadecimal strings.

    This function takes two hexadecimal strings of equal length and returns a new
    hexadecimal string that represents the bitwise XOR of the two inputs.

    Args:
        hex_1 (str): The first hexadecimal string.
        hex_2 (str): The second hexadecimal string.

    Returns:
        str: The result of XOR'ing the two input strings.

    Raises:
        ValueError: If either 'hex_1' or 'hex_2' are not valid hexadecimal strings.
        ValueError: If 'hex_1' and 'hex_2' do not have the same length.
    """
    if len(hex_1) != len(hex_2):
        raise ValueError("Both hex strings must be of the same length.")
    
    try:
        # Convert hex to bytes, XOR them, and convert back to hex.
        byte_array = bytes(a ^ b for a, b in zip(bytes.fromhex(hex_1), bytes.fromhex(hex_2)))
        return byte_array.hex()
    except ValueError:
        raise ValueError("Invalid hexadecimal input(s).")

if __name__ == "__main__":
    test_input_1 = "1c0111001f010100061a024b53535009181c"
    test_input_2 = "686974207468652062756c6c277320657965"
    expected_output = "746865206b696420646f6e277420706c6179"

    # Test the function.
    result = fixed_xor(test_input_1, test_input_2)
    print("Test result:", result)
    assert result == expected_output, "Test failed."