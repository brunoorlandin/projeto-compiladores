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

        pos = self.lexer.pos
        token = self.current_token

        if self.current_token.type == "SHIELD":
            self.eat("SHIELD")
            if self.current_token.type == "IDENTIFIER":
                self.eat("IDENTIFIER")
                print(self.lexer.pos)
                
                if self.current_token.type == "EOL":
                    self.eat("EOL")
                    print(self.lexer.pos)
                    status = self.expr()
        elif self.current_token.type == "SWORD":
            self.eat("SWORD")
            if self.current_token.type == "IDENTIFIER":
                self.eat("IDENTIFIER")
                print(self.lexer.pos)
                if self.current_token.type == "EOL":
                    self.eat("EOL")
                    print(self.lexer.pos)
                    status = self.expr()

        print(self.lexer.pos)
        
        
        if status == False:
            self.lexer.pos = pos
            self.current_token = token

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

        pos = self.lexer.pos
        token = self.current_token
        
        op = ["BUFF", "DEBUFF", "HEAL", "POISON"]

        if self.current_token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            if self.current_token.type == "ATRIBUIDOR":
                self.eat("ATRIBUIDOR")
                if self.current_token.type == "IDENTIFIER":
                    self.eat("IDENTIFIER")
                    print("banana", self.current_token)
                    if self.current_token.type in op:
                        if self.current_token.type == "BUFF":
                            self.eat("BUFF")
                        elif self.current_token.type == "DEBUFF":
                            self.eat("DEBUFF")
                        elif self.current_token.type == "HEAL":
                            self.eat("HEAL")
                        elif self.current_token.type == "POISON":
                            self.eat("POISON")
                        if self.current_token.type == "IDENTIFIER":
                            self.eat("IDENTIFIER")
                            if self.current_token.type == "EOL":
                                self.eat("EOL")
                                status = self.expr()
                elif self.current_token.type == "INTEGER":
                    self.eat("INTEGER")
                    if self.current_token.type in op:
                        if self.current_token.type == "BUFF":
                            self.eat("BUFF")
                        elif self.current_token.type == "DEBUFF":
                            self.eat("DEBUFF")
                        elif self.current_token.type == "HEAL":
                            self.eat("HEAL")
                        elif self.current_token.type == "POISON":
                            self.eat("POISON")
                        if self.current_token.type == "INTEGER":
                            self.eat("INTEGER")
                            if self.current_token.type == "EOL":
                                self.eat("EOL")
                                status = self.expr()
    
        if status == False:
            self.lexer.pos = pos
            self.current_token = token

        return status

    def attrib(self):
        """
        attrib: IDENTIFIER ATRIBUIDOR IDENTIFIER EOL | 
                IDENTIFIER ATRIBUIDOR (INTEGER | STRING) EOL
        """

        print("entrou attrib")

        if self.current_token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            if self.current_token.type == "ATRIBUIDOR":
                self.eat("ATRIBUIDOR")
                if self.current_token.type == "IDENTIFIER":
                    self.eat("IDENTIFIER")
                    if self.current_token.type == "EOL":
                        self.eat("EOL")
                        status = self.expr()
                elif self.current_token.type in ["INTEGER", "STRING"]:
                    if self.current_token.type == "INTEGER":
                        self.eat("INTEGER")
                    elif self.current_token.type == "STRING":
                        self.eat("STRING")
                    if self.current_token.type == "EOL":
                        self.eat("EOL")
                        status = self.expr()


        status = False

        pos = self.lexer.pos
        token = self.current_token



        if status == False:
            self.lexer.pos = pos
            self.current_token = token

        return status

    def ifElse(self):
        '''
        if-else: HIT cond L_CHAVE S R_CHAVE MISS L_CHAVE S  R_CHAVE S | 
                 HIT cond L_CHAVE S R_CHAVE
        '''
        status = False

        pos = self.lexer.pos
        token = self.current_token



        if status == False:
            self.lexer.pos = pos
            self.current_token = token

        return status

    def cond(self):
        '''
        cond: IDENTIFIER comp IDENIFIER |
              INTEGER comp INTEGER |
              STRING DODGE STRING
        '''
        status = False

        pos = self.lexer.pos
        token = self.current_token

        
        if self.current_token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            status = self.comp()
            if self.current_token.type == "IDENTIFIER":
                self.eat("IDENTIFIER")
                status = self.expr()



        if status == False:
            self.lexer.pos = pos
            self.current_token = token

        return status

    def comp(self):
        '''
        comp: ATTACK | DEFENSE | DODGE | CRITICAL | BLOCK 
        '''
        status = False

        pos = self.lexer.pos
        token = self.current_token

        if self.current_token.type == "ATTACK":
            self.eat("ATTACK")
            status = self.expr()
        elif self.current_token.type == "DEFENSE":
            self.eat("DEFENSE")
            status = self.expr()
        elif self.current_token.type == "DODGE":
            self.eat("DODGE")
            status = self.expr()
        elif self.current_token.type == "CRITICAL":
            self.eat("CRITICAL")
            status = self.expr()
        elif self.current_token.type == "BLOCK":
            self.eat("BLOCK")
            status = self.expr()

        if status == False:
            self.lexer.pos = pos
            self.current_token = token

        return status


    def expr(self):
        print(self.current_token)

        '''
        expr: vardec | basicop | attib | if-else | Ɛ
        vardec: (INTEGER | SWORD) IDENTIFIER EOL
        basicop: IDENTIFIER ATRIBUIDOR IDENTIFIER (BUFF | DEBUFF | HEAL | POISON) IDENTIFIER EOL |
                 IDENTIFIER ATRIBUIDOR INTEGER (BUFF | DEBUFF | HEAL | POISON) INTEGER EOL
        attrib: IDENTIFIER ATRIBUIDOR IDENTIFIER EOL | 
                IDENTIFIER ATRIBUIDOR (INTEGER | STRING) EOL
        if-else: HIT cond L_CHAVE S R_CHAVE MISS L_CHAVE S  R_CHAVE S | 
                 HIT cond L_CHAVE S R_CHAVE
        cond: IDENTIFIER comp IDENIFIER | NUMERIC comp NUMERIC | STRING DODGE STRING
        comp: ATTACK | DEFENSE | DODGE | CRITICAL | BLOCK 
        '''


        if self.vardec():
            print("vardec")
            return True
        elif self.basicop():
            print("basicop")
            return True
        elif self.attrib():
            print("attrib")
            return True
        elif self.cond():
            print("cond")
            return True
        elif self.comp():
            print("comp")
            return True
        elif self.current_token.type == 'EOF':
            return True
        else:
            print(self.current_token)
            self.error()
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


if __name__ == '__main__':
    main()