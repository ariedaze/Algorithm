from itertools import permutations


def solution(numbers):
    answer = []
    
    for r in range(1, len(numbers)+1):
        for number in permutations(numbers, r):
            candi = int("".join(list(number)))
            if is_prime(candi):
                answer.append(candi)

    return len(set(answer))


def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    else:
        return True
