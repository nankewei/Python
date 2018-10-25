# 
# from math import sqrt
# def is_prime（n）:
#     if n == 1:
#         return False
#     for i in range（2, int（sqrt（n））+1）:
#         if n % i == 0:
#             return False
#     return True
#奇数序列生成器
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


#筛选函数
def is_notDivisable(n):
    return lambda x: x % n > 0


#奇数序列中筛选素数
def prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(is_notDivisable(n), it)


for n in prime():
    if n < 1000:
        print(n)
    else:
        break
