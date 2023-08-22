def get_eng_alphabet() -> str:
    return "".join([chr(i) for i in range(ord("!"), ord("~") + 1)])


def get_ru_alphabet() -> str:
    return "".join([chr(i) for i in range(ord("А"), ord("я") + 1)])


def get_base_string_alphabet() -> str:
    return f"{get_eng_alphabet()} {get_ru_alphabet()}"


def get_key_string(mode="encrypt"):
    our_string = input(f"Enter key for {mode}: ")
    if our_string is None or our_string == "":
        our_string = "1key2!"
    return our_string


def get_string(mode="encrypt"):
    our_string = input(f"Enter string for {mode}: ")
    if our_string is None or our_string == "":
        our_string = (
            "Hello everybody! Это тестовая , "
            "строка для шифрования! 'цитаты' "
            "123456789 0 - = ! @ # $ % ^ & * ( ) _ +"
        )
    return our_string


def get_shift_key(key: str, position: int, lenght_string: int) -> int:
    return ord(key[position]) + position % lenght_string


def get_encrypt_decrypt_string(string_for_crypt, key, mode="encrypt", debug=False) -> str:
    string_for_code = ""
    our_alphabet = get_base_string_alphabet()
    position_key = -1
    for i in range(len(string_for_crypt)):
        position_key = position_key + 1
        if position_key > len(key) - 1:
            position_key = 0
        shift = get_shift_key(key, position_key, len(string_for_crypt))
        if debug:
            print(f"char from key: {key[position_key]} -> shift: {shift}")
        position = our_alphabet.find(string_for_crypt[i])
        if position == -1:
            # if we don't know char, simple set the same char
            string_for_code = string_for_code + string_for_crypt[i]

        elif mode == "decrypt":
            new_position = position - shift
            if new_position < 0:
                new_position = new_position % len(our_alphabet)
            string_for_code = string_for_code + our_alphabet[new_position]

        elif mode == "encrypt":
            new_position = position + shift
            if new_position > len(our_alphabet) - 1:
                new_position = new_position % len(our_alphabet)
            string_for_code = string_for_code + our_alphabet[new_position]

    return string_for_code


# def main_encrypt_decrypt(mode="encrypt", debug=False):
#     # String for encrypt/decrypt
#     str_for_in = get_string(mode=mode)
#     print(f"Your message is : {str_for_in}")
#     # Key for encrypt/decrypt
#     key = get_key_string(mode=mode)
#     print(f"Key for {mode} : {key}")
#     # result encrypt/decrypt
#     str_for_out = get_encrypt_decrypt_string(str_for_in, key, mode=mode, debug=debug)
#     print(f"{mode.capitalize()} : {str_for_out}")


# def main():
#     print("Start app encrypt / decode ->")
#     mode = "encrypt"
#     debug = False
#     while True:
#         select_mode = input("Select mode: \n "
#                             "1. Encrypt \n "
#                             "2. Decrypt \n "
#                             f"7. Debug mode ({debug}) \n "
#                             "9 End app \n "
#                             "-> ")
#         if select_mode == "1":
#             mode = "encrypt"
#         elif select_mode == "2":
#             mode = "decrypt"
#         elif select_mode == "7":
#             debug = not debug
#             if debug:
#                 print(get_base_string_alphabet())
#             continue
#         elif select_mode == "9":
#             break
#         main_encrypt_decrypt(mode=mode, debug=debug)
