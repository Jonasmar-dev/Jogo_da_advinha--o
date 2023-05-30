import random

palpite = 0
num_secreto = random.randint(1, 50)
tentativas = 0

while True:

    palpite = int(input("Arrisque um número: "))
    if tentativas < 5:
        tentativas += 1
    elif tentativas == 5:
        print("Número máximo de tentativas alcançado. O jogo acabou!")
        break

    if palpite == num_secreto:
        print("Mandou bem!")
    elif palpite < num_secreto:
        print(
            f"Ops! Palpite menor que o número secreto. tentativas: {tentativas}.")
    elif palpite > num_secreto:
        print(
            f"Ops! Palpite maior que o número secreto. tentativas: {tentativas}.")
    else:
        print("(Erro 404! kk) Opção inválida. Tente outro número.")

    jogar_novamente = input("Jogar mais uma vez? (SIM ou NÃO): ")
    if jogar_novamente.lower() == "sim":
        continue  # Continua o loop
    else:
        print(f"numero: {num_secreto}")
    break
