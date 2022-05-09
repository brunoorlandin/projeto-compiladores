from lexer import Lexer
from tokens import Token

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis

class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def vardec(self):
        print("entrou vardec")
        '''vardec: (INTEGER | SWORD) IDENTIFIER EOL'''
        print(self.current_token)

        status = False

        token = self.current_token

        if token.type == "SHIELD":
            self.eat("SHIELD")
            self.eat("IDENTIFIER")
            print(self.lexer.pos)
            self.eat("EOL")
            print(self.lexer.pos)
            status = self.expr()
        elif token.type == "SWORD":
            self.eat("SWORD")
            self.eat("IDENTIFIER")
            print(self.lexer.pos)
            self.eat("EOL")
            print(self.lexer.pos)
            status = self.expr()

        print(self.lexer.pos)
        
        return status
    
    def basicop(self):
        print("entrou basicop")
        """
        basicop: IDENTIFIER ATRIBUIDOR IDENTIFIER (BUFF | DEBUFF | HEAL | POISON) IDENTIFIER EOL |
                 IDENTIFIER ATRIBUIDOR INTEGER (BUFF | DEBUFF | HEAL | POISON) INTEGER EOL
        """
        print(self.current_token)
        
        print(self.current_token.type)

        status = False

        self.eat("IDENTIFIER")
        self.eat("ATRIBUIDOR")

        token = self.current_token

        if token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            print("entrou if")
            if token.type in ["BUFF", "DEBUFF", "HEAL", "POISON"]:
                if token.type == "BUFF":
                    self.eat("BUFF")
                elif token.type == "DEBUFF":
                    self.eat("DEBUFF")
                elif token.type == "HEAL":
                    self.eat("HEAL")
                else:
                    self.eat("POISON")
            self.eat("IDENTIFIER")
            self.eat("EOL")
            status = self.expr()
        elif token.type == "INTEGER":
            self.eat("INTEGER")
            if token.type in ["BUFF", "DEBUFF", "HEAL", "POISON"]:
                if token.type == "BUFF":
                    self.eat("BUFF")
                elif token.type == "DEBUFF":
                    self.eat("DEBUFF")
                elif token.type == "HEAL":
                    self.eat("HEAL")
                else:
                    self.eat("POISON")
            self.eat("INTEGER")
            self.eat("EOL")
            status = self.expr()
        else:
            return status
        
        return status

    def attrib(self):
        """
        attrib: IDENTIFIER ATRIBUIDOR IDENTIFIER EOL | 
                IDENTIFIER ATRIBUIDOR (INTEGER | SWORD) EOL |
                IDENTIFIER ATRIBUIDOR (BUFF | DEBUFF | HEAL | POISON) IDENTIFIER EOL
        """


    def expr(self):
        print(self.current_token)

        '''
        expr: vardec | basicop | attib | if-else | Ɛ
        vardec: (INTEGER | SWORD) IDENTIFIER EOL
        basicop: INTEGER (BUFF | DEBUFF | HEAL | POISON) INTEGER EOL
        attrib: IDENTIFIER ATRIBUIDOR IDENTIFIER EOL | 
                IDENTIFIER ATRIBUIDOR (INTEGER | SWORD) EOL |
                IDENTIFIER ATRIBUIDOR (BUFF | DEBUFF | HEAL | POISON) IDENTIFIER EOL
        if-else: HIT cond L_CHAVE S R_CHAVE MISS L_CHAVE S  R_CHAVE S | HIT cond L_CHAVE S R_CHAVE
        cond: IDENTIFIER comp IDENIFIER | NUMERIC comp NUMERIC | STRING DODGE STRING
        comp: ATTACK | DEFENSE | DODGE | CRITICAL | BLOCK 
        '''


        if self.vardec():
            print("vardec")
            return True
        elif self.basicop():
            print("basicop")
            return True
        elif self.current_token.type == 'EOF':
            return True
        else:
            print(self.current_token)
            return False
        

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
        interpreter = Interpreter(lexer)
        result = interpreter.expr()

    print(result)
    
    # while True:
    #     try:
    #         #get the input
    #         text = input('calc> ')
    #     except EOFError:
    #         break
    #     if not text:
    #         continue
    #     lexer = Lexer(text)
    #     interpreter = Interpreter(lexer)
    #     result = interpreter.expr()
    #     print(result)


if __name__ == '__main__':
    main()