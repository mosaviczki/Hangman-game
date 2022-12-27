import socket, pickle
from time import sleep
import random


clients = []
IP = 'localhost'
PORT = 1234


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def game(client):
    words = ['COMPUTACAO', 'DISTRIBUIDOS', 'BANANA', 'MACA', 'SOFTWARE']
    palavra = random.choice(words)
    tentativas = 6
    if not client in clients:
        clients.append(client)
    spaces = find(palavra, ' ')
    client.send(pickle.dumps((len(palavra), spaces)))
    while True:
        letra = client.recv(128)
        if not letra:
            exit(0)
        letra = pickle.loads(letra)
        if letra in palavra:
            indices = find(palavra, letra)
            client.send(pickle.dumps(1))
            sleep(0.1)
            client.send(pickle.dumps((indices, letra)))
        else:
            tentativas -= 1
            if tentativas == 0:
                client.send(pickle.dumps(-1))
                sleep(0.1)
                client.send(pickle.dumps(f'Fim de jogo! A palavra era: \'{palavra}\''))
                #client.close()
                exit(0)
            elif letra == 'BYE':
                client.send(pickle.dumps(-2))
                sleep(0.1)
                client.send(pickle.dumps(f'Bye, encerrando conexão com o servidor!'))
                client.close()
            else:
                client.send(pickle.dumps(0))
                sleep(0.1)
                client.send(pickle.dumps(f'{tentativas} tentativas'))


def main():
    host = 'localhost'
    port = 1234
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((IP, PORT))
        s.listen()
        print("Esperando conexão com cliente")

        while True:
            client, ender = s.accept()
            print("Conexão estabelecida")
            game(client)
            print("Fechando conexão")

    except ConnectionError:
        #print("[-] Error: Connection Losted: ", ender)
        print("Fechando conexão")
        client.close()
        s.close()
    except KeyboardInterrupt:
        print("[-] Exiting...")
        print("Fechando conexão")
        s.close()
    except OSError:
        print("[-] Error: Address already in use!")
        print("Fechando conexão")
        s.close()

if __name__ == '__main__':
    main()
