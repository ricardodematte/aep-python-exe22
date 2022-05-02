# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

import os
m = (int(input("Digite um valor em metros:\n")))
cm = m*100
mm = m*1000
os.system("clear")
print ("Metros =",m,"\nCentimetros =",cm,"\nMilimetros =",mm)