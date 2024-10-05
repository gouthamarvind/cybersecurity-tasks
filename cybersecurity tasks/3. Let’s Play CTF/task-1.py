def decode_text(encoded_text):
    # Initialize an empty string to hold the decoded message
    decoded_message = ""

    # Loop through each character in the encoded text
    for char in encoded_text:
        # Check if the character is a printable ASCII character
        if ' ' <= char <= '~':
            # Process the character based on its ASCII value
            # Adjust the transformation logic based on your analysis
            if 'A' <= char <= 'Z':
                decoded_message += chr(((ord(char) - ord('A') + 1) % 26) + ord('A'))
            elif 'a' <= char <= 'z':
                decoded_message += chr(((ord(char) - ord('a') + 1) % 26) + ord('a'))
            elif '0' <= char <= '9':
                decoded_message += chr(((ord(char) - ord('0') + 1) % 10) + ord('0'))
            else:
                decoded_message += char  # Non-alphabetic characters remain unchanged

    return decoded_message

# Read the chaotic paragraph from the fil
