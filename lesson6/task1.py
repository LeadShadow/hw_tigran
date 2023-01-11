# 50% -> 0.5
# 1% -> 0.01
# 100% -> 1
def apply_discount(discount: str):
    if len(discount) == 1:
        # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        discount = '0.0' + discount[0]  # 5% -> '0.05'
    elif len(discount) == 2:
        discount = '0.' + discount[0] + discount[1]  # 55% -> '0.55'
    elif len(discount) == 3:
        discount = '1'  # 100% -> 1
    return float(discount)


def discount_price(price, discount):
    def apply_discount():
        nonlocal price, discount
        return price * (1 - discount)
    price = apply_discount()
    return price


if __name__ == "__main__":
    user_input = input('Input discount: ')
    discount = apply_discount(user_input)
    print(discount_price(price=1000, discount=discount))
