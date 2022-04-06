
from ast import Pass
from tokens import Token

reserved = {}
reserved['types'] = ['sword', 'shield', 'armor']
reserved['arithmetic_operators'] = ['buff', 'debuff', 'heal', 'poison']
reserved['conditional_operators'] = ['hit', 'miss']
reserved['compare_operators'] = ['attack', 'defense', 'dodge', 'critical', 'block']

class Lexer(object):
  def __init__(self, text):
    self.text = text
    self.pos = 0
    self.current_char = self.text[self.pos]
    self.is_string = False
    self.is_verifier = False

  def error(self):
    raise Exception("Invalid character!")

  def advance(self):
    self.pos += 1
    
    if self.pos > len(self.text) - 1:
      self.current_char = None
    else:
      self.current_char = self.text[self.pos]

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
  
  def integer(self):
    
    result = ""
    while self.current_char is not None and self.current_char.isdigit():
      result += self.current_char
      self.advance()
    return int(result)

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
      return Token("IDENTIFIER", result)
        
  def get_next_token(self):
    
    while self.current_char is not None:
      
      if self.current_char.isspace():
        self.skip_whitespace()
        continue

      '''if self.current_char.isdigit():
        return Token(INTEGER, self.integer())

      if self.current_char == '"':
        return Token(STRING, self.string())'''
      
      if self.current_char == "(":
        self.advance()
        return Token("L_PAR", "(")

      if self.current_char == ")":
        self.advance()
        return Token("R_PAR", ")")

      if self.current_char == "{":
        self.advance()
        return Token("L_CHAVE", "{")

      if self.current_char == "}":
        self.advance()
        return Token("R_CHAVE", "}")

      if self.current_char == "=":
        self.advance()
        return Token("ATRIBUIDOR", "=")

      self.error()

    return Token("EOF", None)

def main():
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
    
    lexer = Lexer(text)
    '''Imprime todos os tokens '''
    
    token = lexer.get_next_token()
    
    while(token.type is not "EOF"):
      print(token)
      token = lexer.get_next_token()

if __name__ == "__main__":
  main()
