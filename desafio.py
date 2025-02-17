# Integre na solução anterior um fluxo de While 
# que repita o fluxo até que o usuário insira as 
# informações corretas

BONUS = 1000
nome_valido = False
bonus_valido = False
salario_valido = False

# 1) Solicita ao usuário que digite seu nome
while nome_valido == False:
    try:
        nome_usuario = input('Informe seu nome: ')
        if len(nome_usuario) == 0:
            raise ValueError("O nome não pode estar vazio")
            exit()
        elif any(char.isdigit() for char in nome_usuario):
            raise ValueError("O nome não pode conter números.")
        else:
            nome_valido = True
    except ValueError as e:
        print(e)
        #exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
while salario_valido == False:
    try:
        salario_usuario = float(input('Informe seu salario: '))
        if salario_usuario < 0:
            raise ValueError("Informe um valor válido para o salário")
        else:
            salario_valido = True
    except ValueError as e:
        print("Entrada inválida, digite um valor numérico")



# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
while bonus_valido == False:
    try:
        bonus_usuário = float(input('Informe seu bonus: '))
        if bonus_usuário < 0:
            raise ValueError("Informe um valor válido para o bonus")
        else:
            bonus_valido = True
    except ValueError as e:
        print("Entrada inválida, digite um valor numérico")

# 4) Calcule o valor do bônus final
valor_bonus_calculado = BONUS + salario_usuario * bonus_usuário


# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'Olá, {nome_usuario}, seu salário com o bonus será de R${valor_bonus_calculado}')


# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
