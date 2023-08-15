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
for a in range(10000):
    start = time.time()
    i = encrypt()
    end = time.time()
    timer += end-start
    sum1 += i[4]
    print(i, a)
print(round(timer/10000, 6), round(sum1/10000, 6))



# class Person:
#     __name = ''
#     __d = private_key_gnt()
#     __k = private_key_gnt()
#     __G = -1, -1
#     __Q_self = -1, -1               # 공개키

#     __r = 0
#     __s = 0
#     __e = 0

#     def __init__(self, name, G):
#         self.name = name
#         self.__G = G
#         self.__Q_self = public_key_gnt(self.__d, self.__G)

#     def get_public_key(self):
#         return self.__Q_self

#     def get_r(self):
#         while self.__r == 0:
#             x, y = public_key_gnt(self.__k,self.__G)
#             self.__r = x % n

#         return self.__r

#     # 메세지를 해쉬함수로 돌려서 해쉬값을 저장한다
#     def hash_msg(self, m):
#         self.__e = int(hash(m))

#     # s를 계산하고 반환한다
#     def get_s(self):
#         while self.__s == 0:
#             self.__s = (m_inv(self.__k, n) * (self.__e + (self.__d * self.__r))) % n

#         return self.__s


# ECDSA(Elliptic Curve Digital Signature Algorithm) main 함수
# if __name__ == "__main__":
#     # 공유할 점 G생성
#     S = random.sample(valid_points, 1)
#     G = S[0]

#     if not valid(G):
#         print("이 점은 타원 곡선에 없는 점입니다.")


#     # Alice의 이름과 점G를 초기화
#     alice = Person("Alice", G)

#     # 메세지 입력
#     m = input("메세지를 입력하세요 : ")

#     # 메세지 hash
#     alice.hash_msg(m)

#     # Alice의 public key, r, s 생성 및 반환
#     Q = alice.get_public_key()
#     r = alice.get_r()
#     s = alice.get_s()

#     # 조건 확인 조건에 맞지 않으면 Reject
#     if 1 <= r <= (n-1) and 1 <= s <= (n-1):
#         # 메시지 hash
#         e = int(hash(m))
#         # w, u1, u2, X 계산
#         w = m_inv(s, n) % n
#         u1 = (e * w) % n
#         u2 = (r * w) % n
#         X = add(mul(u1, G), mul(u2, Q))

#         # X가 INF면 Reject
#         if X == (-1, -1):
#             print("Reject Signature")
#         else:
#             # v 계산
#             x1, y2 = X
#             v = x1 % n
#             # r이 v와 같으면 Accept
#             if r == v:
#                 print("Accept Signature")
#             else:
#                 print("Reject Signature")
#     else:
#         print("Reject Signature")