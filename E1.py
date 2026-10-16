# E1. a)
s = 0

for i in range(1, 101):
    s += i

print("Suma primelor 100 de numere naturale este: " + str(s))

# 1. b)
s2 = (100 * 101) / 2
print("Suma primelor 100 de numere naturale folosind suma lui Gauss este: " + str(s2))

# 1. c)
s3 = 0

for i in range(50, 151):
    s3 += i

print("Suma tuturor numerelor naturale cuprinse intre 50 si 150: " + str(s3))

# 1. d)
s4 = 0

for i in range(50, 151, 10):
    s4 += i

print("Suma tuturor numerelor naturale cuprinse intre 50 si 150 divizibile cu 10 este: " + str(s4))