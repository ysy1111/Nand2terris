class parser:
    def __init__(self,s):
        self.s = s
        self.comp = ''
        self.dest = ''
        self.jump = ''
        
def decompose(s):
    
    comp_flag = False
    dest_flag = False
    jump_flag = False
    ps = parser(s)
    f1 = s.split('=')
    f2 = s.split(';')
    # print(s)
    if len(f1) == 1: # D;JMP type
        ps.dest = ''
        helper = s.split(';')
        ps.comp = helper[0]
        helper2 = helper[1].split('//')
        helper2 = helper2[0].split('\n')
        ps.jump = helper2[0]
    elif len(f2) == 1:
        ps.jump = ''
        helper = s.split('=')
        ps.dest = helper[0]
        helper2 = helper[1].split('//')
        helper2 = helper2[0].split('\n')
        ps.comp = helper2[0]
    else:
        ps.dest = f1[0]
        f3 = f1[1].split(';')
        ps.comp = f3[0]
        f4 = f3[1].split('//')
        ps.jump = f4[0]
    
    tmp = ''
    for i in ps.dest:
        if i != ' ':
            tmp += i
    ps.dest = tmp
    tmp = ''
    for i in ps.comp:
        if i != ' ':
            tmp += i
    ps.comp = tmp    
    tmp = ''
    for i in ps.jump:
        if i != ' ':
            tmp += i
    ps.jump = tmp
    return ps    
#ps = decompose(' D = M + 1 ; JGT  //comment') 
#print(ps.dest, ps.comp, ps.jump)
# D;JMP        comp  jump  
# D = M        dest  comp  
# D = M; JMP   dest  comp jump  