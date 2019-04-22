from collections import deque

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





# hello = columnBreak("7750f228896eb4561b9cd67497aad0b1")
# print(hello)
# hello = SHIFT_ROWS(hello)
# print(hello)

# def XOR(var1,var2):
#     result = str(int(var1,16) ^ int(var2,16))
#     result = hex(int(result))[2:].zfill(32)
#     return result
# text = "54776F204F6E65204E696E652054776F"
# key = "5468617473206D79204B756E67204675"
# hello = XOR(text,key)
# print(hello)
# keys = []
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


key1 = "7750f228896eb4561b9cd67497aad0b1"

master = getKeySchedule(key1)
# print(master)
print(len(master))
# print(keys[4])
# print(keys)

# hello = byte2array(bytes.fromhex(key1))