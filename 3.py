import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

user = 51
sum = 0
for active in range(11):
    rate = float(combinations_count(user, active)) * pow(0.1, active) * pow(0.9, user-active)
    sum = sum + rate
print(1-sum)

