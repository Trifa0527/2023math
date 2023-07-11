import random

def gcd(himdlda, helloitsme):       # 최대공약수를 구하는 코드
    while helloitsme != 0:
        himdlda, helloitsme = helloitsme, himdlda % helloitsme
    return himdlda

def prime(suckone_no_hair):         # 소수를 판별하는 코드
    for i in range(2, suckone_no_hair):
        if suckone_no_hair % i == 0:
            return 0
    return 1
