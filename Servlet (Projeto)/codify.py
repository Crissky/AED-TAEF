from hashlib import md5

def codify(string):
    value = 0
    code = md5()
    string = str(string)

    for x in range(len(string)):
        value += (ord(string[x])**ord(string[x]))*((x+711)**len(string))
    
    code.update(str.encode(str(value)))
    
    return code.hexdigest()
