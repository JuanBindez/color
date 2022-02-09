

class Color():
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    VERDE_CLARO = '\033[1;92m'
    NEGRITO = '\033[;1m'
    RESET = '\033[0m'



print(Color.VERDE_CLARO + "TESTE" + Color.RESET)
