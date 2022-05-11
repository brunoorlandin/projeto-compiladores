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
        
        self.ifQuantity = 0

        self.listaTokens =[]
        self.posListaTokens = 0

        token = lexer.get_next_token()
        self.current_token = token
        while token.type != "EOF":
          self.listaTokens.append(token)
          token = lexer.get_next_token()
        self.listaTokens.append(token)

        print(self.listaTokens)


    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.posListaTokens += 1
            self.current_token = self.listaTokens[self.posListaTokens]
        else:
            self.error()

    def vardec(self):
        print("Entrou VARDEC")
        '''vardec: (SHIELD | SWORD) IDENTIFIER EOL EXPR'''
        status = False
        pos = self.posListaTokens


        if self.current_token.type == "SHIELD":
            self.eat("SHIELD")

            if self.current_token.type == "IDENTIFIER":
                self.eat("IDENTIFIER")
                
                if self.current_token.type == "EOL":
                    self.eat("EOL")

                    status = self.expr()
        
        elif self.current_token.type == "SWORD":
            self.eat("SWORD")

            if self.current_token.type == "IDENTIFIER":
                self.eat("IDENTIFIER")

                if self.current_token.type == "EOL":
                    self.eat("EOL")

                    status = self.expr()

        if status == False:
            self.posListaTokens = pos
            self.current_token = self.listaTokens[pos]

        print("Retorna de VARDEC ", status)
        return status
    
    def basicop(self):
        print("Entrou BASICOP")
        """
        basicop: IDENTIFIER ATRIBUIDOR IDENTIFIER (BUFF | DEBUFF | HEAL | POISON) IDENTIFIER EOL EXPR|
                 IDENTIFIER ATRIBUIDOR INTEGER (BUFF | DEBUFF | HEAL | POISON) INTEGER EOL EXPR
        """

        status = False

        pos = self.posListaTokens
        
        op = ["BUFF", "DEBUFF", "HEAL", "POISON"]

        if self.current_token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            if self.current_token.type == "ATRIBUIDOR":
                self.eat("ATRIBUIDOR")
                if self.current_token.type == "IDENTIFIER":
                    self.eat("IDENTIFIER")
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
            self.posListaTokens = pos
            self.current_token = self.listaTokens[pos]

        print("Retorna de BASICOP ", status)
        return status

    def attrib(self):
        print("Entrou ATTRIB")
        
        """
        attrib: IDENTIFIER ATRIBUIDOR IDENTIFIER EOL EXPR | 
                IDENTIFIER ATRIBUIDOR (INTEGER | STRING) EOL EXPR
        """

        pos = self.posListaTokens

        status = False

        if self.current_token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")

            if self.current_token.type == "ATRIBUIDOR":
                self.eat("ATRIBUIDOR")

                if self.current_token.type == "IDENTIFIER":
                    self.eat("IDENTIFIER")

                    if self.current_token.type == "EOL":
                        self.eat("EOL")
                        
                        status = self.expr()

                
                elif self.current_token.type in ("INTEGER", "STRING"):
                    if self.current_token.type == "INTEGER":
                        self.eat("INTEGER")
                    elif self.current_token.type == "STRING":
                        self.eat("STRING")

                    if self.current_token.type == "EOL":
                        self.eat("EOL")
                        status = self.expr()
                
        
        if status == False:
            self.posListaTokens = pos
            self.current_token = self.listaTokens[pos]

        print("Retorna de ATTRIB ", status)
        return status
        

    def ifElse(self):
        print("Entrou ifELSE")
        '''
        if-else: HIT cond L_CHAVE EXPR R_CHAVE MISS L_CHAVE EXPR  R_CHAVE EXPR | 
                 HIT cond L_CHAVE EXPR R_CHAVE EXPR
        '''
        status = False
        pos = self.posListaTokens

        if self.current_token.type == "HIT":
            self.eat("HIT")

            if self.cond():
            
                if self.current_token.type == "L_CHAVE":
                    self.eat("L_CHAVE")

                    self.ifQuantity += 1

                    if self.expr():

                        

                        if self.current_token.type == "R_CHAVE":
                            self.eat("R_CHAVE")
                        
                            if self.current_token.type == "MISS":
                                self.eat("MISS")

                                if self.current_token.type == "L_CHAVE":
                                    self.eat("L_CHAVE")

                                    self.ifQuantity += 1

                                    if self.expr():

                                        if self.current_token.type == "R_CHAVE":
                                            self.eat("R_CHAVE")
                                            status = self.expr()

                            else:
                                status = self.expr()
        
        if status == False:
            self.posListaTokens = pos
            self.current_token = self.listaTokens[pos]

        print("Retorna de ifElse ", status)
        return status

    def cond(self):
        print("Entrou COND")
        '''
        cond: IDENTIFIER comp IDENTIFIER |
              INTEGER comp INTEGER |
              STRING DODGE STRING
        '''
        status = False
        pos = self.posListaTokens


        if self.current_token.type == "IDENTIFIER":
            self.eat("IDENTIFIER")
            
            if self.comp():
                
                if self.current_token.type == "IDENTIFIER":
                    self.eat("IDENTIFIER")

                    status = True
        
        elif self.current_token.type == "INTEGER":
            self.eat("INTEGER")
            
            if self.comp():

                if self.current_token.type == "INTEGER":
                    self.eat("INTEGER")

                    status = True


        if status == False:
            self.posListaTokens = pos
            self.current_token = self.listaTokens[pos]

        print("Retorna de COND ", status)
        return status

    def comp(self):
        print("Entrou COMP")
        '''
        comp: ATTACK | DEFENSE | DODGE | CRITICAL | BLOCK 
        '''
        status = False
        pos = self.posListaTokens

        if self.current_token.type in ("ATTACK", "DEFENSE", "DODGE", "CRITICAL", "BLOCK"):
            status = True
            self.eat(self.current_token.type)


        if status == False:
            self.posListaTokens = pos
            self.current_token = self.listaTokens[pos]

        print("Retorna de COMP ", status)
        return status


    def expr(self):
        #print(self.current_token)
        print("Entrou EXPR")
        pos = self.posListaTokens

        '''
        expr: vardec | basicop | attib | if-else | Ɛ
        vardec: (INTEGER | SWORD) IDENTIFIER EOL EXPR
        basicop: IDENTIFIER ATRIBUIDOR IDENTIFIER (BUFF | DEBUFF | HEAL | POISON) IDENTIFIER EOL EXPR|
                 IDENTIFIER ATRIBUIDOR INTEGER (BUFF | DEBUFF | HEAL | POISON) INTEGER EOL EXPR
        attrib: IDENTIFIER ATRIBUIDOR IDENTIFIER EOL EXPR | 
                IDENTIFIER ATRIBUIDOR (INTEGER | STRING) EOL EXPR
        if-else: HIT cond L_CHAVE EXPR R_CHAVE MISS L_CHAVE EXPR R_CHAVE EXPR | 
                 HIT cond L_CHAVE EXPR R_CHAVE EXPR
        cond: IDENTIFIER comp IDENTIFIER | NUMERIC comp NUMERIC | STRING DODGE STRING
        comp: ATTACK | DEFENSE | DODGE | CRITICAL | BLOCK 
        '''

        
        
        
        if self.vardec():
            print("Return EXPR True")
            return True
        
        elif self.basicop():
            print("Return EXPR True")
            return True
        
        elif self.attrib():
            print("Return EXPR True")
            return True

        elif self.ifElse():
            print("Return EXPR True")
            return True
        
        elif self.current_token.type == 'EOF':
            print("Return EXPR True")
            return True

        elif self.current_token.type == 'R_CHAVE' and self.ifQuantity > 0:
            self.ifQuantity -= 1
            print("Return EXPR True")
            return True
        else:

            print("Return EXPR False")
            self.posListaTokens = pos
            self.current_token = self.listaTokens[pos]
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

    text = ""
    for i in range(len(lines)):
        text += lines[i]

    lexer = Lexer(text)
    interpreter = Interpreter(lexer)
    result = interpreter.expr()

    print(result)


if __name__ == '__main__':
    main()