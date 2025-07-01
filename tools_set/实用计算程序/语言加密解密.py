def encrypt(text, shift):
    encrypted_text = []
    for char in text:
        # Get the Unicode code point of the character
        char_code = ord(char)
        # Shift the code point
        shifted_code = char_code + shift
        # Convert back to character and append to result
        encrypted_text.append(chr(shifted_code))
    return ''.join(encrypted_text)


def decrypt(text, shift):
    decrypted_text = []
    for char in text:
        # Get the Unicode code point of the character
        char_code = ord(char)
        # Shift the code point back
        shifted_code = char_code - shift
        # Convert back to character and append to result
        decrypted_text.append(chr(shifted_code))
    return ''.join(decrypted_text)


def main():
    while True:
        text = input("请输入要加密或解密的文本（输入q退出）：")
        if text.lower() == 'q':
            break

        choice = input("请选择操作 (加密输入21，解密输入-21)：")

        try:
            shift = int(choice)
            if shift == 21:
                result = encrypt(text, shift)
                print(f"加密后的文本：{result}")
            elif shift == -21:
                result = decrypt(text, -shift)
                print(f"解密后的文本：{result}")
            else:
                print("无效的选择，请输入21进行加密或-21进行解密。")
        except ValueError:
            print("无效的输入，请输入数字21或-21。")


if __name__ == "__main__":
    main()
