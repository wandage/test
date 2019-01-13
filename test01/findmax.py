# coding=utf-8


li = [10,20,30,44,55,8888,5555]

def findMax(li):
    max = li[0]
    for x in li:
       if x > max:
           max = x
    return max


print(findMax(li))
print("66")



