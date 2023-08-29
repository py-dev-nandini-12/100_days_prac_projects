morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}
decode_dict = {value: key for key, value in morse_dict.items()}
# print(decode_dict)

def code(user_input):
    end = ""
    for char in user_input:
        # print(char)
        for key, value in morse_dict.items():
            if char == key:
                end += morse_dict[char] + " "
    return end  # here return should be outside the for loop since return ends the function


# result = code(input("Enter the string :").upper())
# print(result)


def decode(user_input):
    end_1 = ""
    for char in user_input.split(" "):  # the string gets splitted by space and its converted to list
        for key, value in decode_dict.items():
            if char == key:
                end_1 += decode_dict[char]
    return end_1


# result1 = decode(input("Enter the string :"))
# print(result1)

start_translate = True
while start_translate:
    u_input = input("Do you want to encode or decode?")
    if u_input == "encode":
        print(code(input("Enter the string :").upper()))
        start_translate = False
    else :
        print(decode(input("Enter the code :")))
        start_translate = False