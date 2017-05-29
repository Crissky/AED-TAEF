def base42encode(number, base=42):
    alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZΔΘΠΣΨΩ'

    if not isinstance(number, (int)):
        raise TypeError('Digite um numero inteiro, seu animal!!!')

    if not isinstance(base, (int)):
        raise TypeError('Base tem que ser um número inteiro.')
    if(base < 2 or base > len(alphabet)):
        raise ValueError('Base deve ter um valor entre 2 e %d'%(len(alphabet)))
    
    alphabet = alphabet[:base]
    
    value = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        value = alphabet[i] + value

    return sign + value


def base42decode(string, base=42):
    alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZΔΘΠΣΨΩ'

    if not isinstance(string, (str)):
        raise TypeError('Digite uma string, seu animal!!!')
    
    if not isinstance(base, (int)):
        raise TypeError('Base tem que ser um número inteiro.')
    if(base < 2 or base > len(alphabet)):
        raise ValueError('Base deve ter um valor entre 2 e %d'%(len(alphabet)))
    
    alphabet = alphabet[:base]
    string = string.upper()
    sign = ''
    value = 0
    
    if(string[0] == '-'):
        sign = '-'
        string = string[1:]

    for x in string:
        if(x not in alphabet):
            raise ValueError("'%s' não pertence a base %d"%(string, len(alphabet)))
    
    for x in range(len(string)):
        value = value*len(alphabet)+alphabet.index(string[x])

    return value if sign == '' else -value
