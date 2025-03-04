# Lab 10 - Blockchain

## Hashing
Hashing is a mathematical technique that is used to secure and verify data. Data cannot be returned to its original form once it has been hashed. The contents of hash_value.py can be seen below.

![hash_value.py](https://github.com/user-attachments/assets/1a6ea249-73ee-46e6-9fc2-1392dce1838b)

This file uses hashing with randomization, which adds an extra layer of security. After running this file twice, it can be seen that the more complex the form of data, the more it is affected by this process.

![hashing results](https://github.com/user-attachments/assets/220b0a7a-4dd1-430c-a415-38bcc92112a8)

## Blockchain

This example creates a simple blockchain using the file snakecoin.py.

![snakecoin.py](https://github.com/user-attachments/assets/2bef0a82-ab5f-4044-bbf0-bbeb9b1bfe18)

After running this file using ```python snakecoin.py``` it can be seen that 20 blocks are added onto the chain, all with unique hashes.

![snakecoin.py output](https://github.com/user-attachments/assets/370089ca-6e4b-48e4-b475-97b44ad0b628)

This approach to create a blockchain is then expanded on with the file, snakecoin-server-full-code.py. This file includes networking capabilities, allowing you to mine blocks from an internet connection.

![full code 1/2](https://github.com/user-attachments/assets/50ee29e3-1c6a-41dd-8755-b1191389ae57)
![full code 2/2](https://github.com/user-attachments/assets/1d852bb5-418b-486d-8435-05c45f474ca5)

After running this file, I opened another terminal and used the following commands to mine a block.
![image](https://github.com/user-attachments/assets/eab513aa-10a3-4ea7-91df-775985e78771)

After using these curl commands, the following image shows the output on the terminal running the blockchain server. The same requests made from the client are present on the server side.
![server side after mine](https://github.com/user-attachments/assets/15c2527c-d418-4a30-99f4-10a4265852d0)

Similarly, the transaction can also be found at 127.0.0.1:5000/mine.
![transaction on web side](https://github.com/user-attachments/assets/6d0ba481-4cb6-483f-9b44-5ba127120663)

---

I pledge my Honor I have abided by the Stevens Honor System - _Ray Ringston_
