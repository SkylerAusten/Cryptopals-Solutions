from base64 import b64encode, b64decode

def hex_to_b64(hex_str: str) -> str:
    """Convert a hexadecimal string to a base64 encoded string.

    Converts the input hexadecimal string into bytes, encodes it into base64,
    and then decodes it to a UTF-8 string.

    Args:
        hex_str (str): A string consisting of hexadecimal digits only.

    Returns:
        str: A base64-encoded string corresponding to the input hexadecimal string.

    Raises:
        ValueError: If the input string is not a valid hexadecimal.
    """
    try:
        # Convert hex to bytes and then bytes to base64.
        return b64encode(bytes.fromhex(hex_str)).decode()
    except ValueError as e:
        # Re-raise an exception with a more explanatory message.
        raise ValueError("Invalid hexadecimal input.") from e

if __name__ == "__main__":
    test_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected_output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    # Function test with detailed output.
    result = hex_to_b64(test_input)
    assert result == expected_output, f"Test failed: expected {expected_output}, got {result}"
    print("Test passed.")

    # Display the base64 decoded message.
    print("Decoded message:", b64decode(expected_output.encode()).decode())
