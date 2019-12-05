def diagnosis(contents, input_val=5):
    global pos 
    pos = 0
    instructions = contents[:]
    parameters_no = {'01':3, '02':3, '03':1, '04':1, '05':2, '06':2, '07':3, '08':3}
    
    
    while True:
        instruct = instructions[pos]
        long_instruct = '{:>05}'.format(str(instructions[pos]))
        opcode = long_instruct[-2:]

        if opcode == '99':
            break
        parameter_len = parameters_no[opcode]

        op_list = []
        for op in long_instruct[2::-1][:parameter_len]:
            if int(op):
                op_list.append(pos+1)
            else:
                op_list.append(instructions[pos+1])
            pos += 1

        
        direct_jump = False
        if opcode == '01':
            instructions[op_list[2]] = instructions[op_list[0]] + instructions[op_list[1]]
        elif opcode == '02':
            instructions[op_list[2]] = instructions[op_list[0]] * instructions[op_list[1]]
        elif opcode == '03':
            instructions[op_list[0]] = input_val
        elif opcode == '04':
            if instructions[op_list[0]]:
                print(instructions[op_list[0]])
        elif opcode == '05':
            if instructions[op_list[0]]:
                pos = instructions[op_list[1]]
                direct_jump = True
        elif opcode == '06':
            if instructions[op_list[0]] == 0:
                pos = instructions[op_list[1]]
                direct_jump = True
        elif opcode == '07':
            instructions[op_list[2]] = 1 if instructions[op_list[0]] < instructions[op_list[1]] else 0
        elif opcode == '08':
            instructions[op_list[2]] = 1 if instructions[op_list[0]] == instructions[op_list[1]] else 0
        
        if direct_jump:
            pos = pos
        elif instruct != instructions[pos-parameter_len]:
            pos -= parameter_len
        else:
            pos += 1
                
    
    return instructions[0]

if __name__ == "__main__":

    with open("input.txt",'r') as f:
        content = f.read()

    content = [int(i) for i in content.split(',')]
    diagnosis(content, input_val=1) 
    diagnosis(content, input_val=5)    
        
    
