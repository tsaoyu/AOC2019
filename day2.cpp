#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class Day2{
    private:
        vector<int> inputs;

    public:
        Day2(string input_name){
            ifstream infile(input_name);
            string line;
            while (getline(infile, line, ',')){
                inputs.push_back(stoi(line));
            };
        };

        int final_state_left(int verb, int noun){
            vector<int> input;
            input = inputs;
            int pos = 0;
            input[1] = verb;
            input[2] = noun;
            while (true){
                if (input[pos] == 1){
                    input[input[pos+3]] = input[input[pos+1]] + input[input[pos+2]];
                }
                else if (input[pos] == 2) {
                    input[input[pos+3]] = input[input[pos+1]] * input[input[pos+2]];
                }
                else if (input[pos] == 99){
                    break;
                }
                pos += 4;
            }
            return input[0];
        }

        int terminate_noun_verb(){
            for (int i=0; i<100; i++){
                for (int j=0; j<100; j++){
                    if (final_state_left(i, j) == 19690720){
                        return 100 * i + j;
                    }
                }
            }

        }
};

int main(){
    
    Day2 day2 = Day2("input.txt");

    cout<< day2.final_state_left(12, 2) << endl;
    cout<< day2.terminate_noun_verb() << endl;

    return 0;
}