#INFINITY POINT IS USED HERE AS [-1,-1]
import numpy as np
import math

def read_Parameters():
    global p,a,b,infinity
    file = open("variables.txt", 'r')
    contents = file.read().split(" ")
    file.close()
    p = int(contents[0])
    a = int(contents[1])
    b = int(contents[2])
    infinity = [-1,-1]

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

def bits(n):
    while n:
        yield n & 1
        n >>= 1

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

def read_Point():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    return [x,y]

def write_Point_terminal(point):
    print(point)

def addition(arg1,arg2):
    if(arg1==[-1,-1] and arg2==[-1,-1]): #This is the infinity added to infinity
        return arg1
    '''
    This next construct is for when a point is added to the point
    at infinity
    '''
    if(arg1==[-1,-1]):
        return arg2
    if(arg2==[-1,-1]):
        return arg1
    '''
    Same X coordinate
    '''
    if(arg1[0]==arg2[0]):
        return infinity

    if(arg1[0]!=arg2[0]):
        inverse = inv((arg2[0]-arg1[0]),p)
        slope = ((arg2[1]-arg1[1])*inverse)%p   
        x_r = (pow(slope,2) - arg1[0] - arg2[0])%p
        y_r = (slope*(arg1[0]-x_r) - arg1[1])%p
        return [x_r,y_r]

def pointDoubling(arg1):
    inverse = inv(2*arg1[1],p)
    slope = (3*pow(arg1[0],2)+a)*inverse
    x_r = (pow(slope,2)-(2*arg1[0]))%p
    y_r = (slope*(arg1[0]-x_r)-arg1[1])%p
    return [x_r,y_r]

def multiplePoint(N,times):
    Q = [-1,-1]
    d = []
    for bit in bits(times):
        d.append(bit)
    for i in range(0,len(d)):
        if(d[i]==1):
            Q = addition(Q,N)
        N = pointDoubling(N)
    return Q

def negationPoint(point):
    return [point[0],(-point[1])%p]

def subtractionPoint(point1,point2):
    return addition(point1,negationPoint(point2))

def EC_Check(point): #function to check if given co-ordinates are part of EC or not
    x,y = point
    if(x>p or x<0 or y>p or y<0):
        return False
    flag = ((y**2 - (x**3 + a*x + b)))%p==0
    return flag

def functionCheck(xcord):
    y2 = (xcord**3 + a*xcord + b)%p
    y = math.sqrt(y2)
    return int(y)

def write_to_File(variable):
    file = open("output.txt", 'w')
    file.write(str(variable))
    file.close()

def find_Y(point):
    global p,a,b
    a,u = (pow(point,3) + a*point + b),0
    condition = exponent(a, int((p-1)/2), p)
    if (condition == 1): #Eulers criterion to check if point is a quadratic residue of p
        
        flag = True
        
        while (flag == True):
            u = u + 1
            if (exponent(u, int((p-1)/2), p) != 1):
                flag = False 
        s,variable = 0,p-1
        while ((variable % 2) == 0):
            s = s + 1
            variable = (variable/2)

        t,k = variable,s
        z = exponent(u, int(t), p)
        point = exponent(a, int((t+1)/2), p)
        b = exponent(a, int(t), p)
        while (b != 1 % p):
            m = 1
            variable = pow(b,pow(2,m))
            while ((variable - 1) % p != 0):
                m +=1

            y = exponent(2, (k-m-1), p)
            z = exponent(y,2,p)
            b = b*z % p
            point = point*y % p
            k = m
        return point
    elif(condition==0):
        return 0
    else :
        raise Exception ("Y does not exist for given x =",point)

#################################################################
# FORMAT FOR THE POINTS = [x,y]
# Always pass a list unless specified
# Only find_Y() takes a single integer as a paramter
# Can be converted to string by just placing the points in str([x,y])
#################################################################

#Question (a)
# <-- THIS MUST BE DONE BEFORE DOING ANYTHING ELSE -->
# print("Reading parameters of the EC")
read_Parameters()

#Question (b)
# Return value must be stored to be used later
print("Points input")
points = read_Point()

#Question (c)
#Printing the above read points
print("Writing points")
write_Point_terminal(points)

#Question (d)
print("Addition")
#Case 1 - Adding Inf point to itself. Expected result = [-1,-1]
print(addition([-1,-1],[-1,-1]))

#Case 2 - Adding P to Inf Point. Expected result = P which is [4,14]
print(addition([4,14],[-1,-1]))

#Case 3 - Add two points with same x coordinates but different y coordinates
#Expected result = Infinity point
print(addition([8,2],[8,57]))

#Case 4 - Add with two different points
# Adding 4,14 and 8,2. Expected results for p a b = 59 17 5 is [56,24]
print(addition([4,14],[8,2]))

#Case 5 - Point doubling
#Let's double point [4,14]. 2P = 8,2
print(pointDoubling([4,14]))

#Question (e)
# Negate a point
print("Point negation")
print(negationPoint([8,2]))

#Question (f)
#Subtracting 4,14 from 8,2. If P = 4,14 then 2P = 8,2. So, 2P - P = P (4,14)
print("Point subtraction")
print(subtractionPoint([8,2],[4,14]))

#Question (g)
#Let's multiply the point [4,14]. 7*P = 15,53
print("Point scalar multiplication")
print(multiplePoint([4,14],7))

#Question (h)
#Shanks Algorithm. For a given X, return Y. Expected answer is either 2 or 57 for given X = 8
print("Shanks algorithm")
print(find_Y(8))
