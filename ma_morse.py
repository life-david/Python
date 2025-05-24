import time

def decode_morse_character(morse_char):
    """{key: value}"""
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '`': ' '
    }

    return morse_dict.get(morse_char, '?')

# Nhập Morse code từ bàn phím
morse_code = input("Nhập Morse code (các ký tự cách nhau bằng khoảng trắng): ")

letters = morse_code.split(" ")  # Tách Morse code thành các ký tự riêng lẻ
decoded_text = ""

for letter in letters:
    decoded_char = decode_morse_character(letter)
    decoded_text += decoded_char
    print(f"{decoded_char}   {letter}")
    time.sleep(0.5)

time.sleep(0.8)
print(f"Kết quả giải mã: {decoded_text}")
