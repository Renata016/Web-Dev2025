def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40
    else:
        return 40 <= cigars <= 60 

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

def squirrel_play(temp, is_summer):
    return 60 <= temp <= (100 if is_summer else 90)

def caught_speeding(speed, is_birthday):
    speed_limit = 5 if is_birthday else 0
    if speed <= 60 + speed_limit:
        return 0
    elif speed <= 80 + speed_limit:
        return 1
    else:
        return 2

def sorta_sum(a, b):
    total = a + b
    return 20 if 10 <= total <= 19 else total

def alarm_clock(day, vacation):
    if vacation:
        return "10:00" if 1 <= day <= 5 else "off"
    return "7:00" if 1 <= day <= 5 else "10:00"

def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    return (1 <= n <= 10) if not outside_mode else (n <= 1 or n >= 10)

def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8
