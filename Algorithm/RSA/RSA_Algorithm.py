import random
import time
import string
import datetime

def gcd(himdlda, helloitsme):       # 최대공약수를 구하는 코드
    while helloitsme != 0:
        himdlda, helloitsme = helloitsme, himdlda % helloitsme
    return himdlda

def prime(suckone_no_hair):         # 소수를 판별하는 코드
    for i in range(2, suckone_no_hair):
        if suckone_no_hair % i == 0:
            return 0
    return 1
    
def twoprimes():                    # 2개의 소수 뽑는 코드
    while True:
        a = random.randrange(750, 1000)
        if prime(a):
            b = random.randrange(750, 1000)
            if prime(b):
                return [a, b]
            
def randstring():                   # 8자리 랜덤 문자열 뽑는 코드
    result = ""
    for i in range(8):
        result += random.choice(string.ascii_letters)
    return result

def keygen():                       # 공개, 비밀키 생성에 필요한 시드 생성 코드
    seed = twoprimes()
    p = seed[0]
    q = seed[1]
    n = p * q
    m = (p - 1) * (q - 1)
    return {'n': n, 'm' : m}

def public(m):                      # 공개키 생성 코드
    e = 2
    while e < m and gcd(e, m) != 1:
        e += 1
    return e

def private(m):                     # 비밀키 생성 코드
    d = 1
    while (public(m) * d) % m != 1 or d == public(m):
        d += 1
    return d

#-------------------------------------------------------------

def encrypt():                      # 암호화 코드
    data = [""]
    begin = time.time()
    key = keygen()
    end = time.time()
    data.append(round(end - begin, 6))      # 키 생성
#-------------------------------------------------------------
    ori = (randstring())
    oris = list(ori)
    orior = []
    eori = []
#-------------------------------------------------------------
    begin1 = time.time()
    d = private(key['m'])
    end1 = time.time()
    data.append(round(end1 - begin1, 6))      # 개인키 생성
#-------------------------------------------------------------
    etext = ""
    begin2 = time.time()
    for orisc in range(0, len(oris)):
        orior.append(ord(oris[orisc]))
    for oriorc in range(0, len(orior)):
        eori.append(((orior[oriorc]**public(key['m']))%key['n']))
    for eoric in range(0, len(eori)):
        etext += (str(eori[eoric]))
    end2 = time.time()
    data.append(round(end2 - begin2, 6))      # 암호화

#-------------------------------------------------------------
    data[0] += "평서문 : " + ori + "\n"
    data[0] += "암호문(NUMBER) : {}".format(eori) + "\n"
    data[0] += "암호문(ASCII) : {}".format(etext) + "\n"
    data[0] += "N : {}".format(key['n']) + "\n"
    data[0] += "공개키 : {}".format(public(key['m'])) + "\n"
    data[0] += "개인키 : {}".format(d) + "\n"

    return data

def decrypt():                      # 복호화 코드
    data = ""
    # eori = etext

    # eoris = list(eori)
    # eroiso = []
    # eroisor = []
    # eroar = []
    # text = ""
    # for eorisc in range(0, len(eoris)):
    #     eroiso.append(ord(eoris[eorisc]))
    # for eroisoc in range(0, len(eroiso)):
    #     eroisor.append((eroiso[eroisoc]**d)%n)
    # for eroisorc in range(0, len(eroisor)):
    #     eroar.append(str(eroisor[eroisorc]))
    # for eroarc in range(0, len(eroar)):
    #     text += eroar[eroarc]
#-------------------------------------------------------------

def main(count):                    # 테스트 진행 코드
    f = open("/Users/yys/Basic/Coding/math/2023math/Algorithm/RSA/result.txt", 'w')
    sum = 0.0
    fsum = 0.0
    ssum = 0.0
    tsum = 0.0
    f.close()
    for i in range(count):
        f = open("/Users/yys/Basic/Coding/math/2023math/Algorithm/RSA/result.txt", 'a')
        a = encrypt()
        timer = round(a[1]+a[2]+a[3], 6)
        f.write(str(a[1])+ " " + str(a[2]) + " " + format(a[3], 'f') + " " + str(timer))
        if a == 0:
            f.write(' error\n')
        else:
            f.write('\n')
        fsum += a[1]                                # 키 생성
        ssum += a[2]                                # 비밀키 생성
        tsum += a[3]                                # 암호화 진행
        sum += timer                                # 총 시간
        print(i+1)
        print(a[0])
        f.close()
    f = open("/Users/yys/Basic/Coding/math/2023math/Algorithm/RSA/result.txt", 'a')
    f.write("\navg : " + str(round(fsum/count, 6))+ " " + str(round(ssum/count, 6)) + " " + format(round(tsum/count, 6), 'f')+ " " + str(round(sum/count, 6)))
    f.write("\n\nrepeated " + str(count) + ' time' + "\n")
    f.close()

main(10000)
# def test(max):
#     i = 0
#     begin = time.time()
#     while True:
#         a = random.randrange(1, max)
#         if prime(a) == 1:
#             while True:
#                 b = random.randrange(1, max)
#                 if prime(b) == 1:
#                     i += 1
#                     break
#         if i == 10:
#             break
#     end = time.time()
#     return round(end - begin, 6)
# filename = input("File name : ")
# max = input("count : ")1
# if filename == "" or None:
#     filename = max
# f = open("/Users/yys/Basic/Coding/math/2023math/Algorithm/RSA/"+str(filename)+".txt", 'w')
# f.write(str(max)+"\n\n")
# for i in range(1, 101):
#     f.write(str(i)+":"+str(test(int(max)))+"\n")
#     print(i)
# f.close
