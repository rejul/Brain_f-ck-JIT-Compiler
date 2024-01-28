from enum import Enum

class token(Enum):
    # Token types
    OP_INC ='+'
    OP_DEC = '-'
    OP_LEFT = '<'
    OP_RIGHT = '>'
    OP_INPUT = ','
    OP_OUTPUT = '.'
    OP_JUMP_IF_ZERO = '['
    OP_JUMP_IF_NOT_ZERO = ']'
   




        
class lexer:
    def __init__(self, args1, count):
        self.args1 = args1
        self.count = count

    





def checker(*args):
    buf = []
    stack_jump = []
    #print(len(args))
    i = 0
    while i < len(args)-1:  # Update the condition here
        # main loop

        if args[i] == token.OP_INC.value or args[i] == token.OP_DEC.value or args[i] == token.OP_LEFT.value or args[i] == token.OP_RIGHT.value or args[i] == token.OP_INPUT.value or args[i] == token.OP_OUTPUT.value :
            count = 1
            while i < len(args) - 1 and args[i] == args[i + 1]:
                count += 1
                i += 1
            #print(f'{args[i]} = {count}')
            buf.append(lexer(args[i],count))
            #print(buf)

        elif args[i] == token.OP_INPUT.value:
            pass
        elif args[i] == token.OP_OUTPUT.value:
            pass
        elif args[i] == token.OP_JUMP_IF_ZERO.value:
            pass
        elif args[i] == token.OP_JUMP_IF_NOT_ZERO.value:
            if len(stack_jump) == 0:
                print("Error: ] without [")
                break
            pass
        #print(i)
        i += 1  # increment i to avoid infinite loop

    return  buf
if __name__ == "__main__":
   
    open_file = open("hello.bf", "r")
    file = open_file.read()
    s=checker(*file)
    for i in s:
        print(f'{i.args1} : {i.count}')
       # print(i.count)
   # print(s)
   # print(checker.count_inc)