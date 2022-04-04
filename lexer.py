
from ast import Pass
from tokens import Token
#Meu primeiro lexer

#Definir os tokens da minha linguagem

#EOF: token que representa o fim de um arquivo (end of file)
INTEGER, STRING, IDENTIFIER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF = (
  "INTEGER", "STRING", "IDENTIFIER", "PLUS", "MINUS", "MUL", "DIV", "(", ")", "EOF"
)

#Palavras reservadas
reserved = {}
reserved['types'] = ['sword', 'shield', 'armor']
reserved['arithmetic_operators'] = ['buff', 'debuff', 'heal', 'poison']
reserved['conditional_operators'] = ['hit', 'miss']
reserved['compare_operators'] = ['attack', 'defense', 'dodge', 'critical', 'block']
#


#classe que implementa o analisador lexico
class Lexer(object):
  def __init__(self, text):
    #string do usuario
    self.text = text
    #indice que marca a posicao do texto (o caractere corrente sendo processado no texto)
    self.pos = 0
    #guarda o caractere que está sendo analisado de fato
    self.current_char = self.text[self.pos]
    #identifica se é string
    self.is_string = False
    #identifica se está em processo de verificação
    self.is_verifier = False

  #para retorno de erro
  def error(self):
    raise Exception("Invalid character!")

  #funcao que avanca caractere a caractere no texto
  #vai avancar o indice "pos" e modificar o conteudo da variavle "current_char"
  def advance(self):
    self.pos += 1
    #verifica se a leitura chegou ao fim da sentença
    if self.pos > len(self.text) - 1:
      self.current_char = None
    else:
      self.current_char = self.text[self.pos]

  #funcao que pula um espaco em branco e avanca para o proximo caractere
  def skip_whitespace(self):
    while self.current_char is not None and self.current_char.isspace():
      self.advance()
	
  def string(self):
    result = '"'
    self.advance()
    while self.current_char is not None and self.current_char is isinstance(self.current_char, str) and self.current_char is not '"':
      result += self.current_char
      self.advance()
    result += self.current_char
    return result
  
  #funcao que verifica se um lexema lido eh um inteiro
  def integer(self):
    #variavel para concatecar numeros
    result = ""
    while self.current_char is not None and self.current_char.isdigit():
      result += self.current_char
      self.advance()
    return int(result)

	#função que verifica as palavras reservadas
  def verify(self):
    found_list = []
    result = ""
    if self.pos == 0:
      for word in reserved:
        if word[self.pos] is self.current_char:
          found_list.append(word)
      result += self.current_charf
      self.advance()

    while len(found_list) != 1 and self.current_char is not ' ':
      for word in found_list:
        if word[self.pos] is not self.current_char:
          found_list.remove(word)
      result += self.current_char
      self.advance()    
    
    if len(found_list) == 1:
        return Token(found_list[0].upper(), result)
    
    if self.current_char.isspace():
      return Token(IDENTIFIER, result)
        
  #funcao que implementa o "core/nucleo" do analisador lexico
  #vai quebrar a sentença/arquivo de texto em vários tokens, um por vez
  def get_next_token(self):
    #executa enquanto o caractere corrente não for None
    while self.current_char is not None:
      #verifica se o caractere corrente eh um espaco em branco
      if self.current_char.isspace():
        self.skip_whitespace()
        continue

      #verifica se o caractere atual é um digito
      if self.current_char.isdigit():
        #retorno um Token do tipo INTEGER, com valor referente ao lexema sendo processado caractere a caractere
        return Token(INTEGER, self.integer())

      #verifica se o caractere é uma string
      if self.current_char == '"':
        return Token(STRING, self.string())
      #verifica se o lexema encontrado é um operador
      
      #verifica se o lexema encontrado é um parenteses (abrindo ou fechando)
      if self.current_char == "(":
        self.advance()
        return Token(LPAREN, "(")

      if self.current_char == ")":
        self.advance()
        return Token(RPAREN, ")")

      #se nenhum dos lexemas acima foi encontrado, gera um erro
      self.error()

    #no fim, retorna o Token de fim de linha
    return Token(EOF, None)

#programa principal que invoca o analisador lexico/Lexer
def main():
  #le o input de texto
  while True:
    try:
      try:
        text = raw_input("myLexer> ")
      except NameError:
        text = input("myLexer> ")
    except EOFError:
      break
    if not text:
      continue
    
    #instancio o lexer
    lexer = Lexer(text)
    '''Imprime todos os tokens '''
    #reconheco o primeiro token do input
    token = lexer.get_next_token()
    #enquanto o token retornado for diferente de EOF, continua processando o texto
    while(token.type is not EOF):
      print(token)
      token = lexer.get_next_token()


if __name__ == "__main__":
  main()
