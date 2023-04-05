print(0.1 + 0.2 == 0.3)

print(round(0.1 + 0.2, 1))  # 0.30000000000000004
from decimal import Decimal, getcontext

getcontext().prec = 2
print(Decimal(1) / Decimal(7))  # Decimal

print(1 / 7)  # float


getcontext().prec = 35
print(Decimal(1) / Decimal(7))
# print(Decimal(0.1) + 0.2)

getcontext().prec = 2
print(float(Decimal(0.1) + Decimal(0.2)) == 0.3)


print(Decimal(0.2) + Decimal(0.1) == Decimal(0.3))

print(Decimal(0.2) + Decimal(0.1) == Decimal(0.3) + Decimal(0.0))
# Decimal(0.2) + Decimal(0.1) -> 0.30000000000000004
# Decimal(0.3) + Decimal(0.0) -> 0.30000000000000004