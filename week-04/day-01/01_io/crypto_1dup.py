# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    result = ""
    for i in range(0, len(text)-1):
        if i%2 is 0:
            result += text[i]
        elif i%2 is not 0 and text[i] == "\n":
            result += text[i]
    result += "\n"
    f.close()
    return result
