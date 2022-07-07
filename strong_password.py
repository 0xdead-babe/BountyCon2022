from pwn import *

import hashlib
import zlib
import math
import os
import time

length = 48

characters = string.printable[:94]
flag = 'BountyCon{'
#r = remote('localhost', 7878)

def send_password(i):
    password = i+ os.linesep
    r.sendlineafter('formula', password)
    r.recvuntil('!')
    r.recvline()
    r.recvline()
    
    return_length = r.recvline().decode().split('\n')[0]
    pass_length = hashlib.sha256(password.encode('utf-8')).digest()[0]
    calculated_length = (int(return_length) - pass_length ) // 150
    r.close()
    return (calculated_length)




for i in range(15):
    for i in characters:
        r = remote('ctf.bountycon.xyz', 3006)
        val = send_password(flag+i)
        if(abs(val) == 76):
            flag +=i
            print(flag)
            break
        else:
            continue


#print(flag)


#val = send_password(flag+'J')
#print(val <=68)
