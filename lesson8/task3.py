list1 = [[1, 2, 3], [7, 5, 1], [10, 12]]


def game(terra, power):
    for terr in terra:
        for energy in terr:
            if energy <= power:
                power += energy
                print(power)
            else:
                return 'Game over'
    return power


print(game(list1, 1))
