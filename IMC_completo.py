nome = input("Digite o seu primeiro nome ")
sobrenome = input("Qual o seu sobrenome? ")
alt=float(input("Qual a sua altura em metros? "))
peso = float(input("Qual o seu peso? (em Kg) "))

print("Olá", sobrenome,",",nome, "! Bem vindo(a) a calculadora de IMC! Vamos ver seus dados: \n peso:",peso,"kg \n","altura:",alt, "metros")

IMC = peso/(alt**2)

print(nome,"seu IMC é:",IMC)

if (IMC<18.5):
    print(nome,"você está abaixo do peso")
elif (IMC>=18.5 and IMC<=24.9):
    print(nome,"você está no peso ideal! Parabéns!")
elif (IMC>=25 and IMC<=29.9):
    print(nome,"você está acima do peso.")
elif (IMC>=30 and IMC<=34.9):
    print(nome,"sua classificação é: Obesidade grau I")
elif (IMC>=35 and IMC<=39.9):
    print(nome,"sua classificação é: Obesidade grau II")
else:
    print(nome,"sua classificação é: Obesidade mórbida")