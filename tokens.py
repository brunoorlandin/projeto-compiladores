'''

letras = [a-z] + [A-Z]
digito = "0" + "1" + "2" + "3" + "4" + "5" + "6" + "7" + "8" + "9"
simbolos =  "!" + "@" + "#" + "$" + "%" + "&" + "*"

IDENTIFIER: letra.(letra + digito + simbolo)*
NUMERIC: (digito+) + (digito+.".".digito+)
L_PAR: (
R_PAR: )
L_CHAVE: {
R_CHAVE: }
ATRIBUIDOR: =

## Tipos das variaveis
# Para os tipos das variaveis foram utilizados as palavras abaixo:
# a palavra "sword" corresponde ao tipo char (string)
# a palavra "shield" corresponde ao tipo inteiro
# a palavra "armor" corresponde ao tipo float

# Tokens e expressoes regulares:
CHAR: s.w.o.r.d 
INT: s.h.i.e.l.d
FLOAT: a.r.m.o.r

## Operadores aritimeticos
# Para os operadores aritimeticos foram utilizadas as palavras abaixo
# "buff" significa o operador de adicao (+)
# "debuff" significa o operador de subtracao (-)
# "heal" significa o operador de multiplicacao (*)
# "poison" significa o operador de divisao (/)

# Tokens e expressoes regulares:
OP_SOMA: b.u.f.f
OP_SUB: d.e.b.u.f.f
OP_MULT: h.e.a.l
OP_DIV: p.o.i.s.o.n

## Estruturas condicionais
# Para as estruturas condicionais foram utilizadas as palavras abaixo
# "hit" correspondendo ao se (condicao verdadeira)
# "miss" correspondente ao se não (condicao nao veridadeira)

# Tokens e expressoes regulares:
IF: h.i.t
ELSE: m.i.s.s

## Simbolos de comparacao
# Para os simbolos de comparacao foram utilizadas as palavras abaixo:
# "attack" correspondendo a maior (>)
# "defense" correspondendo a maior (<)
# "dodge" correspondendo a comparacao de igualdade (==)
# "critical" correspondendo a maior (>=)
# "block" correspondendo a maior (<=)

# Tokens e expressoes regulares
MAIOR: a.t.t.a.c.k
MENOR: d.e.f.e.n.s.e
IGUALDADE: d.o.d.g.e
MAIOR_IGUAL: c.r.i.t.i.c.a.l
MENOR_IGUAL: b.l.o.c.k

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
