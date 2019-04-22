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
9. To sign the hash instead of the message, run the command "hashing.py". This will, replace the message in the message.txt with the hash instead. Run the Sign script and you are good to go. To remove the hash, just edit the message.txt file again. Decrypting 
10. All the text files are in the parameters folder.
11. **I have used p instead of q and q instead of p. Just following the slides and not the question given in the pset. Please keep this in mind.**