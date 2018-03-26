def is_leap_year(year):
    not_divisible_100 = year % 100 != 0
    divisible_400 = year % 400 == 0
    divisible_4 = year % 4 == 0
    return divisible_4 and not_divisible_100 or divisible_400
