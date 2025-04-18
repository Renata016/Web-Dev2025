def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - min(goal // 5, big) * 5 <= small

def lone_sum(a, b, c):
    return (a if a != b and a != c else 0) + (b if b != a and b != c else 0) + (c if c != a and c != b else 0)

def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    return 0 if 13 <= n <= 19 and n not in {15, 16} else n


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    return (num + 5) // 10 * 10


def close_far(a, b, c):
    close_b = abs(a - b) <= 1
    close_c = abs(a - c) <= 1
    far_b = abs(a - b) >= 2 and abs(b - c) >= 2
    far_c = abs(a - c) >= 2 and abs(b - c) >= 2
    
    return (close_b and far_c) or (close_c and far_b)

def make_chocolate(small, big, goal):
    max_big = min(goal // 5, big)
    remaining = goal - max_big * 5
    return remaining if remaining <= small else -1

