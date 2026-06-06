# GMlib/boolean_algebra_logic_gates.py
# =====================================
# Boolean Algebra, Logic Gates & Binary Arithmetic (Base 2)
# =====================================

# -------------------------
# Logic Gates
# -------------------------
def AND(a: int, b: int) -> int:
    return a & b

def OR(a: int, b: int) -> int:
    return a | b

def NOT(a: int) -> int:
    return 1 - a

def NAND(a: int, b: int) -> int:
    return NOT(AND(a, b))

def NOR(a: int, b: int) -> int:
    return NOT(OR(a, b))

def XOR(a: int, b: int) -> int:
    return a ^ b

def XNOR(a: int, b: int) -> int:
    return NOT(XOR(a, b))


# -------------------------
# Binary Arithmetic Using Logic Gates
# -------------------------
def full_adder_bit(a: int, b: int, carry: int) -> tuple[int, int]:
    """Add two bits with carry. Returns (sum, carry_out)."""
    sum_bit = XOR(XOR(a, b), carry)
    carry_out = OR(OR(AND(a, b), AND(b, carry)), AND(a, carry))
    return sum_bit, carry_out

def binary_add(a: str, b: str) -> str:
    """Add two binary numbers represented as strings."""
    # Make equal length
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ""
    carry = 0
    for i in range(max_len-1, -1, -1):
        s, carry = full_adder_bit(int(a[i]), int(b[i]), carry)
        result = str(s) + result
    if carry:
        result = "1" + result
    return result

def binary_subtract(a: str, b: str) -> str:
    """Subtract b from a (a >= b) in binary using two's complement."""
    # Convert b to two's complement
    b_inv = ''.join('1' if x=='0' else '0' for x in b.zfill(len(a)))
    sum_result = binary_add(a.zfill(len(b_inv)), binary_add(b_inv, "1".zfill(len(b_inv))))
    return sum_result[-len(a):]  # ignore overflow

def binary_multiply(a: str, b: str) -> str:
    """Multiply two binary numbers."""
    a = a[::-1]
    b = b[::-1]
    result = "0"
    for i in range(len(b)):
        if b[i] == "1":
            temp = a[::-1] + "0"*i
            result = binary_add(result.zfill(len(temp)), temp)
    return result.lstrip("0") or "0"

def binary_divide(dividend: str, divisor: str) -> tuple[str, str]:
    """Binary division. Returns (quotient, remainder)."""
    dividend = dividend.lstrip("0") or "0"
    divisor = divisor.lstrip("0") or "0"
    if divisor == "0":
        raise ValueError("Cannot divide by zero in binary!")

    quotient = ""
    remainder = ""
    for bit in dividend:
        remainder += bit
        if int(remainder,2) >= int(divisor,2):
            remainder = binary_subtract(remainder, divisor)
            quotient += "1"
        else:
            quotient += "0"
    return quotient.lstrip("0") or "0", remainder.lstrip("0") or "0"


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    print("Binary Addition 101 + 11 =", binary_add("101", "11"))
    print("Binary Subtraction 101 - 11 =", binary_subtract("101", "11"))
    print("Binary Multiplication 101 * 11 =", binary_multiply("101", "11"))
    print("Binary Division 1101 / 11 =", binary_divide("1101", "11"))
