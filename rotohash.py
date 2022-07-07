from pwn import *
from hashlib import md5
import time

length = -abs(31)
characters = string.printable[:94]
c = 31
valid_chars = []

def send_flag(i):
    time.sleep(30)
    r.sendlineafter('? ', str(i))
    returned_hash = r.recvline().decode('utf-8').strip('\n')
    r.close()
    return returned_hash

def shift_characters():
    pass


for i in range(32):
    r = remote("ctf.bountycon.xyz", 3016)
    returned_hash = send_flag(length)
    for x in characters:
        test_flag = x + ''.join(valid_chars)[::-1] + '$' * c
        #print(test_flag)
        #print(md5(test_flag.encode('utf-8')).hexdigest())
        if(returned_hash == md5(test_flag.encode('utf-8')).hexdigest()):
                valid_chars.append(x)
                print(test_flag)
                c -= 1
                length += 1

        else:
            continue





#print(send_flag(length))


















