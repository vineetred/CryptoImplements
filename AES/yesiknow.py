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
def byte2array(bytes):
    """Converts bytes to 4 x 4 array
    :param bytes: bytes
    :return: 4 x 4 array
    """
    array = []
    for i, byte in enumerate(bytes):
        if i % 4 == 0:
            array.append([byte])
        else:
            array[i // 4].append(byte)
    return array

def array2hex(array):
    """Converts 4 x 4 array to hex string
    :param array: array
    :return: hex string
    """
    hexstr = ""
    for i in range(4):
        hexstr += ''.join('{:02x}'.format(x) for x in array[i])
    return hexstr

def getKeySchedule(key):
    W = []
    # key = "7750f228896eb4561b9cd67497aad0b1"
    # key = columnBreak(key)
    keys = byte2array(bytes.fromhex(key))
    
    for j in range(4,44):
        x0 = keys[j-4][0]
        x1 = keys[j-4][1]
        x2 = keys[j-4][2]
        x3 = keys[j-4][3]
        fren = [x3,x0,x1,x2]
        keys.append(fren)     
    return keys

def SHIFT_ROWS(state_array):
    column = state_array
    for i in range(0,4):
        middleMan = deque(column[i])
        middleMan.rotate(-i)
        column[i] = list(middleMan)
    return column

def columnBreak(test):
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

def SUBBING(array):
    c = []
    letters = []
    for i in range(0,4):
        for j in range(0,4):
            p0 = hex(SBOX[int(array[i][j],16)])[2:].zfill(2)
            letters.append(p0)
            # print(p0)
        # print(letters)
        c.append(letters)
        letters = []
    return c

def SUBSTITUTE_BYTES(state_array):
    subs = []
    for k in range(0,4):
        s0 = SBOX[state_array[k][0]]
        s1 = SBOX[state_array[k][1]]
        s2 = SBOX[state_array[k][2]]
        s3 = SBOX[state_array[k][3]]
        medium = [s0,s1,s2,s3]
        # print("INSIDE")
        # print(medium)
        subs.append(medium)
    return subs

def XOR(var1,var2):
    output = []
    output.append(var1[0]^var2[0])
    output.append(var1[1]^var2[1])
    output.append(var1[2]^var2[2])
    output.append(var1[3]^var2[3])
    return output

def transpose(array):
    for i in range(0,4):
        for j in range(0,4):
            matrix[j][i] = array[i][j]
    return matrix

def AddRoundKey(inp,index):
    ark = []
    for l in range(0,4):
        k0 = inp[l][0]^finalKeys[index][0]
        k1 = inp[l][1]^finalKeys[index][1]
        k2 = inp[l][2]^finalKeys[index][2]
        k3 = inp[l][3]^finalKeys[index][3]
        index+=1
        franco = [k0,k1,k2,k3]
        ark.append(franco)
    return ark


def encrypt(text,key):

    global finalKeys
    finalKeys = getKeySchedule(key)
    
    #Conversion to bytes
    text = byte2array(bytes.fromhex(text))
    #ROUND0 ARK
    input = []
    for i in range(0,4):
        input.append(XOR(text[i],finalKeys[i]))

    #BEGIN 9 more ROUNDS
    count = 4
    for z in range(0,10):
        #FIRST TRANSPOSE
        input = transpose(input)
        # print(input)
        #THEN WE SUBSIT
        input = SUBSTITUTE_BYTES(input)
        # print(input)

        #SHIFT ROWS!
        input = SHIFT_ROWS(input)
        # print(input)

        #WE TRANPOSE AGAIN!
        input = transpose(input)

        #Adding the round Key
        input = AddRoundKey(input,count)
        count+=4
    print(array2hex(input))
key = "7750f228896eb4561b9cd67497aad0b1"
plaintext = ["27153a16906ef425d078796f71569cbe",
             "b6f2d9b55d607b9a3e23cb4b9e133a18",
             "1a9d31f65a985ae9dfb6344cc90ec75b",
             "4e90a7cd0d8bce7285161377f0fd6fca"]
for text in plaintext:
    encrypt(text,key)