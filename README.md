# Cryptographic Implementations

## RSA 
1. Language = Python 3.6.4
2. To run the program, we have to first generate our public and private keys. To do this, just run the command
"python3 keygen.py".
3. After this, two text files would have been created, public_key and private_key. These contain your keys.
4. The plaintext text file contains the text that needs to be encrypted. Edit this to whatever you like. 
5. To encrypt, just run the command "python3 encrypt.py".
6. To decrypt, run the command "python3 decrypt.py".
7. Make sure the number of bits of the message is smaller than 1024.
8. The decrypted text can be found in the terminal as well as in the file called decryptedtext.txt

## ElGamal
1. Language = Python 3.6.4
2. To run the program, we have to first generate our public and private keys. To do this, just run the command
"python3 keygen.py".
3. After this, two text files would have been created, public_key and private_key. These contain your keys.
4. The plaintext text file contains the text that needs to be encrypted. Edit this to whatever you like. 
5. To encrypt, just run the command "python3 encrypt.py".
6. To decrypt, run the command "python3 decrypt.py".
7. Make sure the number of bits of the message is smaller than 1024.
8. The decrypted text can be found in the terminal as well as in the file called decryptedtext.txt

## RSA Factoring
1. Language = Python 3.6.4
2. Change the values of e, d and n in the file, misc/factoring.py
3. Run the command, "python3 factoring.py"

## Elliptical Curves
1. Language = Python 3.6.4
2. To run the program, one needs to run the command "python3 ec.py".
3. After this, all the placeholder commands inside the program testing out every operation and function will run.
4. The format of the points is as follows - [x,y]. The arguments need to passed into this format for the program to run properly.
5. The EC Domain parameters will be found in the file called 'variables.txt'. Changes to the curve must be made here.
6. The outputs will be saved in the file named 'output.txt'.
7. The details of every function can be found commented throughout the script and below

### Function definitions
* **read_Parameters()** - Reads the parameters from the variables.txt file
* **read_Point()** - Reads the points from user input through the terminal
* **write_Point_terminal()** - Prints given points onto the terminal
* **addition()** - Adds two points. Accepted format of points is [x1,y1],[x2,y2]
* **pointDoubing()** - Doubles the given point. Accepted format of points is [x,y]
* **negationPoint()** - Returns the negation of a given point
* **subtractionPoint()** - Returns the different between two points.
* **mutliplePoint()** - Returns the scalar multiplitcation of a point, P. Accepted format of points is [x,y],k.
* **find_Y()** - Returns either y or an exception. Accepted format of points is (x).



## ElGamal Signature Scheme
1. Language = Python 3.6.4
2. To run the program, we have to first generate our public and private keys. To do this, just run the command
"python3 keygen.py".
3. After this, two text files would have been created, public_key and private_key. These contain your keys. Another file is the text file containing the value of q.
4. The message text file contains the text that needs to be signed. Edit this to whatever you like. 
5. To sign,  run the command "python3 Sign.py". This will create a text file, signature.txt containing r and s.
6. To decrypt and verify, run the command "python3 Decrypt.py".
7. Make sure the number of bits of the message is smaller than 1024.
8. To run the existentital forgery demo, run the command "python3 forgery.py". This will generate a forged signature and message. Before running the decrypt script, comment out the readKeys and readMessage functions and uncomment the forged function.
9. To sign the hash instead of the message, run the command "hashing.py". This will, replace the message in the message.txt with the hash instead. Run the Sign script and you are good to go. To remove the hash, just edit the message.txt file again. 
10. All the text files are in the parameters folder.


## AES
Barely works. I suggest you not use my implementation. Not the best idea.
## References for code
1. Dhruv Agarwal, Vidur Singh, TS Harikrishnan, Preetha Datta and Debayan Gupta - Code References
2. https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
3. https://rosettacode.org/wiki/RSA_code
4. https://gist.github.com/JonCooperWorks/5314103 - A medium blog post repo
5. https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test - Miller Rabin
6. https://rosettacode.org/wiki/Modular_inverse Modular Inverse using extended Euclidean algorithm
