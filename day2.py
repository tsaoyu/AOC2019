class Day2:

    def __init__(self):
        pass

    def final_state_left(self, content, v=12, n=2):
        pos = 0
        instructions = content[:]
        instructions[1] = v
        instructions[2] = n 
        while True:
            if instructions[pos] == 1:
                instructions[instructions[pos+3]] = instructions[instructions[pos+1]] + instructions[instructions[pos+2]]
            elif instructions[pos] == 2:
                instructions[instructions[pos+3]] = instructions[instructions[pos+1]] * instructions[instructions[pos+2]]
            elif instructions[pos] == 99:
                break
            pos += 4
        return instructions[0]

    def terminate_noun_verb(self, instructions):
        for i in range(100):
            for j in range(100):
                if self.final_state_left(instructions, v=i, n=j) == 19690720:
                    return i*100 + j 

if __name__ == "__main__":

    with open("input.txt",'r') as f:
        content = f.read()

    content = [int(i) for i in content.split(',')]

    print(Day2().final_state_left(content))
    print(Day2().terminate_noun_verb(content))
    
