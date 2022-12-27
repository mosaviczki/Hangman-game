import socket, pickle

IP = 'localhost'
PORT = 1234
global x
x = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

print("======= Bem vindo ao jogo da Forca! ======= ")
print("6 tentativas falhas e fim de jogo")

wordLen, spaces = pickle.loads(s.recv(128))
letters = [""] * wordLen
for i in range(wordLen):
    for j in spaces:
        if i == j:
            print(" ", end="")
            break
    else:
        print("_ ", end="")
print("\n")

for i in range(len(letters)):
    for j in spaces:
        if i == j:
            letters[i] = " "

while True:
    letra = input("Letra: ").upper()
    s.send(pickle.dumps(letra))
    t = pickle.loads(s.recv(128))
    data = pickle.loads(s.recv(128))

    if t == -2:
        print(f'\n{data}')
        s.close()
        exit(0)
    if t == -1:
        print(f'\n{data}')
        print("  _______     ")
        print(" |/      |    ")
        print(" |     (x_x)  ")
        print(" |      /|\   ")
        print(" |       |    ")
        print(" |      / \   ")
        print("_|___         ")
        s.close()
        exit(0)
    elif t == 1:
        indices, letra = data
        if letra in letters:
            print(f'A letra {letra} já foi, por favor, escolha uma letra diferente!\n')
            for i in letters:
                if i == "":
                    print("_ ", end="")
                else:
                    print(f'{i} ', end="")
            print("\n")
        else:
            for c in range(wordLen):
                for i in indices:
                    if c == i:
                        letters[i] = letra
            for i in letters:
                if i == "":
                    print("_ ", end="")
                else:
                    print(f'{i} ', end="")
            print("\n")
            ok = 1
            for i in letters:
                if i == "":
                    ok = 0
            if ok:
                print("Você ganhou!!!")
                print("  _____        _____            ____  ______ _   _  _____ ") 
                print(" |  __ \ /\   |  __ \     /\   |  _ \|  ____| \ | |/ ____|") 
                print(" | |__) /  \  | |__) |   /  \  | |_) | |__  |  \| | (___ ") 
                print(" |  ___/ /\ \ |  _  /   / /\ \ |  _ <|  __| | . ` |\___  |")
                print(" | |  / ____ \| | \ \  / ____ \| |_) | |____| |\  |____) |") 
                print(" |_| /_/    \_\_|  \_\/_/    \_\____/|______|_| \_|_____/ ") 
                s.close()
                

    elif t == 0:
        print(data)
        for i in letters:
            if i == "":
                print("_ ", end="")
            else:
                print(f'{i} ', end="")
        print("\n")
        val = True
        while val:
            if x == 1:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("_|___         ")
                x = 2
                break
            elif x == 2:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |       |    ")
                print(" |       |    ")
                print(" |            ")
                print("_|___         ")
                x = 3
                break
            elif x == 3:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      /|    ")
                print(" |       |    ")
                print(" |            ")
                print("_|___         ")
                x = 4
                break
            elif x == 4:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      /|\   ")
                print(" |       |    ")
                print(" |            ")
                print("_|___         ")
                x = 5
                break        
            elif x == 5:
                print("  _______     ")
                print(" |/      |    ")
                print(" |      (_)   ")
                print(" |      /|\   ")
                print(" |       |    ")
                print(" |      /     ")
                print("_|___         ")
                break 

