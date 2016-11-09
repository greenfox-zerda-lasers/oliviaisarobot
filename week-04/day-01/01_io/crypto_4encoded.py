# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.read()
    result = ""
    abc = "abcdefghijklmnopqrstuvwxyz"
    exc = "\n , "
    for a in text:
        if a not in exc:
            result += chr(ord(a) - 1)
        else:
            result += a
    f.close()
    return result
