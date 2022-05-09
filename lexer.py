
from tokens import Token
import re

reserved = {}
reserved['types'] = ['sword', 'shield', 'armor']
reserved['arithmetic_operators'] = ['buff', 'debuff', 'heal', 'poison']
reserved['conditional_operators'] = ['hit', 'miss']
reserved['compare_operators'] = ['attack', 'defense', 'dodge', 'critical', 'block']

identifier = re.compile("[a-zA-z]+[a-zA-z0-9]")

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
    while self.current_char != None and self.current_char.isspace():
      self.advance()
	
  def string(self):
    result = '"'
    self.advance()
    while self.current_char != None and self.current_char != '"':
      if self.current_char != None: 
        result += self.current_char
      self.advance()
    result += '"'
    self.advance()
    return Token('STRING', result)
  
  def integer(self):
    result = ""
    while self.current_char != None and self.current_char.isdigit():
      result += self.current_char
      self.advance()
    return int(result)
  
  def verify(self):
    found_list = []
    result = ""
    if len(result) == 0:
      for key in reserved:
        for word in reserved[key]:
          if word[len(result)] is self.current_char:
            found_list.append(word)
      result += self.current_char
      self.advance()
    while len(found_list) != 1 and self.current_char != ' ' and self.current_char != None:
      for word in found_list:
        if word[len(result)] != self.current_char:
          found_list.remove(word)
      result += self.current_char
      self.advance()    
    
    if len(found_list) == 1:
      while len(found_list[0]) != len(result):
        result += self.current_char
        self.advance()
      return Token(found_list[0].upper(), result)
    if result[-1] == ';':
      self.pos -= 1
      result = result[:-1]
      return Token("IDENTIFIER", result)
    if self.current_char.isspace():
      return Token("IDENTIFIER", result)
        
  def get_next_token(self):
    result = ""
    while self.current_char != None:
      if self.current_char.isspace():
        self.skip_whitespace()
        continue

      if self.current_char.isdigit():
        return Token('INTEGER', self.integer())

      if self.current_char == '"':
        return self.string()

      if self.current_char == "(":
        self.advance()
        return Token("L_PAR", "(")
      
      elif self.current_char == ")":
        self.advance()
        return Token("R_PAR", ")")
      
      elif self.current_char == "{":
        self.advance()
        return Token("L_CHAVE", "{")
      
      elif self.current_char == "}":
        self.advance()
        return Token("R_CHAVE", "}")

      elif self.current_char == "=":
        self.advance()
        return Token("ATRIBUIDOR", "=")
      elif self.current_char == ";":
        self.advance()
        return Token("EOL", ";")
      
      elif self.current_char != " ":
       # result += self.current_char
        return self.verify()
        continue
      
      else:
        if re.fullmatch(identifier, result):
          return Token("IDENTIFIER", "=")
        result = ""
        continue

      self.error()

    return Token("EOF", None)

def main():
  file = open("source.rpg", "r")
  line = file.readlines()
  lines_split = []
  lines = []

  for item in line:
    lines_split.append(item.split("\n"))

  for i in range(len(lines_split)):
    if lines_split[i][0] != '':
      lines.append(lines_split[i][0])

  for i in range(len(lines)):
    text = lines[i]
    lexer = Lexer(text)
    token = lexer.get_next_token()
    while token.type != "EOF":
      print(token)
      token = lexer.get_next_token()

if __name__ == "__main__":
  main()