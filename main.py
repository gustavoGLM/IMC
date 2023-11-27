print("IMC\n")

a = float(input("Insert your height(m): "))
p = float(input("Insert your weight(kg): "))

imc = p / (a**2) 
imc1 = round (imc, 2)

print("Your IMC is:", imc1)

if imc1 < 18.5:
    print("Magreza")
elif 18.5 <= imc1 <= 24.9:
    print("Normal")
elif 25 <= imc1 <= 29.9:
    print("Sobrepeso")
elif 30 <= imc1 <= 34.9:
    print("Obesidade 1")