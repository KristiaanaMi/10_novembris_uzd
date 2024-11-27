# Izveidot programmu, kura prasa lietotâjam ievadît cilindra râdiusu un tâ augstumu, tiek aprçíinâts cilindra laukums un tilpums. Rezultâts tiek parâdîts konsolç.
# tilpums = 3.14 * râdiuss * râdiuss * augstums
# laukums = 2 * (3.14 * râdiuss * râdiuss) + augstums * (2 * 3.14 * râdiuss)

import math

radius=float(input("Lūdzu ievadi cilindra radiusu:"))
height=float(input("Lūdzu ievadi cilindra augstumu"))

PI=3.14

volume = PI * radius**2 * height

surface_area = 2 * (PI * radius**2) + (2 * PI * radius * height)

print(f"Cilindra tilpums ir : {volume:.27}")
print(f"Cilindra laukums ir : {surface_area:.2f}")