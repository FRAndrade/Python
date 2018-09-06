def pergunto(mensagem, tentativas = 3, lembrete = "Tente novamente"):
    while True:
        resp=input(mensagem)
        if resp in ("sim","s"):
            return True
        elif resp in ("nao","n"):
            return False
        else:
            tentativas = tentativas - 1
            if tentativas <=0:
                return -1
        print(lembrete)

def main():
    i = input ("Numero ")
    ir = int(i)
    print(pergunto("Suave",ir))
    i = input ("Numero ")
    ir = int(i)
    print(pergunto("Suave",ir))
