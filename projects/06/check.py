import os

def compare(f,f1,f2):
    os.chdir(f)
    
    f_1 = open(f1+'.bincode','r')
    f_2 = open(f2+'.bincode','r')
    
    for i,line in enumerate(f_1):
        s1 = line
        s2 = f_2.readline()
        if s1 != s2:
            print(i,s1,s2)
            print('not equal')
            return
    print('GOOD')
    
compare('Pong','Pong','PongL')