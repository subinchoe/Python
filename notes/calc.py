def plus(n, m):
    return n + m
    
def minus(n, m):
    return n - m

def multiplication(n, m):
    return n * m

def division(n, m):
    try:
        return n / m
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'