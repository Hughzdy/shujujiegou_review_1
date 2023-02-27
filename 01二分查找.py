# 作者：Hugh
# 创建日期；2023/2/8



def erfen_chazhao(li,v):
    left = 0
    right = len(li)-1
    while left <=right:
        mid =int ((right + left) / 2)
        if li[mid] == v:
            return mid
        elif li[mid] > v:
            right = mid - 1
        elif li[mid] <v:
            left = mid + 1
    else:
        return None


li = list(range(100000))
erfen_chazhao(li,20)

