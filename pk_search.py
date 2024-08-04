from bitcoin import *
import random

a = int (input("start scan range:"))
b = int (input("endof scan range:"))
c = input ("address:")

while True:
    ran = random.randrange(a,b)
    myhex = "%064x" % ran
    myhex = myhex[:64]
    priv = myhex
    pub = privtopub(priv)
    pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
    addr = pubtoaddr(pubkey1)
    n = addr
    if n.strip() == c:
        print ("found!!", addr, myhex)
        s1 = myhex
        s2 = addr

        f=open(u"results_101.txt","a")
        f.write(s1)
        f.write(s2)
        f.close()
        break
    else:
        print ("searching...",addr,myhex)
