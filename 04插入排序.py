# 作者：Hugh
# 创建日期；2023/2/8
import random


def charu_paixu(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j + 1] = tmp

li = [3,0,4,2,1]

print(li)
charu_paixu(li)
print(li)



def insert_(li):
    for i in range(1,len(li)):
        tmp = i
        j = i -1
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp





def insert_1(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i-1
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j + 1] = tmp



def insert_2(li):
    for i in range (1,len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp

def insert_3(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i -1
        while j >= 0 and li[j] > tmp :
            li[j+1] = li[j]
            j -= 1
        li[j+ 1] = tmp











