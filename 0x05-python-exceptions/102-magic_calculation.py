#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for w in range(1, 3):
        try:
            if w > a:
                raise Exception('Too far')
            result += a ** b / w
        except Exception:
            result = b + a
            break
    return result
