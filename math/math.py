def is_prime(x):
    if(x <2):
        return False
    for i in range(2, int(x**0.5) + 1):
        if(x % i == 0):
            return False
    return True

def is_int(x):
    if(abs(x) - round(abs(x)) > 0):
        return False
    else:
        return True

def digital_sum(n):
    ret = 0
    for item in str(n):
        ret += int(item)
    return ret

def reverse(text):
    ret = ""
    for c in text:
        ret = c + ret
    return ret