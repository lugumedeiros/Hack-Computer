#Problem at M-1

import re

rpl_dest = {
    #Destination
    # 'AMD;'   : '111',
    # 'AD;'    : '110',
    # 'MD;'    : '011',
    # 'AM;'    : '101',
    # '0;'     : '000',
    # 'M;'     : '001',
    # 'D;'     : '010',
    # 'A;'     : '100',
    '@'      : '0',
    'AMD='   : '111',
    'MD='    : '011',
    'AM='    : '101',
    'AD='    : '110',
    '0='     : '000',
    'M='     : '001',
    'D='     : '010',
    'A='     : '100',
}
repl_op = {
    #Operation
    '=D|M'   : '1010101',
    '=D&M'   : '1000000',
    '=M-D'   : '1000111',
    '=D-M'   : '1010011',
    '=D+M'   : '1000010',
    '=M-1'   : '1110010',
    '=M+1'   : '1110111',
    '=D|A'   : '0010101',
    '=D+1'   : '0011111',
    '=A+1'   : '0110111',
    '=!A'    : '0110001',
    '=D-1'   : '0001110',
    '=A-1'   : '0110010',
    '=D+A'   : '0000010',
    '=D-A'   : '0010011',
    '=A-D'   : '0010011',
    '=D&A'   : '0000000',
    '=-A'    : '0110011',
    '=!M'    : '1110001',
    '=!D'    : '0001101',
    '=-D'    : '0001111',
    '=M'     : '1110000',
    '=A'     : '0110000',
    '=D'     : '0001100',
    '=-1'    : '0111010',
    '=1'     : '0111111',
    '=0'     : '0101010'
}
repl_opjmp = {
    'D|M;'   : '1010101',
    'D&M;'   : '1000000',
    'M-D;'   : '1000111',
    'D-M;'   : '1010011',
    'D+M;'   : '1000010',
    'M-1;'   : '1110010',
    'M+1;'   : '1110111',
    'D|A;'   : '0010101',
    'D+1;'   : '0011111',
    'A+1;'   : '0110111',
    '!A;'    : '0110001',
    'D-1;'   : '0001110',
    'A-1;'   : '0110010',
    'D+A;'   : '0000010',
    'D-A;'   : '0010011',
    'A-D;'   : '0010011',
    'D&A;'   : '0000000',
    '-A;'    : '0110011',
    '!M;'    : '1110001',
    '!D;'    : '0001101',
    '-D;'    : '0001111',
    'M;'     : '1110000',
    'A;'     : '0110000',
    'D;'     : '0001100',
    '-1;'    : '0111010',
    '1;'     : '0111111',
    '0;'     : '0101010',
}
rpl_jmp = {
    #Jumps
    'JGT'	: '001',
    'JEQ'	: '010',
    'JGE' 	: '011',
    'JLT' 	: '100',
    'JNE'	: '101',
    'JLE'	: '110',
    'JMP'	: '111'
}

custom_vars = {
    '@R0'    : '0',  
    '@R1'    : '1',
    '@R2'    : '2',
    '@R3'    : '3',
    '@R4'    : '4',
    '@R5'    : '5',
    '@R6'    : '6',
    '@R7'    : '7',
    '@R8'    : '8',
    '@R9'    : '9',
    '@R10'   : '10',
    '@R11'   : '11',
    '@R12'   : '12',
    '@R13'   : '13',
    '@R14'   : '14',            
    '@R15'   : '15',
    '@SCREEN': '16384',
    '@KBD'   : '24576',
    'SP'     : '0',
    'LCL'    : '1',
    'ARG'    : '2',
    'THIS'   : '3',
    'THAT'   : '4'
}


file_name = input("File name: ")
end_file = file_name.replace('.asm', '.hack')
print(end_file)
blocked_lines = [] #lines that can't be changed anymore

#REMOVE COMMENTS AND BLANKS
with open(file_name, 'r') as file, open('tempa.txt', 'w+') as temp:
    uncommented_lines = []
    for line in file:
        index = line.find("//")
        if (index != -1):
            uncommented_lines.append(line[:index])
        else:
            uncommented_lines.append(line)

    for line in uncommented_lines:
        if (line.strip()):
            line = re.sub(' +', ' ', line)
            temp.write(line)

#ADD CUSTOM LABELS
with open('tempa.txt', 'r') as file, open('tempb.txt', 'w+') as temp:
    addresses_changed = []
    line_index = 0 
    for line in file:
        addresses_changed = re.findall(r'\((.*?)\)', line)
        if not addresses_changed:
            line_index += 1
            temp.write(line)
        for word in addresses_changed:
            custom_vars['@'+word] = str(line_index)
#print(custom_vars)

#CHANGE CUSTOM VARS INTO BINARY      
sorted_dict = {k: v for k, v in sorted(custom_vars.items(), key=lambda item: len(item[0]), reverse=True)} #idk how to use REGEX lol
    #dictionary was sorted to avoid replacing substring


#print(sorted_dict)
with open("tempb.txt", 'r') as file, open('tempc.txt', 'w+') as temp:
    line_index = 0
    for line in file:
        line_index += 1
        for name, binary in sorted_dict.items():
            if name in line:
                blocked_lines.append(line_index-1)
            line = line.replace(name, str(format(int(binary), '016b')))
        temp.write(line)

new_dict = {}
with open("tempc.txt", 'r') as file, open('tempd.txt', 'w+') as temp:
    opline_index = 0
    available_address = 16
    for line in file:
        is_a_instruction = False
        if '@' in line:
            line = line.replace('@', '')
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            is_a_instruction = True
            blocked_lines.append(opline_index)
            try:
                line_int = int(line)
                line_int = int(line)
                line = format(line_int, '016b')
            except ValueError:
                if (line in new_dict):
                    line = format(new_dict[line], '016b')
                else: 
                    line_int = available_address
                    new_dict[str(line)] = available_address
                    line = format(line_int, '016b')
                    available_address += 1

        opline_index += 1
        temp.write(line)
        if is_a_instruction:
            temp.write('\n')

with open('tempd.txt', 'r') as file, open(end_file, 'w+') as temp:
    opline_index = 0
    for line in file:
        bool_changed = False
        bool_jmp = False
        current_nline = '111'
        if opline_index not in blocked_lines:
            for name, binary in repl_op.items():
                if name in line:
                    current_nline += binary
                    bool_changed = True
                    bool_jmp = False
                    break
                else:
                    bool_jmp = True
            if bool_jmp:
                for name, binary in repl_opjmp.items():
                    if name in line:
                        current_nline += binary
                        current_nline += '000'
            for name, binary in rpl_dest.items():
                if name in line:
                    current_nline += binary
                    bool_changed = True
                    break #############
            for name, binary in rpl_jmp.items():
                if name in line:
                    current_nline += binary
                    bool_changed = True
                    bool_jmp = True

        if not bool_jmp:
            current_nline += '000'

        current_nline = current_nline.replace(' ', '')
        line = line.replace(' ', '')
        if bool_changed:
            temp.write(current_nline+'\n')
        else:
            temp.write(line)
        opline_index += 1

