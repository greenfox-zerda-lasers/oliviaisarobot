# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    result = ""
    for line in range(len(text)-1, -1, -1):
        result += text[line]
    return result
    f.close()
