base_rate = 40  # базовий тариф
price_per_km = 10  # ціна за кожен кілометр
total_trip = 0  # кількість поїздок
total_sum = 0
s = 'hello world'


def trip_price(path: int):
    global total_trip, total_sum
    total_trip += 1
    sum = base_rate + price_per_km * path
    total_sum += sum
    return sum


print(trip_price(5))
print(total_trip)
print(trip_price(2))
print(total_trip)
print(trip_price(4))
print(total_trip)
print(trip_price(7))
print(total_trip)
print(trip_price(1))
print(total_trip)
print(trip_price(4))
print(total_trip)
print(trip_price(3))
print(total_trip)
print(trip_price(9))
print(total_trip)
print(trip_price(6))
print(total_trip)
print(trip_price(7))
print(total_trip)
print(trip_price(2))
print(total_trip)
print(trip_price(5))
print(total_trip)
print(trip_price(1))
print(total_trip)

print('Загальна сума грошей ==', total_sum)
