# Inteiro para float

preco = 10
preco = float(preco)

print(preco)

# Float para inteiro

preco = 20.5
preco = int(preco)

print(preco)

# Numérico para string

preco = 10.5
idade = 30

print(str(preco))
print(str(idade))

texto = f"Idade {idade} Preco {preco}" # usa-se para concatenar
print(texto)

# Obs.: não é possivel transformar str para float ou str para int

exemplo = "teste"
exemplo = float(exemplo)

print(exemplo)

exemplo = "teste"
exemplo = int(exemplo)

print(exemplo)