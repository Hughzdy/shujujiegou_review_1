# 作者：Hugh
# 创建日期；2023/2/8
import random


def select(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[min_loc] > li[j]:
                min_loc = j
        li[min_loc],li[i] = li[i],li[min_loc]
        print(li)

li = list(range(5))
random.shuffle(li)
select(li)


def sel(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range (i + 1,len(li)):
            if li[min_loc] > li[j]:
                min_loc = j
        li[min_loc],li[j] = li[j],li[min_loc]
        print(li)






