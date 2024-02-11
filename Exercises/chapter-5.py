def count_case(s):
    s = str(s)
    upper, lower = 0, 0
    for i in range(len(s)):
        if s[i].isupper():
            upper += 1
        elif s[i].islower():
            lower += 1
    return upper, lower


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= n:
        if i == n:
            return True
        if n % i == 0:
            return False
        i += 1

def palindrome(s):
    s = str(s).lower()
    s = (s.replace(" ", "")
         .replace("!", "")
         .replace(",", "")
         .replace(".", "")
         .replace("?", "")
         .replace("'", "")
         .replace(":", "")
         .replace(";", "")
         .replace("-", "")
         .replace("(", "")
         .replace(")", "")
         .replace("[", "")
         .replace("]", "")
         .replace("{", "")
         .replace("}", ""))
    print(s)
    if s == s[::-1]:
        return True
    return False


print(palindrome("A man, a plan, a canal, Panama!"))