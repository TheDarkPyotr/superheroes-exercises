class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        limit = len(s)
        negative = False
        somma = 0
        limit_inf = -2 ** 31
        limit_sup = 2 ** 31 - 1

        while i < limit and s[i] == " ":
            i += 1
        if i < limit and s[i] == "-":
            negative = True
            i += 1
        elif i < limit and s[i] == "+":
            i += 1
        while i < limit and s[i].isdigit():
            somma = (somma * 10) + int(s[i])
            i += 1
        if negative is True:
            somma *= -1
            if somma < limit_inf:
                return limit_inf
        else:
            if somma > limit_sup:
                return limit_sup
        return somma