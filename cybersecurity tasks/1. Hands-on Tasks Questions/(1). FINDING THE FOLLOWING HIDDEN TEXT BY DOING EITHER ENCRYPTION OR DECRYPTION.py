import base64
decoded_bytes = base64.b64decode('eW91IGd1ZXNzZWQgaXQgcmlnaHQsIHRoaXMgaXMgQkFTRTY0ISE=')
decoded_text = decoded_bytes.decode('utf-8')
print(decoded_text)


