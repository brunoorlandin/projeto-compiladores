from ast import pattern
from logging.config import IDENTIFIER
import re

'''letras = [a-z] + [A-Z]
digito = "0" + "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9"
simbolos =  "!" + "@" + "#" + "$" + "%" + "&" + "*"

IDENTIFIER: letra.(letra + digito + simbolo)*
NUMERIC: (digito+) + (digito+.".".digito+)
'''

identifier = "[a-zA-z]+[a-zA-z0-9]"
numeric = "([0-9]+)|([0-9].[0-9]+)"
sword = "sword"

texto = "1"

while(texto != ""):
  texto = input("Texto: ")

  if(re.search(sword, texto)):
    print("Passou")
  else:
    print("Nao passou")
