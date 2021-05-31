import Myparser
import argparse
import os 
from symbol2bit import *

if __name__ == '__main__':
    c = argparse.ArgumentParser(description='choose the file')
    c.add_argument('filename', type=str, help = 'filename')
    c.add_argument('foldername', type=str, help = 'foldername')
    args = c.parse_args()
    file_name = args.filename
    folder_name = args.foldername
    path = './{x1}/{x2}.asm'.format(x1=folder_name,x2=file_name)
    
    
    
    table = symbol_table()
    
    f = open(path,"r")
    p = 0
    for line in f:
        if line != '\n' and line[:2] != '//':
            break
        p+=1
        
    # print(initial_place) skip the comment part
    i = 0
    for line in f: # first scan 
        #print(line)
        if line[0] == '(':
            #print(i,line[1:-2])
            key = line[1:-2]
            value = i+1
            table.__add__(key,value)
        else:
            i+=1
    #print(table.symT)
    f.close()
    f = open(path,'r')
    out_path = './{x0}/{x1}.bincode'.format(x0=folder_name,x1=file_name)
    f_out = open(out_path,'w')
    j = 16
    for i,line in enumerate(f):
        if i>=p:
            k = 0
            while k < len(line):
                if line[k] == ' ':
                    k+=1
                else:
                    break
            first_effective_letter = line[k]
            #A-instruction
            if first_effective_letter == '@':
                end = k+1
                while end<len(line) and line[end]!=' ':
                    end+=1
                address = line[k+1:end]
                if address[-1] == '\n':
                    address = address[:-1]
                
                if address.isdigit():
                    bit_address = str(bin(int(address)))[2:]
                    bit_code = '0'*(16 - len(bit_address)) + bit_address
                else:
                    if address not in table.symT:
                        
                        key = address
                        value = j
                        table.__add__(key,value)
                        print(address,table.symT[address])
                        j+=1
                    
                    bit_address = str(bin(int(table.symT[address])))[2:]
                    bit_code = '0'*(16 - len(bit_address)) + bit_address
                print(bit_code)
                f_out.write(bit_code + '\n')
            elif first_effective_letter!='(': #C-instruction
                #print(line)
                ps = Myparser.decompose(line)
                dest = ps.dest
                comp = ps.comp
                jump = ps.jump
                # print('dest',dest)
                # print('comp',comp)
                # print('jump',jump)
                dest_c = code(dest)
                comp_c = code(comp)
                jump_c = code(jump)
                bit_code = '111' + comp_c.comp() + dest_c.dest() + jump_c.jump()
                f_out.write(bit_code + '\n')
                print(bit_code)
    f.close()
    f_out.close()