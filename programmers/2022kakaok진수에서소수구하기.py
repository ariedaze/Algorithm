def solution(n, k):
    answer = 0
    numbers = change(n, k).split('0')
    for number in numbers:
        if is_prime(number): answer += 1
    return answer

def change(n, k):
    rev = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev += str(mod)
    return rev[::-1]
    

def is_prime(num):
    if not num or num == '1': return False
    number = int(num)
    for i in range(2, int(number**0.5)+1):
        if number % i == 0: return False
        
    return True