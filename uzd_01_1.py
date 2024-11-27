# Uzdevums: 01-1: Izveidot programmu, kas prasa lietotâjam ievadît skaitli n, tad programma aprçíina n+nn+nnn. 
#Rezultâts tiek parâdîts konsolç.

n = input("Ievadi skaitli n: ")
summa = int(n) + int(n * 2) + int(n * 3)
print(f"{n} + {n*2} + {n*3} = {summa}")
