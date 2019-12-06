#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

class Day5{
    private:
        vector<int> inputs;
        map<string, int> m = {{"01",3}, {"02",3}, {"03",1}, {"04",1}, {"05",2}, {"05",2}, {"06",2}, {"07",3}, {"08",3}};
    public:
        Day5(string input_name){
            ifstream infile(input_name);
            string line;
            while (getline(infile, line, ',')){
                inputs.push_back(stoi(line));
            };
        };

        void set_input(const vector<int> & input){
            inputs = input;
        }
        int diagnosis(const int& input_val){
            int pos = 0;
            while (true){
                string instruct = to_string(inputs[pos]);
                while (instruct.size() <5){
                    instruct = '0' + instruct;
                }

                string opcode = instruct.substr(3);
                if (opcode == "99"){
                    break;
                }

                vector<int> op_list;
                for (auto i=0; i<m[opcode];i++){
                    if (instruct[2-i] == '1'){
                        op_list.push_back(pos+1);
                    }
                    else{
                        op_list.push_back(inputs[pos+1]);
                    }
                    pos += 1;
                }
                
                if (opcode == "01"){
                    inputs[op_list[2]] = inputs[op_list[0]] + inputs[op_list[1]];
                }
                else if (opcode == "02"){
                    inputs[op_list[2]] = inputs[op_list[0]] * inputs[op_list[1]];
                }
                else if (opcode == "03"){
                    inputs[op_list[0]] = input_val;
                }
                else if (opcode == "04"){
                    if (inputs[op_list[0]]){
                        cout << inputs[op_list[0]] << endl;
                    }    
                }
                else if (opcode == "05"){
                    if (inputs[op_list[0]]){
                        pos = inputs[op_list[1]];
                        continue;
                    }    
                }
                else if (opcode == "06"){
                    if (inputs[op_list[0]] == 0){
                        pos = inputs[op_list[1]];
                        continue;
                    }  
                }
                else if (opcode == "07"){
                    if (inputs[op_list[0]] < inputs[op_list[1]]){
                        inputs[op_list[2]] = 1;
                    }
                    else{
                        inputs[op_list[2]] = 0;
                    }
                }
                else if (opcode == "08"){
                    if (inputs[op_list[0]] == inputs[op_list[1]]){
                        inputs[op_list[2]] = 1;
                    }
                    else{
                        inputs[op_list[2]] = 0;
                    }
                }
                pos += 1;
            }
        }
        
};

int main(){
    
    Day5 day5 = Day5("input.txt");

    //day5.set_input({3,3,1108,-1,8,3,4,3,99});
    day5.diagnosis(1);
    day5.diagnosis(5);

    return 0;
}