def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def next_prime_after(n: int) -> int:
    i = n + 1
    while True:
        if is_prime(i):
            return i
        i += 1


def first_prime_before(n: int) -> int:
    i = n - 1
    while True:
        if is_prime(i):
            return i
        i -= 1


def convert_str_to_int(key: str) -> int:
    length = len(key)
    l, r = 0, length - 1
    m = (l + r) // 2
    converted_key = 9 * (ord(key[l]) - ord("a")) + 1
    converted_key += (9 * (ord(key[r]) - ord("a")) + 1) * 37
    converted_key += (9 * (ord(key[m]) - ord("a")) + 1) * 37 * 37

    return converted_key
