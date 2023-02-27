# 作者：Hugh
# 创建日期；2023/2/11

def merge(li,low,mid,hight):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j<=hight:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while 执行完毕 勘定有一部分没有数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= hight:
        ltmp.append(li[j])
        j +=1
    li[low:hight+1] = ltmp
























