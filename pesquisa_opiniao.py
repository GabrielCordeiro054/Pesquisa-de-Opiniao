# Pesquisa de Opinião - TudoWeb

excelente = 0
ruim = 0

for i in range(1, 51):
    print("\nEntrevistado", i)

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print("\n===== RESULTADO DA PESQUISA =====")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)