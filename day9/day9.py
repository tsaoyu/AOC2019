def diagnosis(contents, input_vals=[2]):
    pos = 0
    relative_pos = 0
    inputs_pos = 0
    instructions = contents[:]
    mem = {}
    output_list = []
    i = 0
    for instruction in instructions:
        mem[i] = instruction
        i += 1
    parameters_no = {'01':3, '02':3, '03':1, '04':1, '05':2, '06':2, '07':3, '08':3, '09':1}
    
    stopped = False
    while True:
        instruct = instructions[pos]
        long_instruct = '{:>05}'.format(str(instructions[pos]))
        opcode = long_instruct[-2:]

        if opcode == '99':
            stopped = True
            break
        parameter_len = parameters_no[opcode]

        op_list = []
        for op in long_instruct[2::-1][:parameter_len]:
            if int(op) == 1:
                arg = pos+1
            elif int(op) == 2:
                arg = relative_pos + instructions[pos+1]
            else:
                arg = instructions[pos+1]
            if arg not in mem.keys():
                mem[arg] = 0
            op_list.append(arg)
            pos += 1

        output = None
        direct_jump = False
        if opcode == '01':
            mem[op_list[2]] = mem[op_list[0]] + mem[op_list[1]]
        elif opcode == '02':
            mem[op_list[2]] = mem[op_list[0]] * mem[op_list[1]]
        elif opcode == '03':
            mem[op_list[0]] = input_vals[inputs_pos]
            inputs_pos = 1
        elif opcode == '04':
            output_list.append(mem[op_list[0]])
        elif opcode == '05':
            if mem[op_list[0]]:
                pos = mem[op_list[1]]
                direct_jump = True
        elif opcode == '06':
            if mem[op_list[0]] == 0:
                pos = mem[op_list[1]]
                direct_jump = True
        elif opcode == '07':
            mem[op_list[2]] = 1 if mem[op_list[0]] < mem[op_list[1]] else 0
        elif opcode == '08':
            mem[op_list[2]] = 1 if mem[op_list[0]] == mem[op_list[1]] else 0
        elif opcode == '09':
            relative_pos += mem[op_list[0]]

        if direct_jump:
            pos = pos
        elif instruct != mem[pos-parameter_len]:
            pos -= parameter_len
        else:
            pos += 1

    return output_list, stopped, mem

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        output = f.read()

    output = [int(i) for i in output.split(',')]
    print(diagnosis(output, input=[1])[0])
    print(diagnosis(output, input=[2])[0])