#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

import random, string, os, math

seedfile = "/dev/urandom"

def get_random(bitcount):
    '''
    gen = random.SystemRandom()
    intcharset = string.digits
    outputstr = ''
    for x in range(bytecount):
        newdigit = gen.choice(intcharset)
        outputstr = outputstr + newdigit
    output = int(outputstr)
    '''
    #bytelist = os.urandom(bytecount)
    #bytestring = ''.join(random.choice)
    #bitint = map(ord, bytestring)
    cryptoGen = random.SystemRandom()
    randbits = cryptoGen.getrandbits(bitcount)
    #int.from_bytes(bytestring, byteorder='big', signed=False)
    return randbits

#on a [a,b)
def get_random_interval(minimum,maximum):
    if minimum > maximum:
        return get_random_interval(maximum,minimum)
    seed = get_random(1024)
    scaletop = maximum - minimum
    return minimum + ((seed  * scaletop / pow(2,1024)))

def jacobi(a, b):
    if (b % 2 == 0) or (b <= 0):
        return 0
    j = 1
    if (a < 0):
        a = -a
        if (b % 4) == 3:
            j = -j
    while (a != 0):
        while (a % 2) == 0:
            a = a/2
            if ((b % 8) == 3) or ((b % 8) == 5):
                j = -j
        temp = b
        b = a
        a = temp
        if ((a % 4) == 3) and ((b % 4) == 3):
            j = -j
        a = a % b

    if (b == 1):
        return j
    else:
        return 0

def solovay_strassen(n, k):
    if n % 2 == 0:
        return False
    half = (n-1)/2
    #print "Half: {}\n".format(half)
    for i in range(k):
        #print "Test #{}".format(i)
        a = get_random_interval(2,n-1)
        x = jacobi(a,n)
        #print "Jacobi: {}\n".format(x)
        if (x == 0):
            return False
        if pow(a,half,n) != x % n:
            return False
    return True

def generate_prime(bitcount):
    x = 0
    while (x < 3):
        x = get_random(bitcount)
    potentialprime = x
    if (potentialprime % 2 == 0):
        potentialprime -= 1
    while not (solovay_strassen(potentialprime, 100)):
        potentialprime += 2
    return potentialprime
#print "Prime: {}".format(generate_prime(6))
