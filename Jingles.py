import base64
import codecs
import base36
import base32_crockford
import base64

# Given encoded values
encoded_values = [
    "SmluZ2xlcyhJX1dpTExf",
    "\\x4e\\x33\\x76\\x33\\x72\\x5f\\x47\\x31\\x76\\x33\\x5f",
    "II2GGS27KRUDG===",
    "95 83 110 48 119 71",
    "01101100 00110000 01100010 00110011 00100001 00100001 01111101",
]

def Jingles(value):
    return base64.b64decode(value).decode('utf-8')

def Stole(value):
    hex_values = value.split('\\x')[1:]
    decoded = ''.join([chr(int(hex_value, 16)) for hex_value in hex_values])
    return decoded

def SnowGlobes(value):
    return base64.b32decode(value).decode('utf-8')

def Santa(value):
    decimal_values = value.split()
    decoded = ''.join([chr(int(decimal_value)) for decimal_value in decimal_values])
    return decoded

def VeryMad(value):
    binary_values = value.split()
    decoded = ''.join([chr(int(binary_value, 2)) for binary_value in binary_values])
    return decoded

# Decoding and printing values
for i, encoded_value in enumerate(encoded_values, start=1):
    decoded_value = None
    if i == 1:
        decoded_value = Jingles(encoded_value)
    elif i == 2:
        decoded_value = Stole(encoded_value)
    elif i == 3:
        decoded_value = SnowGlobes(encoded_value)
    elif i == 4:
        decoded_value = Santa(encoded_value)
    elif i == 5:
        decoded_value = VeryMad(encoded_value)

    print(f"Encoded Value {i}: {encoded_value}")
    print(f"Decoded Value {i}: {decoded_value}")
    print("=" * 30)
