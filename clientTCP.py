import socket
import socket
import sys
import time
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão Falhou")
        print("Erro: {}".format(e))
        sys.exit()
    
    print("Socket criado com sucesso!!!")


    HostAlvo = input("Digite o Host a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente TCP Conectado com Sucesso no Host: " + HostAlvo + " e na porta: " + PortaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possivel conectar no Host: " + HostAlvo + " e Porta: " + PortaAlvo)
        print("Erro: {}".format(e))
        

if __name__ == "__main__":
    main()
    time.sleep(10)
    sys.exit()







