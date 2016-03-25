import sys
import genkeys, primegen, rsaencrypt

def runEncryption():
    keyHandle = open(keyfile,"r")
    keytext = keyHandle.read()
    keyHandle.close()
    if len(keytext) == 0:
        sys.stderr.write("ERROR: No key given. Please generate keys. You could use generatekeys.py\n")
    else:
        keyLines = keytext.split('\n')
        key = (long(keyLines[0]),long(keyLines[1]))

    if keyword == "-d":
        print "We will be decrypting {}".format(messagefile)
        f = open(messagefile,"r")
        ciphertext = long(f.read())
        f.close()
        message = rsaencrypt.decipher(ciphertext, key)
        print message
        return

    if keyword == "-e":
        print "We will be encrypting {}".format(messagefile)
        f = open(messagefile,"r")
        message = f.read()
        f.close()
        ciphertext = rsaencrypt.encipher(message,key)
        print ciphertext
        return

    else:
        sys.stderr.write("USAGE: rsa [textfile] [-d or -e] [key] [targetfile]\n")

progname, messagefile, keyword, keyfile = sys.argv
runEncryption()
