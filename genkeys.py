import primegen

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

def mod_inverse(x, y):
    s = 0
    t = 1
    old_s = 1
    old_t = 0
    r = y
    old_r = x
    while (r != 0):
        quotient = old_r / r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)
    return (x + old_t)

def generateKeysFromPrimes(p,q):
    n = p * q #the modulus
    m = n - (p + q - 1) #private
    e = 3 #must be coprime with m
    while True:
        if gcd(m,e) == 1:
            break
        else:
            e += 2
    d = mod_inverse(m,e)

    publicKey = (n,e)
    privateKey = (n,d)

    return (publicKey, privateKey)

def generateKeys():
    p = primegen.generate_prime(1024)
    q = primegen.generate_prime(1024)
    return generateKeysFromPrimes(p,q)
