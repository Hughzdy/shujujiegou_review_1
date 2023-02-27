# 作者：Hugh
# 创建日期；2023/2/8

def shunxu_chazhao(li,vv):
    for index,va in enumerate(li):
        if va == vv:
            return print(index)
    else:
        return None

li = list(range(100000))
shunxu_chazhao(li,30)


