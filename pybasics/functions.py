import math


def compute_hypotenuse(l1, l2):
    hypotenuse = math.sqrt(l1**2 + l2**2)
    return hypotenuse


length_a = float(input('enter short side one \n'))
length_b = float(input('enter short side two \n'))


print(compute_hypotenuse(length_a, length_b))


def lesser_of_two_evens(a, b):
    if a+b % 2 == 0:
        print(min(a, b))
    else:
        print(max(a, b))


def animal_crackers(text):
    word_list = text.split()
    return word_list[0][0] == word_list[1][0]


print(animal_crackers('ghana baby')


def makes_twenty(n1, n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20


print(makes_twenty(2, 5))
# WHEN YOU RETURN A CONDITION IT RESULTS IN A TRUE OF FALSE'''


def taxi_fare(distance_traveled):
    total_fare_amount = 4.00 + ((distance_traveled * 1000)/140 * .25)
    return total_fare_amount


print(taxi_fare(2))


def middle_number(x, y, z):
    return x + y + z - max(x, y, z) - min(x, y, z)


print(middle_number(10, 45, 299))































