def leap_year(year):
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False


def rotate(s, n):
    for i in range(n):
        s = s[len(s) - 1] + s[:len(s) - 1]
    return s


def digit_count(n):
    even_count, odd_count, zero_count = 0, 0, 0
    n = str(n)
    for i in range(len(n)):
        if n[i] == ".":
            break
        elif n[i] == '0':
            zero_count += 1
        elif int(n[i]) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count, zero_count


def float_check(n):
    n = str(n)
    if n.isdigit():
        return True
    elif n.count(".") == 1 and n.replace(".", "").isdigit():
        return True
    return False

