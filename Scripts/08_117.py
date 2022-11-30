import math

degree = 360

print(degree * math.pi / 180)

print(math.radians(degree))

degree = 45

print(degree * math.pi / 180)

print(math.radians(degree))


small_r = 22
big_r = 27
family_r = 39
small_c = 11.5
big_c = 15.6
family_c = 22

print((small_r * 0.01) ** 2 * math.pi)

print((big_r * 0.01) ** 2 * math.pi)

print((family_r * 0.01) ** 2 * math.pi)


small_p = (small_r * 0.01) ** 2 * math.pi
big_p = (big_r * 0.01) ** 2 * math.pi
family_p = (family_r * 0.01) ** 2 * math.pi

small_1m = small_c / small_p
big_1m = big_c / big_p
family_1m = family_c / family_p

print(small_1m, big_1m, family_1m)


math_ls = dir(math)
print(math_ls)
