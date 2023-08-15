import random
import time
import string
from ecc import mul, add, valid
from extended_euclid import m_inv

valid_points = [(2, 6), (4, 19), (8, 10), (13, 23), (16, 2), (19, 16), (27, 2),
                (0, 7), (2, 23), (5, 7), (8, 19), (14, 6), (16, 27), (20, 3), (27, 27),
                (0, 22), (3, 1), (5, 22), (10, 4), (14, 23), (17, 10), (20, 26),
                (1, 5), (3, 28), (6, 12), (10, 25), (15, 2), (17, 19), (24, 7),
                (1, 24), (4, 10), (6, 17), (13, 6), (15, 27), (19, 13), (24, 22)]

n = 37

def private():                      # 비공개키 생성 코드
    k = random.randint(0, 100000)
    return k

def public(k, s):                   # 공개키 생성 코드
    q = mul(k, s)
    return q

def randstring():                   # 8자리 랜덤 문자열 뽑는 코드
    a = ""
    for i in range(8):
        a += random.choice(string.ascii_letters)
    return a
sum1 = 0
def encrypt():
    a=[]
    S = random.sample(valid_points, 1)
    fstring = randstring()
    prik = private()
    pubk = public(prik, S[0])
    start = time.time()
    sstring = int(hash(fstring))
    end = time.time()
    b = end-start
    a.append(fstring)
    a.append(prik)
    a.append(pubk)
    a.append(sstring)
    a.append(b)
    return a

timer=0
start = time.time()
for a in range(100000):
    start = time.time()
    i = encrypt()
    end = time.time()
    timer += end-start
    sum1 += i[4]
    print(i, a)
print(round(timer/10000, 6), round(sum1/10000, 6))