# Aghilas AZZOUG 
# Binary
# 8 November 2019
# for Graphs functions but not used in my interface (sorry mr Sonntag ;) )

BINARY_CODE_DICT = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    '10':'1010',
    '11':'1011',
    '12':'1100',
    '13':'1101',
    '14':'1110',
    '15':'1111',
}


def encryptor(text):
    encrypted_text = ""
    for letters in text:
        if letters != " ":
            encrypted_text = encrypted_text + BINARY_CODE_DICT.get(letters) + " "
        else:
            encrypted_text += " "
    print(encrypted_text)


def decryptor(text):
    text += " "
    key_list = list(BINARY_CODE_DICT.keys())
    val_list = list(BINARY_CODE_DICT.values())
    binary = ""
    normal = ""
    for letters in text:
        if letters != " ":
            binary += letters
            space_found = 0
        else:
            space_found += 1
            if space_found == 2:
                normal += " "
            else:
                normal = normal + key_list[val_list.index(binary)]
                binary = ""
    print(normal)


print("\n\n\n\t\tBinary Code Generator")
ch = input("Press N To Encrypt Or B To Decrypt : ")
if ch == 'N' or ch == 'B':
    text_to_encrypt = input("Enter Some Numbers To Encrypt : ").upper()
    encryptor(text_to_encrypt)
else:
    text_to_decrypt = input("Enter Binary code to Decrypt : ")
    decryptor(text_to_decrypt)
