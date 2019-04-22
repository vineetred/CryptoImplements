SBOX = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)
from pyfinite import ffield
F = ffield.FField(8)
fixed_Matrix = (
    [0x02,0x03,0x01,0x01],[0x01,0x02,0x03,0x01],[0x01,0x01,0x02,0x03],[0x03,0x01,0x01,0x02]
)
RC = [0x01000000, 0x02000000, 0x04000000,0x08000000,  #The round constants
0x10000000,0x20000000,0x40000000,0x80000000,0x1B000000,
0x36000000,0x6C000000,0xD8000000,0xAB000000,0x4D000000,0x9A000000]


W = []
keys = []

def wordBreak(word):
    words = []
    for i in range(0,4):
        words.append(word[i*8:(i+1)*(8)])
    return words

def getKeySchedule(key):

    sss = key
    for i in range(0,4):
        W.append(sss[i*8:(i+1)*(8)])

    j = 0
    k = 0
    for i in range(4,44):
        if (j%4==0):
            intermed = W[i-1][2::] + W[i-1][:2:]
            sub_W = SUBSTITUTE_BYTES(intermed)
            g_w = RC[k]^ int(sub_W,16)
            k+=1
            hello = int(W[i-4],16) ^ g_w
            hello = hex(hello)
            hello = hello[2:]
            W.append(hello)
            j+=1
            continue

        hello = int(W[i-1],16) ^ int(W[i-4],16)
        hello = hex(hello)
        hello = hello[2:]
        W.append(hello)
        j+=1

    
    key = ""
    for i in range(0,45):
        if(i%4==0 and i!=0):
            keys.append(key)
            key = ""
        key +=W[i]
    for key in keys:
        print(key)

    return keys

def encrypt(plaintext, key_schedule):
    #FIRST WE XOR THE PLAINTEXT WITH ROUND KEY:
    arrXOR = XOR(text,keys[0])
    finale = arrXOR
    for i in range(1,11):
        
        
        #WE THEN BREAK IT INTO 4 WORDS of a BYTE each
        # words = wordBreak(finale)
        #Subsituite step SBOX
        # subWords = ""
        # for word in words:
        #     subWords = subWords + SUBSTITUTE_BYTES(word)
        finale = columnHello(finale)
        subWords = SUBBING(finale)
        print("THIS IS SUBWORD: ",len(subWords))
        #WE do SHIFT ROWS NOW
        shifted_Rows = SHIFT_ROWS(subWords)
        #We add the round key now!
        finale = ADD_ROUND_KEY(shifted_Rows, keys[i])
        print("I= ",i)
        print("FINALE ",finale)
def XOR(var1,var2):
    result = str(int(var1,16) ^ int(var2,16))
    result = hex(int(result))[2:].zfill(32)
    # print("This is the XOR")
    return result
    # print(result)

# def columnBreak(test):
#     c = []
#     letters = []
#     c.append(test[0:2] + test[8:10] + test[16:18] + test[24:26])
#     c.append(test[2:4] + test[10:12] + test[18:20] + test[26:28])
#     c.append(test[4:6] + test[12:14] + test[20:22] + test[28:30])
#     c.append(test[6:8] + test[14:16] + test[22:24] + test[30:32])
#     final = c[0]+c[1]+c[2]+c[3]
#     return c

def columnHello(test):
    c = []
    letters = []
    k =0
    for j in range(0,4):
        for i in range(0,4):
            letters.append(test[(8*i)+k:(8*i)+2+k])
        k+=2
        c.append(letters)
        letters = []
    return c

def ADD_ROUND_KEY(state_array, key):
    res = []
    output = []
    key = columnHello(key)
    print(key)
    for i in range(0,4):
        for j in range(0,4):
            res.append(hex(int(state_array[i][j],16)^int(key[i][j],16))[2:].zfill(2))
    output.append(res)
    print("ARK")
    print(output)
    return output

            # print("hey")

def SUBBING(array):
    c = []
    letters = []
    for i in range(0,4):
        for j in range(0,4):
            p0 = hex(SBOX[int(array[i][j],16)])
            letters.append(p0)
            print(p0)
        c.append(p0)
    return c

def SUBSTITUTE_BYTES(state_array):
    p0 = str(hex(SBOX[int(state_array[0:2],16)]))
    if(len(p0)<4):
        p0 = p0[:2] + '0' + p0[2:]
    p1 = str(hex(SBOX[int(state_array[2:4],16)]))
    if(len(p1)<4):
        p1 = p1[:2] + '0' + p1[2:]
    p2 = str(hex(SBOX[int(state_array[4:6],16)]))
    if(len(p2)<4):
        p2 = p2[:2] + '0' + p2[2:]
    p3 = str(hex(SBOX[int(state_array[6:8],16)]))
    if(len(p3)<4):
        p3 = p3[:2] + '0' + p3[2:]
    state_array = p0[2:] + p1[2:] + p2[2:] + p3[2:]
    return state_array


def SHIFT_ROWS(state_array):

    column = columnHello(state_array)
    for i in range(0,4):
        column[i] = column[i][i::] + column[i][:i:]
    return column

key = "5468617473206D79204B756E67204675"

getKeySchedule(key)

text = "27153a16906ef425d078796f71569cbe"

encrypt(44,22)
# ADD_ROUND_KEY(world)
