'''
letras = [a-z] + [A-Z]
digito = "0" + "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9"
simbolos =  "!" + "@" + "#" + "$" + "%" + "&" + "*"

IDENTIFIER: letra.(letra + digito + simbolo)*
INTEGER: (digito+)
STRING: ".letra*"
L_CHAVE: {
R_CHAVE: }
ATRIBUIDOR: =
EOL: ;

## Tipos das variaveis
# Para os tipos das variaveis foram utilizados as palavras abaixo:
# a palavra "sword" corresponde ao tipo char (string)
# a palavra "shield" corresponde ao tipo inteiro

# Tokens e expressoes regulares:
SWORD: s.w.o.r.d 
SHIELD: s.h.i.e.l.d

## Operadores aritimeticos
# Para os operadores aritimeticos foram utilizadas as palavras abaixo
# "buff" significa o operador de adicao (+)
# "debuff" significa o operador de subtracao (-)
# "heal" significa o operador de multiplicacao (*)
# "poison" significa o operador de divisao (/)

# Tokens e expressoes regulares:
BUFF: b.u.f.f
DEFUBB: d.e.b.u.f.f
HEAL: h.e.a.l
POISON: p.o.i.s.o.n

## Estruturas condicionais
# Para as estruturas condicionais foram utilizadas as palavras abaixo
# "hit" correspondendo ao se (condicao verdadeira)
# "miss" correspondente ao se não (condicao nao veridadeira)

# Tokens e expressoes regulares:
HIT: h.i.t
MISS: m.i.s.s

## Simbolos de comparacao
# Para os simbolos de comparacao foram utilizadas as palavras abaixo:
# "attack" correspondendo a maior (>)
# "defense" correspondendo a maior (<)
# "dodge" correspondendo a comparacao de igualdade (==)
# "critical" correspondendo a maior (>=)
# "block" correspondendo a maior (<=)

# Tokens e expressoes regulares
ATTACK: a.t.t.a.c.k
DEFENSE: d.e.f.e.n.s.e
DODGE: d.o.d.g.e
CRITICAL: c.r.i.t.i.c.a.l
BLOCK: b.l.o.c.k

'''

class Token(object):
  def __init__(self, type, value):
    self.type = type
    self.value = value

  #representação em string da classe
  def __str__(self):
    return "Token({type}, {value})".format(type = self.type, value = repr(self.value))

  def __repr__(self):
    return self.__str__()
