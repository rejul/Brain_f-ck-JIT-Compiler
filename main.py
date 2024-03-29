from enum import Enum
#from collections import deque

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

    


stack_jump = []


def checker(*args):
    buf = []
    #stack_jump= deque()
    global stack_jump
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
            current_hidden_address = i
            count = 0
            #print(f'{i}here')# actual address before adding to stack 
            ind=len(buf)
            #if buf[ind-1].value==0:
            #    pass
            buf.append(lexer(args[i],count))
           
            stack_jump.append(ind)
            pre_val=ind-1
            
            
        elif args[i] == token.OP_JUMP_IF_NOT_ZERO.value:
            #f the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.
            if len(stack_jump) == 0:
                print(f'{i+1} - Synatx error: ] without [')
                buf.clear()
                break

            sp_pointer= len(stack_jump)-1 #last index of stack_jump
            sp_return=stack_jump[sp_pointer]#get the value of last element of stack_jump

            buf.append(lexer(args[i],sp_return+1)) #append the value of sp_return to buf's (buf is a list )current object's count

            Cur_pointer=len(buf)-1
            #get object-->buf[sp_return].Countg
            buf[sp_return].count=Cur_pointer+1 #Backpatching '[' value points to address of ']' 
       
            stack_jump.pop()

           
       
        i += 1  # increment i to avoid infinite looprem
    
    return  buf #return buf to main function 

if __name__ == "__main__":

    result=[]
   
    open_file = open("hello.bf", "r")
    file = open_file.read()
    s=checker(*file)
    for i in s:
        print(f'{s.index(i)}:{i.args1} : {i.count}')

       # print(i.count) buffer arg and count
    i=0
    while i < len(s): 

        if s[i].args1==token.OP_INC.value:
            result.append(s[i].count) #add data pointer by value of count
            i+=1 #buffer arg and count next index

        elif s[i].args1==token.OP_DEC.value:
            
            """current_index=len(result)-1 #get the last index of result
            result[current_index]=result[current_index]-s[i].count"""
            last_elm=result.pop()
            result.append(last_elm-s[i].count)


   # print(s
    ''' fori in stack_jump:
        print(f'{i}help')'''
   # print(checker.count_inc)