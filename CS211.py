# Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOF = -1

# Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

# Global variables
charClass = None
lexeme = ''
nextChar = ''
lexLen = 0
nextToken = None
in_fp = None
index = 0
input_str = ''

def addChar():
    global lexeme, lexLen, nextChar
    lexeme += nextChar
    lexLen += 1

def getChar():
    global nextChar, charClass, index, input_str
    if index < len(input_str):
        nextChar = input_str[index]
        index += 1
        if nextChar.isalpha():
            charClass = LETTER
        elif nextChar.isdigit():
            charClass = DIGIT
        else:
            charClass = UNKNOWN
    else:
        nextChar = ''
        charClass = EOF

def getNonBlank():
    global nextChar
    while nextChar.isspace():
        getChar()

def lookup(ch):
    global nextToken
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MULT_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
    return nextToken

def lex():
    global lexeme, lexLen, nextToken
    lexeme = ''
    lexLen = 0
    getNonBlank()

    if charClass == LETTER:
        addChar()
        getChar()
        while charClass == LETTER or charClass == DIGIT:
            addChar()
            getChar()
        nextToken = IDENT

    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT

    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()

    elif charClass == EOF:
        nextToken = EOF
        lexeme = 'EOF'

    print(f"Next token is: {nextToken}, Next lexeme is {lexeme}")
    return nextToken

# Main driver
def main():
    global input_str, index
    input_str = "(sum + 47) / total"
    index = 0
    getChar()
    while True:
        token = lex()
        if token == EOF:
            break

if __name__ == '__main__':
    main()