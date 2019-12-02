class Day1():
    def __init__(self):
        pass 
    
    def sum_of_fuel(self, inputs):
        fuel = 0
        for mass in inputs:
            fuel += int(mass) // 3 -2
        return fuel

    def sum_of_fuel_added(self,inputs):
        fuel = 0 
        for mass in inputs:
            added_fuel = int(mass)
            while added_fuel:
                added_fuel = max(added_fuel // 3 - 2, 0)
                fuel += added_fuel

        return fuel

if __name__ == "__main__":

    with open('input.txt', 'r') as r:
        content = r.readlines()
    
    print(Day1().sum_of_fuel(content))
    print(Day1().sum_of_fuel_added(content))

