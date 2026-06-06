def decimal_to_binary(num: int) -> str:
    return bin(num)[2:]


def binary_to_decimal(binary_str: str) -> int:
    if not all(ch in "01" for ch in binary_str):
        raise ValueError("Binary number must contain only 0 or 1.")
    return int(binary_str, 2)


# Universal converter
def convert(value):
    """
    If the input is binary (only 0 and 1) → convert to decimal.
    If the input is decimal → convert to binary.
    """
    if isinstance(value, int):
        return decimal_to_binary(value)

    value = str(value)

    if all(c in "01" for c in value):
        return binary_to_decimal(value)

    # if decimal string
    if value.isdigit():
        return decimal_to_binary(int(value))

    raise ValueError("Invalid value for convert()")
