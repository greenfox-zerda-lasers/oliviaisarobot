# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    result = ""
    for a in text:
        result += a[-2::-1] + "\n"
    f.close()
    return result
