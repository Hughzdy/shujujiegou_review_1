# 作者：Hugh
# 创建日期；2023/2/8
import random


def maopao_paixu(li):
    for i in range (len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j]<li[j + 1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        if not exchange:
            return None

li = list(range(10))
random.shuffle(li)
maopao_paixu(li)
print(li)