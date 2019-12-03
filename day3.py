class Day3:

    def __init__(self):
        pass

    def closest_intersection(self, path1, path2):
        
        m = {"R":(1,0), "L":(-1,0), "U":(0,1), "D":(0,-1)}
        trace1 = {}
        current_pos = (0, 0)
        length = 0
        for move in path1:
            direction, distance = m[move[0]], int(move[1:])
            for d in range(distance):
                current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
                length += 1
                trace1[current_pos] = length
        
        trace2 = {}
        current_pos = (0, 0)
        length = 0
        for move in path2:
            direction, distance = m[move[0]], int(move[1:])
            for d in range(distance):
                current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
                length += 1
                trace2[current_pos] = length
        
        intersections = set(trace1.keys()) & set(trace2.keys())

        print(min([abs(x) +  abs(y) for x,y in intersections]))
        print(min([trace1[p] +  trace2[p] for p in intersections]))
        

if __name__ == "__main__":

    with open("input.txt","r") as f:
        output = f.readlines()

    path1, path2 = output
    path1 = path1.split(',')
    path2 = path2.split(',')
  
    Day3().closest_intersection(path1, path2)
