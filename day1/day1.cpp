#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class Day1{
    private:
        vector<int> input;

    public:
        Day1(string input_name){
            ifstream infile(input_name);
            string line;
            while (getline(infile, line)){
                input.push_back(stoi(line));
            };
        };

        int sumOfFuel(){
            int fuel = 0;
            for (auto i: input){
                fuel += i / 3 -2;
            }

            return fuel;
        }

        int sumOfFuelAdded(){
            int fuel = 0;
            for (auto i: input){
                int added_fuel = i;
                while (added_fuel){
                    added_fuel = max(added_fuel / 3 -2, 0);
                    fuel += added_fuel;
                }
            }
            return fuel;

        }
        
};

int main(){
    
    Day1 day1 = Day1("input.txt");
    cout<< day1.sumOfFuel() << endl;
    cout<< day1.sumOfFuelAdded() << endl;

    return 0;
}