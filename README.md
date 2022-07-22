```python


class Color():
    GREEN = '\033[92m'
    LIGTH_GREEN = '\033[1;92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    BOLD = '\033[;1m'
    CYAN = '\033[1;36m'
    LIGHT_CYAN = '\033[1;96m'
    LIGTH_GREY = '\033[1;37m'
    DARK_GREY = '\033[1;90m'
    BLACK = '\033[1;30m'
    WHITE = '\033[1;97m'
    INVERTE = '\033[;7m'
    RESET = '\033[0m'
```


```python
from color import Color


print(Color.CYAN +
    '''
                                             _   _                 _____ 
                                 _ __  _   _| |_| |__   ___  _ __ |___ / 
                                | '_ \| | | | __| '_ \ / _ \| '_ \  |_ \ 
                                | |_) | |_| | |_| | | | (_) | | | |___) |
                                | .__/ \__, |\__|_| |_|\___/|_| |_|____/ 
                                |_|    |___/                        
    
        
    '''
    + Color.RESET)

```





```python

#cores ANSI

class Color():
    VERDE = '\033[92m'
    VERDE_CLARO = '\033[1;92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    NEGRITO = '\033[;1m'
    CYANO = '\033[1;36m'
    CYANO_CLARO = '\033[1;96m'
    CINZA_CLARO = '\033[1;37m'
    CINZA_ESCURO = '\033[1;90m'
    PRETO = '\033[1;30m'
    BRANCO = '\033[1;97m'
    INVERTE = '\033[;7m'
    RESET = '\033[0m'


#print(Color.VERDE_CLARO + "TESTE" + Color.RESET)

```

```python
    from color import Color
    
    print(Color.CYANO +
    '''
                                             _   _                 _____ 
                                 _ __  _   _| |_| |__   ___  _ __ |___ / 
                                | '_ \| | | | __| '_ \ / _ \| '_ \  |_ \ 
                                | |_) | |_| | |_| | | | (_) | | | |___) |
                                | .__/ \__, |\__|_| |_|\___/|_| |_|____/ 
                                |_|    |___/                        
    
        
    '''
    + Color.RESET)

```


