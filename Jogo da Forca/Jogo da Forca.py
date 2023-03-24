# Desenvolvido por Renato Fernandes (renatofernandes.dev@gmail.com)
import random
import os

arquivo = open('palavras.txt')  # Importa o arquivo de texto
linhas = arquivo.readlines()  # Lê as linhas
palavras = random.choice(linhas).strip()  # Escolhe uma palavra aleatória da lista lida anteriormente.

lista = []  # Lista vazia para registro de letras.

chances = 6  # Número de chances.

ativar = True  # Coloquei essa variável como True para controlar o funcionamento do while e evitar usar break.

#print(palavras)    # Estava usando para testes
print("================================================\n"
      "=======      Olá, seja bem vindo ao      =======\n"
      "=======        Jogo da Forca x.x         =======\n"
      "=======         - Boa Sorte ! -          =======\n"
      "================================================\n")


while ativar is True:  # Condição while para o funcionamento da lógica do programa abaixo.

    chute = str(input("Digite uma letra: ").upper()).strip()  # Input do chute com auto caps-lock e strip()
    # para remoção de possíveis erros de entrada.

    if len(chute) > 1 or chute.isdigit() == True:  # Condições para avisar possíveis erros de entrada como
        # mais de uma letra ou entrada de números.
        print("\nInsira somente uma letra !\n")
    else:
        lista.append(chute)  # Append para adicionar o chute à lista
        sequencia = ''  # Sequencia vazia para o funcionamento da lógica abaixo
        for letra in palavras:  # Conta o index da palavra certa num loop chamado letra e adiciona no if abaixo
            if letra in lista:  # Se o número do loop estiver na lista que foi adicionado pelo append.chute(), então
                sequencia += letra  # A letra será adicionada na sequencia pelo index do loop letra.
            else:
                sequencia += '_'  # Caso contrário, adicionará um underline vazio, com o tamanho da palavra

        if chute not in palavras:
            chances -= 1  # Variavel para diminuição de chances

        # Interface "gráfica" do programa logo abaixo.
        if chances == 6:
            print("  _______     ")
            print(" |/      |    ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print("/|\__         ")
            print(f"Você já digitou: {sequencia}\n")
            print(f"Você ainda tem {chances} chances.\n")

        if chances == 5:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print("/|\__         ")
            print("------- Você errou! -------\n")
            print(f"Você já digitou: {sequencia}\n")
            print(f"Você ainda tem {chances} chances.\n")
        if chances == 4:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |       |    ")
            print(" |       |    ")
            print(" |            ")
            print(" |            ")
            print("/|\__         ")
            print("------- Você errou! -------\n")
            print(f"Você já digitou: {sequencia}\n")
            print(f"Você ainda tem {chances} chances.\n")
        if chances == 3:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      /|    ")
            print(" |       |    ")
            print(" |            ")
            print(" |            ")
            print("/|\__         ")
            print("------- Você errou! -------\n")
            print(f"Você já digitou: {sequencia}\n")
            print(f"Você ainda tem {chances} chances.\n")
        if chances == 2:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      /|\   ")
            print(" |       |    ")
            print(" |            ")
            print(" |            ")
            print("/|\__         ")
            print("------- Você errou! -------\n")
            print(f"Você já digitou: {sequencia}\n")
            print(f"Você ainda tem {chances} chances.\n")
        if chances == 1:
            print("  _______     ")
            print(" |/      |    ")
            print(" |      (_)   ")
            print(" |      /|\   ")
            print(" |       |    ")
            print(" |      /     ")
            print(" |            ")
            print("/|\__         ")
            print("------- Você errou! -------\n")
            print(f"Você já digitou: {sequencia}\n")
            print("Você tem mais uma chance!\n")

        if chances <= 0:
            print("  _______     ")
            print(" |/      |    ")
            print(" |     (x-x)   ")
            print(" |      /|\   ")
            print(" |       |    ")  # Conferencia de 0 chances e mensagem de derrota
            print(" |      / \   ")
            print(" |            ")
            print("/|\__         ")
            ativar = False  # Desativa a funcionalidade do programa para evitar uso do break ;)
            print(f"Você digitou: {sequencia}\n\nVocê perdeu! A palavra certa era: {palavras}.\n")
            os.system("pause") 
        else:
            if sequencia == palavras:  # Conferencia da sequencia com palavra certa
                ativar = False  # Desativa a funcionalidade do programa para evitar uso do break ;)
                print("\n-Parabéns, você venceu!-")
                print("       ___________      ")
                print("      '._--====--.'     ")
                print("     .-\\:       /-.    ")
                print("     | (|.       |) |    ")  # Mensagem de vitória
                print("      \'|:.      |'/    ")
                print("        \::.     /      ")
                print("         '::. .'        ")
                print("           ) (          ")
                print("         _.' '._        ")
                print("       '========='       \n")
                os.system("pause")

arquivo.close()  # Fecha o arquivo de texto lido para evitar possíveis erros.
