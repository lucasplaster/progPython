# Adivinha a palavra que o programa escolhe aleatoriamente

import os
import random
import time

#palavras disponiveis
dados = ['motocicleta', 'banana', 'carreta', 'gatinhos', 'programa', 'computador', 'tecnologia', 'inovar', 'microondas', 'bolacha', 'liberdade']
user_input = ''
contador = 0
letras_ja_digitadas = [""]
#Escolhendo uma palavra aleatoriamente
palavra_secreta = random.choice(dados)

palavra_cifrada = list("*"*len(palavra_secreta))

while list(palavra_secreta) != palavra_cifrada:
    os.system('clear')
    print("Eu pensei uma palavra. Tente adivinhar.")
    if contador > 0:
        print(f"Você já acertou {len(palavra_cifrada) - palavra_cifrada.count("*")} de {len(palavra_cifrada)}.")
    
    for i in palavra_cifrada:
        print(i, end="")
    print("")
    print("Digite uma letra: ")
    user_input = input(">>> ")[0].lower()
    if user_input not in letras_ja_digitadas:
        if user_input not in palavra_secreta:
            print(f"A letra {user_input} não está na palavra secreta")
            letras_ja_digitadas += user_input
            time.sleep(3)
            contador += 1
        else:
            for i in range(len(palavra_secreta)):
                if user_input == palavra_secreta[i]:
                    palavra_cifrada[i] = user_input[0]
            contador += 1
            letras_ja_digitadas += user_input
    elif user_input in letras_ja_digitadas:
        print(f"A letra {user_input} já foi digitada.")
        time.sleep(3)

os.system('clear')
print("Parabéns !")
print(f"A palavra é {palavra_secreta}.")
print(f"Você usou {contador} chances.")
