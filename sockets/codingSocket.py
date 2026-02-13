import sys

def byteorder():
    return sys.byteorder
    
def standard_encoding():
    return sys.getdefaultencoding()

def standardausgabe_encoding():
    return sys.stdout.encoding

def string2bytes(text):
    return bytes(text, "utf8")

def bytes2string(bytes):
    return str(bytes, "utf8")