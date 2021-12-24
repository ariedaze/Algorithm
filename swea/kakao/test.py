import math

# def solution(n, k):
#     answer = 0
#     convert_n = convert(n, k).split("0")
#     print(convert_n)
#     for n in convert_n:
#         if n == "" or not is_prime(int(n)):
#             continue
#         answer += 1
    
#     return answer

# def convert(num, base):
#     rev_base = []
#     while num > 0:
#         num, mod = divmod(num, base)
#         rev_base += str(mod)
        
#     return "".join(rev_base[::-1])

# def is_prime(num):
#     for i in range(2, int(math.sqrt(num))+1):
#         if num % i == 0:
#             return False
#     return True    
    
# solution(437674, 3)

from copy import deepcopy


def ff():
    Q = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

    a = [0]
    # a[0] = deepcopy(cc(Q))
    print(cc(Q))

def cc(Q):
    a = []
    a = deepcopy(Q)
    print(a)
    return a

ff()