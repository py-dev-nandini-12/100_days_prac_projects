strings_for_input = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                     "S", "T", "U", "V", "W", "X", "Y", "Z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ".", ",", "?",
                     "'", "!", "/", "(", ")", "&", ":", ";", "=", "+", "-", "_", "''", "$", "@", " "]

morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
               "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
               "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", ".-.-.-",
               "--..--", "..--..", ".----.", "-.-.--", "-..-.", "-.--.", "-.--.-", ".-...", "---...",
               "-.-.-.", "-...-", ".-.-.", "-....-", "..--.-", ".-..-.", "...-..-", ".--.-",
               "/"]


# print(len(strings_for_input))
# print(len(morse_codes))

def code(user_input):
    end = ""
    # count = 0
    # while count != len(user_input):
    for char in user_input:
        # print(char)
        if char in strings_for_input:
            # count += 1
            position = strings_for_input.index(char)  # here .index gives the index starts counting from 0
            # print(position)
            output = morse_codes[position]
            end += output + " "
    return end  # here return should be outside the for loop since return ends the function


# result = code(input("Enter the string :").upper())
# print(result)


def decrypt(message):
    end_r = ""
    # count = 0
    # while count != len(message):
    for char in message.split(" "):  # Split a string into a list where each word is a list item
        # print(char)
        if char in morse_codes:
            # count += 1
            position = morse_codes.index(char)
            output1 = strings_for_input[position]
            end_r += output1
    return end_r


# result2 = decrypt(input("Enter the code :"))
# print(result2)

start_translate = True
while start_translate:
    u_input = input("Do you want to encode or decode?")
    if u_input == "encode":
        print(code(input("Enter the string :").upper()))
        start_translate = False
    else :
        print(decrypt(input("Enter the code :")))
        start_translate = False


