from random import randrange, getrandbits, random
import math
import binascii

def exponent(num,e,n):
    if((e&1)==1):
        remainder = num%n
    else:
        remainder = 1
    e //=2

    while(e>0):
        num = (num*num) % n
        if((e&1)==1):
            remainder = (remainder*num)%n
        e//=2
    return remainder

def ext_GCD(arg1, arg2):
    prevRemain, remainder = abs(arg1), abs(arg2)
    x, oldX, y, oldY = 0, 1, 1, 0
    while remainder:
        prevRemain, (quotient, remainder) = remainder, divmod(prevRemain, remainder)
        x, oldX = oldX - quotient*x, x
        y, oldY = oldY - quotient*y, y
    return prevRemain, oldX * (-1 if arg1 < 0 else 1), oldY * (-1 if arg2 < 0 else 1)

def inv(e, phi):
    g, x, y = ext_GCD(e, phi)
    if (g != 1):
	    raise Exception("No modular inverse exists")
    posans = (x%phi)
    return posans



file = open("Parameters/public_key.txt", 'r')
global p,g,h,r,signature
p = int(file.readline())
g = int(file.readline())
h = int(file.readline())
file.close()
file = open("Parameters/q_val.txt", 'r')
q = int(file.readline())
file.close()

z = randrange(2,(q-1))

r = exponent(g,z,p)
r = (r*h)%p

signature = (-r)%q
message = (z*signature)%q

file = open("Parameters/forged_signature.txt", 'w')
file.write(str(r) + "\n")
file.write(str(signature))
file.close()
file = open("Parameters/message.txt", 'w')
file.write(str(message) + "\n")