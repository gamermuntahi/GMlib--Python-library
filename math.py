# ================================
# PRIME NUMBER IDENTIFIER
# ================================

def IS_PRIME_CORE(n):
    if n < 2:
        return False

    limit = int(n**0.5) + 10
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True


def IS_PRIME(num=None):
    if num is None:
        num = int(input("Enter a number: "))
    return IS_PRIME_CORE(num)


# ================================
# ROOT FINDER (NO FLOAT)
# ================================

def ROOT_CORE(n):
    """Returns exact square root if perfect square,
       otherwise returns high-precision decimal root"""

    def int_sqrt(x):
        r = x
        s = (r + x // r) // 2
        while s < r:
            r = s
            s = (r + x // r) // 2
        return r

    r = int_sqrt(n)

    # Exact root check
    if r * r == n:
        return r

    # High precision decimal root
    digits = 20
    scale = 10 ** (2 * digits)
    r2 = int_sqrt(n * scale)

    return r2 / (10 ** digits)


def ROOT(n=None):
    """User-friendly root function"""
    if n is None:
        n = int(input("Enter a number: "))
    return ROOT_CORE(n)

# ================================
# BASIC OPERATIONS
# ================================

def ADD(a, b):
    return a + b

def SUB(a, b):
    return a - b

def MUL(a, b):
    return a * b

def DIV(a, b):
    if b == 0:
        return "Undefined (division by zero)"
    return a / b

def MOD(a, b):
    return a % b

def POWER(a, b):
    return a ** b


# ================================
# FACTORIAL
# ================================

def FACT(n):
    if n < 0:
        return "Invalid"
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


# ================================
# EVEN / ODD
# ================================

def IS_EVEN(n):
    return n % 2 == 0

def IS_ODD(n):
    return n % 2 != 0


# ================================
# GCD / LCM
# ================================

def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def LCM(a, b):
    return (a * b) // GCD(a, b)


# ================================
# FIBONACCI
# ================================

def FIB(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


# ================================
# DIGIT BASED CALCULATIONS
# ================================

def DIGIT_SUM(n):
    s = 0
    for i in str(abs(n)):
        s += int(i)
    return s

def DIGIT_COUNT(n):
    return len(str(abs(n)))

def REVERSE_NUM(n):
    rev = str(abs(n))[::-1]
    if n < 0:
        return -int(rev)
    return int(rev)


# ================================
# NUMBER PROPERTY CHECKS
# ================================

def IS_PERFECT_SQUARE(n):
    r = int(n ** 0.5)
    return r * r == n

def IS_ARMSTRONG(n):
    s = 0
    d = len(str(n))
    t = n
    while t > 0:
        s += (t % 10) ** d
        t //= 10
    return s == n

def IS_PALINDROME(n):
    return str(n) == str(n)[::-1]


# ================================
# RANGE UTILITIES
# ================================

def PRIME_RANGE(a, b):
    plist = []
    for i in range(a, b + 1):
        if IS_PRIME_CORE(i):
            plist.append(i)
    return plist

def FACT_RANGE(n):
    flist = []
    for i in range(1, n + 1):
        flist.append(FACT(i))
    return flist


# ================================
# COMPARISON UTILITIES
# ================================

def MAX2(a, b):
    if a > b:
        return a
    return b

def MIN2(a, b):
    if a < b:
        return a
    return b

def MAX3(a, b, c):
    return MAX2(MAX2(a, b), c)

def MIN3(a, b, c):
    return MIN2(MIN2(a, b), c)


# ================================
# PERCENTAGE & AVERAGE
# ================================

def PERCENT(total, part):
    return (part * 100) / total

def AVERAGE(nums):
    return sum(nums) / len(nums)
