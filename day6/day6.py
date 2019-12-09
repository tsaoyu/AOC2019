from itertools import permutations
def diagnosis(contents, input_vals=[5]):
    pos = 0
    inputs_pos = 0
    instructions = contents[:]
    parameters_no = {'01':3, '02':3, '03':1, '04':1, '05':2, '06':2, '07':3, '08':3}
    
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
            if int(op):
                op_list.append(pos+1)
            else:
                op_list.append(instructions[pos+1])
            pos += 1

        output = None
        direct_jump = False
        if opcode == '01':
            instructions[op_list[2]] = instructions[op_list[0]] + instructions[op_list[1]]
        elif opcode == '02':
            instructions[op_list[2]] = instructions[op_list[0]] * instructions[op_list[1]]
        elif opcode == '03':
            instructions[op_list[0]] = input_vals[inputs_pos]
            inputs_pos = 1
        elif opcode == '04':
            if instructions[op_list[0]]:
                output = instructions[op_list[0]]
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
    return output, stopped, instructions

if __name__ == "__main__":

    with open("input.txt",'r') as f:
         content = f.read()

    content = [int(i) for i in content.split(',')]
    # content = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    # content = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    # content = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    max_output = 0
    p = list(permutations(range(5)))
    for i in p:
        output = 0
        for j in i:
            o, stopped, _ = diagnosis(content,[j,output])
            output = o if o is not None else output
            max_output = max(max_output, output)
    print(max_output)
    
    max_output = 0
    p2 = list(permutations(range(5,10)))
    
    for i in p2:
        output = 0
        running = [True] * 5
        state_store = [None]*5
        while True in running:
            for j in range(5):
                if state_store[j] is not None:
                    o, stopped, state = diagnosis(state_store[j],[i[j], output])
                else:
                    o, stopped, state = diagnosis(content,[i[j], output])
                state_store[j] = state 
                output = o if o is not None else output
                if stopped:
                    running[j] = False
        max_output = max(max_output, output)
    print(max_output)
