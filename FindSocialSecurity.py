#This program seaches for a social security number within a string

def isSocialSecurity(text):

    if len(text) != 11:
        return False

    elif text[3] != "-" or text[6] != "-":
        return False

    for i in range(0, 9):
        if text[i] == "-":
            text = text.replace(text[i], '')

    return text.isdigit()

def searchNumber(message):
    message_chunk = ""
    numbers_found = []
    for i in range(len(message)):
        message_chunk = message[i:i+11]
        if isSocialSecurity(message_chunk):
            numbers_found.append(message_chunk)

    return numbers_found

message = "John Doe's SSN is 123-45-6789. Jane's is 000-00-0000. Bill's is 333-33-3333"
print("SSN's: ",searchNumber(message))