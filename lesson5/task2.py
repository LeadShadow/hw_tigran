# 50% -> 0.5
# 1% -> 0.01
# 100% -> 1

def discount_price(price, discount):
    def apply_discount():
        nonlocal price, discount
        return price * (100 - discount) / 100  # -> 1000 * 50 / 100
    price = apply_discount()
    return price


input_price = input('Input price: ')
input_discount = input('Input discount: ')
print(discount_price(int(input_price), int(input_discount)))
