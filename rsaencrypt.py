import random
import primegen

def array_to_int(array, maxval):
    b = len(array)
    m = 0
    for i in range(0,b):
        m += array[i] * pow(maxval,b-1-i)
    return m

def pad(text):
    u = unicode(text, 'utf-8')
    bArray = map(ord,u)
    rArray = []
    for _ in range(16):
        rArray.append(int(primegen.get_random_interval(0,256)))
    return rArray + bArray

def unpad(tArray):
    return tArray[16:]

def int_to_array(iInt,maxval):
    output = []
    while iInt > 0:
        output.append(iInt%maxval)
        iInt = iInt / maxval
    return output[::-1]

def test_arrayops(text):
    padded = pad(text)
    inted = array_to_int(padded,256)
    uninted = int_to_array(inted,256)
    newtext = map(unichr, uninted)
    print text
    print padded
    print inted
    print uninted
    print newtext

def encipher(text, publicKey):
    (n, e) = publicKey
    tArray = pad(text)
    tInt = array_to_int(tArray, 256)
    ciphertext = pow(tInt, e, n)
    return ciphertext

def decipher(c, privateKey):
    (n, d) = privateKey
    inverted = pow(c,d,n)
    tArray = unpad(int_to_array(inverted,256))
    message = map(unichr,tArray)
    return ("".join(message))

#print array_to_int(pad("eee"),256)
#print text_to_int("hello my name is bob")
