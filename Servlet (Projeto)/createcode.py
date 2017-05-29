import secrets
import string

def createCode():
    alphabet = string.ascii_uppercase + string.digits
    code = ''
    for x in range(12):
        code += secrets.choice(alphabet)

    return code

if(__name__ == '__main__'):
    print(insertCode())
